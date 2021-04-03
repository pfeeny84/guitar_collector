from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Guitar, Strap
from .forms import MaintenanceForm

# Create your views here.
class GuitarCreate(CreateView):
    model = Guitar
    fields = ['brand', 'model', 'description', 'year']

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
    straps_guitar_doesnt_have = Strap.objects.exclude(id__in = guitar.straps.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'guitars/detail.html', { 
        'guitar': guitar, 'maintenance_form': maintenance_form,
        'straps': straps_guitar_doesnt_have
    
    })

def add_maintenance(request, guitar_id):
  # create a ModelForm instance using the data in request.POST
  form = MaintenanceForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_maintenance = form.save(commit=False)
    new_maintenance.guitar_id = guitar_id
    new_maintenance.save()
  return redirect('detail', guitar_id=guitar_id)

def assoc_strap(request, guitar_id, strap_id):
  Guitar.objects.get(id=guitar_id).straps.add(strap_id)
  return redirect('detail', guitar_id=guitar_id)

class StrapList(ListView):
  model = Strap

class StrapDetail(DetailView):
  model = Strap

class StrapCreate(CreateView):
  model = Strap
  fields = '__all__'

class StrapUpdate(UpdateView):
  model = Strap
  fields = '__all__'

class StrapDelete(DeleteView):
  model = Strap
  success_url = '/straps/'
