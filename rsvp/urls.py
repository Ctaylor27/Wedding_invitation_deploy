# urls.py

from django.urls import path
from .views import index, RSVPView, submit_rsvp, landing, delete, login_user, create_user
from django.conf.urls.static import static
app_name = 'rsvp'

urlpatterns = [
    path('', landing, name='landing'),
    path('login', login_user, name="login"),
    path('create', create_user, name="create"),
    path('guestlist', index, name='index'),
    path('rsvp_form', RSVPView, name='rsvp_form'),
    path('submit', submit_rsvp, name='submit_rsvp'),
    path('del/<int:id>', delete, name='delete')

]
