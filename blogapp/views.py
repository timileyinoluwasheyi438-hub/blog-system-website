from django.shortcuts import render, redirect
from .models import Blogpost

def homePageview(request):
    return render(request,'blogapp/index.html' )

def advertPage(request):
    return render(request,"blogapp/advert.html")

def contactPage(request):
    return render(request,"blogapp/contact.html")


def allPostView(request):
    all_post = Blogpost.objects.all()
    context ={
        "all_post": all_post
    }
    return render(request, 'blogapp/posts.html',context)

def createPostView(request):
    if request.method == 'POST':
        post_image=request.FILES['post-image']
        post_header = request.POST['post-header']
        post_body = request.POST['post-body']
        post_author = request.POST['post-author']

        new_post = Blogpost(blog_header=post_header,blog_body=post_body,author=post_author,post_image=post_image )
        new_post.save()
        return redirect("post")
    return render(request,'blogapp/creatposts.html')

def aboutPage(request):
    return render(request, 'blogapp/about.html')

def advertPage(request):
    return render(request,'blogapp/advert.html')


def updatePostView(request, pk):
    post_found = Blogpost.objects.get(pk=pk)
    if request.method =='POST':
        post_image=request.FILES.get['post-image']
        post_found.blog_header = request.POST['post-header']
        post_found.blog_body = request.POST['post-body']
        post_found.post_author = request.POST['post-author']
        
        post_found.save()
        return redirect('post')
    return render(request, 'blogapp/update.html', {'post': post_found})

def deletePostView(request, pk):
    post_found = Blogpost.objects.get(pk=pk)
    if post_found:
        post_found.delete()
    return redirect('post')


