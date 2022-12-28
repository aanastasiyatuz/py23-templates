from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'home.html')

def posts_list(request):
    queryset = Post.objects.all()
    return render(request, 'list.html', {"posts":queryset})

def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'create.html', {"form":form})
    elif request.method == 'POST':
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('list'))
    return redirect(reverse_lazy('list'))