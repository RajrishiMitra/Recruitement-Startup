from django.shortcuts import render, redirect
from .forms import JobPostingForm  # Import the form for handling form data
from .models import JobPosting


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def jobs(request):
    return render(request, 'jobs.html')

def post_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful submission
    else:
        form = JobPostingForm()

    return render(request, 'post_job.html', {'form': form})

def job_post_submit(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful form submission
    else:
        form = JobPostingForm()
    
    return render(request, 'post_job.html', {'form': form})
