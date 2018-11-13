from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jobs/home.html')

def alljobs(request):
    return render(request,'jobs/job.html')
