# views.py

from django.http import JsonResponse
from django.utils import timezone
from .models import SensorData
from .tasks import send_sms_alert
from .serializers import SensorDataSerializer  # Import the serializer
from rest_framework.parsers import JSONParser  # This is necessary to parse JSON data
from django.views.decorators.csrf import csrf_exempt

# Thresholds
DOOR_OPEN_THRESHOLD = 10 * 60  # 10 minutes in seconds

@csrf_exempt
def update_sensor_data(request):
    if request.method == "POST":
        data = JSONParser().parse(request)  # Parse the incoming JSON data
        serializer = SensorDataSerializer(data=data)
        
        if serializer.is_valid():  # Check if the data is valid
            sensor_data = serializer.save()  # Save the validated data to the database

            # Check if the door has been open for too long
            if sensor_data.door_status == 1:  # Assuming 1 means the door is open
                last_open_time = sensor_data.timestamp
                time_door_open = (timezone.now() - last_open_time).total_seconds()
                
                if time_door_open >= DOOR_OPEN_THRESHOLD:
                    # Trigger SMS alert
                    send_sms_alert(sensor_data.temperature)
            
            return JsonResponse({"status": "success", "message": "Data received"}, status=201)
        return JsonResponse({"status": "error", "message": "Invalid data", "errors": serializer.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
