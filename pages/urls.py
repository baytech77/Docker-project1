from django.urls import path
from .views import TempView

urlpatterns = [
    path('',TempView.as_view(), name='landing' ),
    
]