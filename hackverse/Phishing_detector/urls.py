from . import views
from django.urls import path


app_name = 'Phishing_detector'
urlpatterns = [
    path('', views.get_index, name='get_index'),
    path('classify/',views.classify_URL, name='classify_URL'),
    ]
