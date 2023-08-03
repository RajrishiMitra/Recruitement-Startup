# models.py
from django.db import models

class JobPosting(models.Model):
    job_title = models.CharField(max_length=100)
    job_category = models.CharField(max_length=50)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.job_title


