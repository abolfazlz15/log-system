from rest_framework import serializers
from monitoring.models import LogEntry


class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'