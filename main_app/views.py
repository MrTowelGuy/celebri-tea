from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>okUUURRR</h1>')

def about(request):
    return HttpResponse('<h1>spill some tea</h1>')