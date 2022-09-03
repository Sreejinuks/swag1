from Tools.scripts.pindent import start
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from sample.student import Student

from swagApp.form import StudentForm
from swagApp.models import Akshay, zara, login, college


def home(request):
    return HttpResponse("HELLO WORLD")
def darkk(request):
    return render(request,'login.html')
def kgf(request):
    z=Akshay.objects.all()
    return render(request,'appu.html',{'key':z})
def swagdef(request):
    data1=zara.objects.get(id=4)
    return render(request,'start.html',{'data2':data1})


def swagall(request):
    b= zara.objects.all()
    print(b)
    return render(request,'tokyo.html',{'wroom':b})

def drrr(request):
    xy=login.objects.get()
    return render(request,'login2.html')

def register(request):
    if request.method=='GET':
        return render(request,'insert.html')
    else:
      name  = request.POST.get('name')
      age  = request.POST.get('age')
      desi =request.POST.get('designation')
      sal = request.POST.get('salary')
      Student.objects.create(name=name,age=age,designation=desi,salary=sal)
      return render(request,'insert.html')
# for display......................
def emp(request):
    ob=Student.objects.all()
    return render(request,'insert.html',{'ob':ob})
def insert(request):
    if request.method=='GET':
        ob=StudentForm()
        return render(request,'new.html',{'ob':ob})
    else:
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('swagApp:emp')
def update(request,id):
    if request.method=="GET":
        ob=Student.objects.get(id=id)
        return render(request,'update.html',{'ob':ob})
    else:
      name  = request.POST.get('name')
      age  = request.POST.get('age')
      desi =request.POST.get('designation')
      sal = request.POST.get('salary')
      Student.objects.filter(id=id).update(name=name,age=age,designation=desi,salary=sal)
    return redirect('swagApp:emp')
def delete(request,id):
    Student.objects.get(id=id).delete()
    return redirect('swagApp:emp')


def display(request):
    object = college.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(object, 2)
    try:
        users = paginator.page(page)

    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'page.html', {'users': users})
