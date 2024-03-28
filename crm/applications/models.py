from django.db import models
from tutors.models import Tutors
from leads.models import Leads


class Application(models.Model):
    STATUS_CHOICES = [('new', 'New'), ('sent_profile',
                                       'Sent Profile'), ('cmi', 'CMI'), ('pending', "Pending ")]

    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE)
    preferred_rate = models.CharField(max_length=50)
    remarks = models.TextField(blank=True)
    timings = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='new')
    # Add other fields as needed

    def __str__(self):
        return f"{self.tutor.name} applied to {self.lead.name}"
