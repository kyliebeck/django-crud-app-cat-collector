from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='home')
    
]
