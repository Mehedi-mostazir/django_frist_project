from django.shortcuts import render
from .models import appvaraity
from django.shortcuts import get_object_or_404


# Create your views here.
def all_fristapp(request):
  apps = appvaraity.objects.all()
  return render(request,'fristapp/all_fristapp.html', {'apps' : apps})

def app_detail(request, app_id):
  app = get_object_or_404(appvaraity, pk = app_id)
  return render(request, 'fristapp/app_detail.html', {'app': app})

