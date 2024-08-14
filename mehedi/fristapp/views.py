from django.shortcuts import render


# Create your views here.
def all_fristapp(request):
  return render(request,'fristapp/all_fristapp.html')

