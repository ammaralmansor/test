from django.shortcuts import render

from .forms import LoginForm,SubjectForm,StudentForm
from .models import Laptop, Login

# Create your views here.


# def index(request):
#    return render(request, 'pages/index.html',{'pro':Laptop.objects.all()})

def index(request):
    if request.method == 'POST':
        sdata = StudentForm(request.POST)
        subdata = SubjectForm(request.POST)
        print(sdata)
        if sdata.is_valid() and subdata.is_valid():
            sdata.save()
            subdata.save()


    return render(request, 'pages/index.html',{'sf':StudentForm,'sub':SubjectForm})
