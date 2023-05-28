from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def show_editor(request):
    return render(request, 'index.html')
