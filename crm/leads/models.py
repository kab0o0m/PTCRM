from django.db import models
from tutors.models import Tutors
# Create your models here.


class Leads(models.Model):
    STATUS_CHOICES = [
        ('new_case', 'New Case'),
        ('tutors_sent', 'Tutors Sent'),
        ('tutors_needed', 'Tutors Needed'),
        ('closed', 'Closed'),
        ('activate_tuition_centres', 'Activate Tuition Centres'),
        ('premium_education', 'Premium Education'),
        ('issue_cases', 'Issue Cases'),
        ('follow_up_to_close', 'Follow Up to Close'),
        ('group_chats_created', 'Group Chats Created'),
        ('awaiting_confirmation', 'Awaiting Confirmation'),
        ('incomplete', 'Incomplete'),
    ]

    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    client_name = models.CharField(max_length=200)
    client_number = models.CharField(max_length=15)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='new_case')
    remarks = models.CharField(max_length=500)
    many_tutor_link = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    last_reviewed_date = models.DateTimeField(auto_now=True)


class TutorInformation(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('sent_profile', 'Sent Profile'),
        ('cmi', 'CMI'),
        ('pending', 'Pending')
    ]

    lead = models.ForeignKey(
        Leads, on_delete=models.CASCADE, related_name="tutors")
    tutor = models.OneToOneField(
        Tutors, on_delete=models.CASCADE, related_name="tutor_information")
    apply_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='new')
    preferred_rate = models.CharField(max_length=30)
    remarks = models.TextField()  # Assuming remarks can be longer text
    timings = models.CharField(max_length=100)
