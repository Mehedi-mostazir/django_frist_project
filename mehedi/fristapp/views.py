from django.shortcuts import render
from .models import appvaraity


# Create your views here.
def all_fristapp(request):
  apps = appvaraity.objects.all()
  return render(request,'fristapp/all_fristapp.html')

