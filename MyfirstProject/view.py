from datetime import datetime
from django.shortcuts import render
def index(request):
    date=datetime.today()
    context={"thedate":date}
    return render(request,'myfirstproject/index.html',context)
    