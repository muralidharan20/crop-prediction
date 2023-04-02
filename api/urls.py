from django.urls import path
from .views import *

urlpatterns = [
    path('analyze/',CropPredictionView.as_view()),
    path('util/',util_data)
]
