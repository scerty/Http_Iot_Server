# serializers.py

from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['door_status', 'temperature', 'timestamp']  # Specify the fields you want to include
