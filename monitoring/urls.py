from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('log/log-list', views.LogListView.as_view(), name='log_list'),
    path('log/list-log-chart', views.DynamicLogListView.as_view(), name='list_log_char'),
]