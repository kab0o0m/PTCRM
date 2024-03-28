from django.urls import path
from .views import ApplicationCreateAPIView

urlpatterns = [
    path('', ApplicationCreateAPIView.as_view(),
         name='create_application'),
    # Add more URL patterns as needed
]
