from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def models(request):
    return render(request, 'models.html')

def treemap(request):
    return render(request, 'treemap.html')

def chart(request):
    return render(request, 'chart.html')