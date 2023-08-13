from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Connection Setup', 'Connection Setup'),
        ('Billing Inquiry', 'Billing Inquiry'),
        # Add more service types here
    ]

    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    details = models.TextField()
    attached_file = models.FileField(upload_to='attachments/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer_name} - {self.service_type}'
