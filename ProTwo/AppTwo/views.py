from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import FormName
# Create your views here.

def index(request):
    return HttpResponse("<h1> Thank You !! </h1>")

def form_name_view(request):
    form = FormName()
    if request.method=='POST':
        form = FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'AppTwo/AppTwo.html',{'form':form})
