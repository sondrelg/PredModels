from django.shortcuts import render

def api_docs(request):
    return render(request, 'api_docs.html')