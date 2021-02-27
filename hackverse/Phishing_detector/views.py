from django.shortcuts import render
from .feature_extraction import featureExtraction
from .predict import predict

# Create your views here.

def get_index(request):
    features = []
    features = featureExtraction('sieck-kuehlsysteme.de')
    predict(features)

    return render(request, 'index.html')
