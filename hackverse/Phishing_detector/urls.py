from . import views
from django.urls import path


app_name = 'Phishing_detector'
urlpatterns = [
    path('', views.get_index, name='index'),
    ]
