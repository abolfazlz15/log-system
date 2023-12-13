from django.urls import path
from . import views

urlpatterns = [
    path('log/log-list', views.LogListView.as_view(), name='log_list'),
    path('log/list-log-chart', views.DynamicLogListView.as_view(), name='list_log_char'),


    path('test/info', views.InfoTestView.as_view(), name='info'),
    path('test/warning', views.WarningTestView.as_view(), name='warning'),
    path('test/error', views.ErrorTestView.as_view(), name='error'),

]