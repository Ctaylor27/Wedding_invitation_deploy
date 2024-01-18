# urls.py

from django.urls import path
from .views import index, RSVPView, submit_rsvp, landing, delete
from django.conf.urls.static import static
app_name = 'rsvp'

urlpatterns = [
    path('', index, name='index'),
    path('landing', landing, name='landing'),
    path('rsvp_form', RSVPView, name='rsvp_form'),
    path('submit', submit_rsvp, name='submit_rsvp'),
    path('del/<int:id>', delete, name='delete')

]
