from django.db import models

class CalendarBox(models.Model):
    date = models.DateField()
    message = models.TextField()
    image = models.ImageField(upload_to='advent_images/')
    is_opened = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Casella del {self.date}"