from rest_framework import serializers
from monitoring.models import LogEntry


class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'


class MethodCountSerializer(serializers.Serializer):
    method = serializers.CharField()
    count = serializers.IntegerField()  