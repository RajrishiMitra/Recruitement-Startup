# forms.py
from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['job_title', 'job_category', 'job_description', 'job_location', 'company_name', 'contact_email']
