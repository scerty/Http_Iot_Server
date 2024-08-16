# models.py

from django.db import models

class SensorData(models.Model):
    door_status = models.IntegerField()  # 0 for closed, 1 for open
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Door: {'Open' if self.door_status else 'Closed'}, Temp: {self.temperature}°C"
