from django.contrib import admin
from .models import LogEntry, StatusCodeList, LogController

admin.site.register(LogEntry)
admin.site.register(LogController)
admin.site.register(StatusCodeList)