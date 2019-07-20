from django.db.models import Avg, Max, Min
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from demo.Modules.module1 import M1
# from demo.Modules.module2 import M2
from demo.Modules.module4 import M4
from demo.Modules.module5 import M5
from datetime import datetime


# Create your views here.

def index(request):

    M1.reset_data()
    cap_list=M1.historical_backtest()

    return render(request, 'demo/index.html',{'cap_list':cap_list})

def index2(request):
    M1.reset_data()
    M1.historical_backtest()
    historical_ratios=models.HISTORICAL_RATIO.objects.all()
    return render(request, 'demo/index2.html',{'historical_ratios':historical_ratios})