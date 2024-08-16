# urls.py

from django.urls import path
from .views import update_sensor_data  # Import the view you created

urlpatterns = [
    path('api/update_sensor_data/', update_sensor_data, name='update_sensor_data'),
]
