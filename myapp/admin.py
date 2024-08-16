# admin.py

from django.contrib import admin
from .models import SensorData

# Register the SensorData model with the admin site
@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('door_status', 'temperature', 'timestamp')
    list_filter = ('door_status', 'timestamp')
    search_fields = ('door_status', 'temperature')
