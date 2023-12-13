from django.contrib import admin
from .models import LogEntry, StatusCodeList, LogController

from django.contrib import admin
from .models import LogEntry




class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'method', 'status', 'date_time']
    list_filter = ['method', 'status', 'date_time']

class LogControllerAdmin(admin.ModelAdmin):
    list_display = ['is_active']


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(LogController, LogControllerAdmin)
admin.site.register(StatusCodeList)