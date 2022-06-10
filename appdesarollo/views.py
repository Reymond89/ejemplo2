from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def Index(request):

    return render (request, 'inicio.html')



def Pagina(request):

    return render(request, 'pagina.html')

