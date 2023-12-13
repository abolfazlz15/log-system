from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from monitoring.models import LogEntry
from rest_framework import filters

from monitoring.serializers import LogListSerializer


class LogListView(generics.ListAPIView):
    serializer_class = LogListSerializer
    queryset = LogEntry.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user', 'status', 'method']
    ordering_fields = ['user', 'status', 'method']



class TestView(APIView):
    def get(self, request):
        return Response({'message': 'test'})