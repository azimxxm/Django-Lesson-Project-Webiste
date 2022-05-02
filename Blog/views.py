from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Post, Pricing
from .forms import PostForm, UserRegisterForm, CreatePostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'blog/form/login.html', context)


def Logout(request):
    logout(request)
    return redirect('login')


def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('login')
        else:
            messages.error(request, 'User not created because user already exists')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'blog/form/register.html', context)


@login_required(login_url='login')
def home(request):
    pricing = Pricing.objects.all()
    context = {
        'pricing': pricing,
    }
    return render(request, 'blog/home.html', context)


@login_required(login_url='login')
def view_posts(request):
    post = Post.objects.filter(is_published=True)
    context = {
        'post': post
    }
    return render(request, 'blog/view_posts.html', context)


@login_required(login_url='login')
def view_posts_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/view_post_detail.html', context)


@login_required(login_url='login')
def CreateNewPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully')
            return redirect('view-posts')
        else:
            messages.error(request, 'Post not created')
    else:
        form = CreatePostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/new_post_form.html', context)


@login_required(login_url='login')
def view_posts_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('view-posts-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'blog/view_post_form.html', context)


@login_required(login_url='login')
def view_posts_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('view-posts')


# search function
def Search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text:
            post = Post.objects.filter(Q(title__icontains=search_text) | Q(discrition__icontains=search_text))
            context = {
                'post': post
            }
            return render(request, 'blog/view_posts.html', context)
        else:
            messages.error(request, 'No search results found')
            return redirect('view-posts')
    else:
        return redirect('view-posts')
