from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Guitar
from .forms import MaintenanceForm

# Create your views here.
class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GuitarUpdate(UpdateView):
  model = Guitar
  
  fields = ['brand', 'model', 'description', 'year']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'

def home(request):
  return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    maintenance_form = MaintenanceForm()
    return render(request, 'guitars/detail.html', { 
        'guitar': guitar, 'maintenance_form': maintenance_form
    
    })