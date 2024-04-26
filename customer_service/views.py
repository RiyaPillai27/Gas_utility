from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def home(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'home.html', {'service_requests': service_requests})

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'track_request.html', {'service_request': service_request})
