from django.contrib import admin
from .models import ServiceRequest, Customer, SupportRepresentative

# Register your models here.
admin.site.register(ServiceRequest)
admin.site.register(Customer)
admin.site.register(SupportRepresentative)