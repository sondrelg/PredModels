from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/templates/index.html')

def wrong_ticker(request):
    return render(request, 'frontend/templates/404.html')