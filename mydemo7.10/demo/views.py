from django.db.models import Avg, Max, Min
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from demo.Modules.module1 import M1
# from demo.Modules.module2 import M2
from demo.Modules.module4 import M4
from demo.Modules.module5 import M5
from demo.Modules.module7 import M7
from datetime import datetime


# Create your views here.

def index(request):

    time_list=[]
    #
    # M1.reset_data()
    # cap_list=M1.historical_backtest()


    time1=M7.calculate_time1()
    time2= M7.calculate_time2()

    time_list.append(time1)
    time_list.append(time2)





    return render(request, 'demo/index.html',{'time_list':time_list})

