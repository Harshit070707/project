# consumer_service/models.py
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Meter Reading', 'Meter Reading'),
        # Add more types as needed
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Service Request #{self.id} - {self.type}"

class CustomerAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    # Add more account-related fields as needed

    def __str__(self):
        return f"Account: {self.account_number}"
