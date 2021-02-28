from django.shortcuts import render
from .feature_extraction import featureExtraction
from .predict import predict
from .getFeatures import generate_data_set

# Create your views here.

def get_index(request):
    print('hello')
    return render(request, 'index.html')

def classify_URL(request):
    url = request.POST["url"]
    features = []
    features = generate_data_set(url)
    print(features)
    ans = predict(features)

    return render(request, 'index.html', {'ans': ans, 'flag': 1, 'url' : url})
