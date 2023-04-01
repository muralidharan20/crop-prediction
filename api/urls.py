from django.urls import path
from .views import crop_analyze,util_data

urlpatterns = [
    path('analyze/',crop_analyze),
    path('util/',util_data)
]