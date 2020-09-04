from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
# Create your views here.

#List All the records of db  table.
def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list':post
    }
    return render(request,"blog/blog_list.html",context)

#Details of sepcific record.
def blog_detail(request,id):
    each_post = Post.objects.get(id = id)
    context = {'blog_detail' : each_post}
    return render(request,"blog/blog_detail.html",context)

#Delete specific record.
def blog_delete(request,id):
    each_post = Post.objects.get(id = id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')

    

