from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class RSVP(models.Model):
    name = models.CharField(max_length=200)
    party_total = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    email = models.EmailField(max_length=200, default="")

    def update_party_total(self):
        self.party_total = self.attendee_set.count() + 1
        self.save()
  
    def __str__(self) -> str:
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=200)
    rsvp = models.ForeignKey(RSVP, on_delete=models.CASCADE, related_name='attendees')

    def __str__(self) -> str:
        return self.name