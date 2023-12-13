from datetime import datetime, timedelta

from django.db.models import Count
from django.shortcuts import render
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from monitoring.models import LogEntry
from monitoring.pagination import CustomPagination
from monitoring.serializers import LogListSerializer, MethodCountSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, extend_schema_view
from drf_spectacular.types import OpenApiTypes


# Log endpoints
class LogListView(generics.ListAPIView):
    '''
    List log endpoint with filter
    path: /log/log-list?ordering=-user&search=404
    '''
    serializer_class = LogListSerializer
    queryset = LogEntry.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user', 'status', 'method']
    ordering_fields = ['user', 'status', 'method']
    pagination_class = CustomPagination


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(name='number', description='get number of month or day', type=str),
            OpenApiParameter(name='time', description='get monthly or daily', type=str),
        ]
    )
)
class DynamicLogListView(APIView):
    '''
    List of the number of methods dynamically by month or day for charts
    path example: /log/list-log-chart?time=-monthly&number=1
    output: get=50, post=10 . . .
    '''
    def get(self, request):
        # Get query parameters
        time_filter = request.query_params.get('time', None)
        number = request.query_params.get('number', 1)

        if time_filter == 'daily':
            time_ago = datetime.now() - timedelta(days=int(number))
        elif time_filter == 'monthly':
            time_ago = datetime.now() - timedelta(weeks=int(number) * 4)  
        else:
            return Response({'error': 'Invalid time parameter use this ?time=daily or monthly&number=integer'})

        # Query to get the count of each method in the specified time range
        method_counts = LogEntry.objects.filter(
            date_time__gte=time_ago
        ).values('method').annotate(count=Count('method'))

        # Serialize the data
        serializer = MethodCountSerializer(method_counts, many=True)

        return Response(serializer.data)


#
class InfoTestView(APIView):
    '''end point for test IMFO log level'''

    def get(self, request):
        return Response({'log level': 'INFO'}, status=200)
    

class WarningTestView(APIView):
    '''end point for test WARNING log level'''

    def get(self, request):
        return Response({'log level': 'WARNING'}, status=404)
    

class ErrorTestView(APIView):
    '''end point for test ERROR log level'''

    def get(self, request):
        return Response({'log level': 'ERROR'}, status=500)