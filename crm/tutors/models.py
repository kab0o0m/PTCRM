from django.db import models

# Create your models here.


class Tutors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    remarks = models.TextField()

    # Additional Information
    current_occupation = models.CharField(max_length=200)
    bio = models.TextField()

    # Documents
    profile_pic = models.FileField(upload_to='tutor/profile_pics/')
    certificate = models.FileField(upload_to='tutor/certificates/')
    resume = models.FileField(upload_to='tutor/resumes/')
    created_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE, related_name='profiles')
    additional_information = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile for {self.tutor.first_name} {self.tutor.last_name}"