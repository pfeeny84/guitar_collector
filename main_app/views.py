from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Guitar:
    def __init__(self, brand, model, description, year):
        self.brand = brand
        self.model = model
        self.description = description
        self.year = year

guitars = [
    Guitar('Gibson', 'Les Paul Custom', 'Super sick guitar', 1956),
    Guitar('Fender', 'Telecaster', 'Twaaaaaaang', 1975),

]

def home(request):
  return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', { 'guitars': guitars })