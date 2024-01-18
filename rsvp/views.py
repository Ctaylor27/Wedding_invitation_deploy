from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import RSVP, Attendee
from django.db import transaction
# Create your views here.

def index(request):
    rsvps = RSVP.objects.all()
    guests = Attendee.objects.all()
    context = { 'rsvps': rsvps, 'rsvp_count' : rsvps.count(), 'guest_count' : guests.count()}
    return render(request, 'rsvp/index.html', context)

def landing(request):
    return render(request, 'rsvp/landing.html')

def RSVPView(request):
    return render(request, 'rsvp/rsvp_form.html')

def submit_rsvp(request):
    if request.method == "POST":
        
        # Get the list of attendees from the POST request
        attendees = [request.POST.get(f'attendee_{i}') for i in range(1, int(request.POST.get('num_attendees', 0)) + 1)]

        # Create the RSVP based on the name and num_attendees provided
        rsvp = RSVP(name=request.POST['name'], party_total=request.POST['num_attendees'], email=request.POST['email'])
        rsvp.save()
        # Creat an Attendee for each and attach them to the RSVP
        for attendee in attendees:
            new_attendee = Attendee(name=attendee, rsvp=rsvp)
            new_attendee.save()

        return HttpResponseRedirect(reverse("rsvp:landing"))
    
def delete(request, id):
    try:
        with transaction.atomic():
            entry = RSVP.objects.get(id=id)
            attendees = Attendee.objects.filter(rsvp=entry)
            
            for attendee in attendees:
                attendee.delete()
            
            entry.delete()
        
        # If the transaction is successful, return a success response
        return HttpResponse(status=200)
    
    except RSVP.DoesNotExist:
        # Handle the case where the entry does not exist
        return HttpResponse("RSVP not found in DB", status=404)
    except Exception as e:
        # Handle other exceptions
        print(e)
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

    
