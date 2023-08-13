from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect('submit_service_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'consumer_services/submit_request.html', {'form': form})

def track_service_request(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'consumer_services/track_request.html', {'service_requests': service_requests})
