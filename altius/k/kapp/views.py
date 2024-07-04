from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})


def delete(request,id1):
    blog=Blog.objects.get(id=id1)
    blog.delete()
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})


def add(request):
    if request.method=="POST":
        tit1=request.POST.get('tit2',False)
        con1=request.POST.get("con2",False)
        if tit1!="":
            
            blog=Blog.objects.create(title=tit1,body=con1)
            blog.save()
        return HttpResponse("<h1>/thanks/</h1>")
    else:
       
        return render(request,'add.html')