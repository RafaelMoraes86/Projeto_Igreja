from django.shortcuts import render
from .models import Fiel

# Create your views here.
def lista_fieis(request):
    fieis = Fiel.objects.all()
    return render(request, 'lista_fieis.html', {'fieis': fieis})