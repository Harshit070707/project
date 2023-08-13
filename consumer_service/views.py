# consumer_service/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest, CustomerAccount
from django.contrib.auth.decorators import login_required

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'submit_service_request.html')

@login_required
def track_service_request(request, request_id):
    # Retrieve the requested service request and display its details
    pass

@login_required
def customer_account(request):
    # Display customer account information
    pass
