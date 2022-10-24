from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tea

# Define the home view
def home(request):
  return HttpResponse('<h1>okUUURRR</h1>')

def about(request):
    return render(request, 'about.html')


# Add new view
def tea_index(request):
  tea = Tea.objects.all()
  return render(request, 'tea/index.html', { 'tea': tea })

def tea_detail(request, tea_id):
  tea = Tea.objects.all(id=tea_id)
  return render(request, 'tea/detail.html', { 'tea': tea })


class TeaCreate(CreateView):
  model = Tea
  fields = ['title','type','description','witnesses']
  success_url = '/tea/'


class TeaUpdate(UpdateView):
  model = Tea
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type', 'description', 'witnesses']

class TeaDelete(DeleteView):
  model = Tea
  success_url = '/tea/'
