from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import forms
from . import models

@login_required
def home(request):
    blogs = models.Blog.objects.filter(contributors=request.user)
    return render(request, 'blog/home.html', context={'blogs':blogs})

@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.save()
            blog.contributors.add(request.user, through_defaults={'contribution':'Auteur principal'})
            return redirect('home')
    context = {
        'blog_form': blog_form,
    }
    return render(request, 'blog/create_blog_post.html', context=context)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {'blog':blog})

@login_required
def edit_blog(request, blog_id):
    blog=get_object_or_404(models.Blog, id=blog_id)
    edit_form=forms.BlogForm(instance=blog)
    delete_form=forms.DeleteBlogForm()
    if request.method=='POST':
        if 'edit_blog' in request.POST:
            edit_form=forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect ('home')
        if 'delete_blog' in request.POST:
            delete_form=forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('home')
    context={
        'edit_form': edit_form,
        'delete_form':delete_form
    }
    return render (request, 'blog/edit_blog.html', context=context)

@login_required
def follow_users(request):
    form=forms.FollowUsersForm(instance=request.user)
    if request.method=='POST':
        form=forms.FollowUsersForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form':form})