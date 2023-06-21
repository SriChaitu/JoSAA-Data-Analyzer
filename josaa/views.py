from django.shortcuts import render
from .models import programm
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Hello</h1>')

from django.http import HttpResponse
from django.template import loader

def home(request):
#   template = loader.get_template('first.html')
  return render(request,'index.html')

def start(request):
  return render(request,'start.html')

def rank_analyser(request):
  return render(request,'rank-anlyser.html')

def display(request):
  rankk = float(request.POST.get("rank"))
  yearr = float(request.POST.get("year"))
  rounddd = float(request.POST.get("roundd"))
  cate = str(request.POST.get("category"))
  gend = str(request.POST.get("gender"))
  context={
    'ps': programm.objects.all().order_by('open'),
    'rank1': rankk,
    'cate1': cate,
    'gend1': gend,
    'year1': yearr,
    'roundd1':rounddd
  }
  
  return render(request,'display.html',context)