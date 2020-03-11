from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def form(request):
    return render(request,'form.html',context=None)

def new_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content= request.POST['content']
        published_on = timezone.now()
        Post.objects.create(title=title,content=content,published_on=published_on).save()
        return redirect('/')
    return redirect('/')