from django.db import models

# models.py
from django.db import models

class LogEntry(models.Model):
    status = models.IntegerField(null=True)
    user = models.CharField(max_length=255, null=True)
    date_time = models.DateTimeField(null=True)
    method = models.CharField(max_length=10, null=True)
    module = models.CharField(max_length=255, null=True)
    table = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.date_time} - {self.user} - {self.method} - {self.status}"
