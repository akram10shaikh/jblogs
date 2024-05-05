from django.shortcuts import render
from blog.models import Category,Post
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    posts = Post.objects.all()
    cat = Category.objects.all()
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    servicedatafinal = paginator.get_page(page_number)
    return render(request,'index.html',{'posts':posts,'cat':cat,'page':servicedatafinal})

def posts_data(request,id):
    post = Post.objects.get(post_id=id)
    cat = Category.objects.all()
    return render(request,'posts.html',{'posts':post,'cat':cat})

def cat_data(request,id):
    cat = Category.objects.get(cat_id = id)
    post = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'post':post})



def header(request):
    cat = Category.objects.all()
    return render(request,'header.html',{'cat':cat})

def footer(request):
    cat = Category.objects.all()
    return render(request,'header.html',{'cat':cat})

def cats(request):
    cat = Category.objects.all()
    return render(request,'cat.html',{'cat':cat})

def about(request):
    return render(request,'about.html')

def login1(request):
    return render(request,'login.html')

def user_data(request):
    return render(request,'user_data.html')

def log_out(request):
    return render(request,'login.html')

def second_base(request):
    cats = Category.objects.all()
    return render(request,'second_base.html',{'cats':cats})

def login_user(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request,username=user,password=password)
        if user is not None:
            login(request,user)
            return render(request,'dashboard.html')
        else:
            msg = 'User or password is invalid '
            return render(request,'login.html',{'msg':msg})

def dashboard(request):
    return render(request,'dashboard.html')

def add_cat(request):
    if request.method == 'POST':
        cat = request.POST.get('cat')
        url = request.POST.get('url')
        description = request.POST.get('description')
        image = request.FILES['image']

        data = Category.objects.create(title=cat,description=description,url=url,image=image)
        data.save()
        msg = 'New category is added'
        return render(request,'dashboard.html',{'error':msg})

def add_post(request):
    if request.method == 'POST':
        post = request.POST.get('post_title')
        url = request.POST.get('url')
        content = request.POST.get('content')
        image = request.FILES['image']
        cat_list = request.POST.get('cat_list')

        cat = Category.objects.get(cat_id=cat_list)

        data = Post.objects.create(title=post,content=content,url=url,image=image,cat=cat)
        data.save()
        msg = 'New Post is added'
        return render(request,'dashboard.html',{'error':msg})


def delete_page(request):
    post = Post.objects.all()
    return render(request,'delete_page.html',{'post':post})

def edit(request,id):
    post = Post.objects.get(post_id=id)
    return render(request,'edit.html',{'p':post})

def delete_post(request,id):
    post = Post.objects.get(post_id=id)
    return render(request,'delete_post.html',{'p':post})

def edit_data(request):
    try:
        id = request.POST.get('post_id')
        title = request.POST.get('post_title')
        url = request.POST.get('url')
        content = request.POST.get('content')
        image = request.FILES['image']

        data = Post.objects.get(post_id=id)
        data.post_id = id
        data.title = title
        data.url = url
        data.content = content
        data.image = image
        data.save()

        msg = 'Post is edited successfully'
        return render(request, 'dashboard.html', {'error': msg})

    except Post.DoesNotExist:
        msg = 'Something went wrong'
        return render(request, 'edit.html', {'error': msg})


def delete_data(request,id):
    post = Post.objects.get(post_id=id)
    post.delete()
    msg = 'Post deleted successfully'
    return render(request, 'dashboard.html',{'error':msg})


def edit_cat(request):
    cat = Category.objects.all()
    return render(request,'edit_category.html',{'cat':cat})

def cat_edit(request,id):
    c = Category.objects.get(cat_id=id)
    return render(request, 'cat_edit.html', {'c': c})

def cat_data_edit(request):
    try:
        id = request.POST.get('cat_id')
        title = request.POST.get('cat_title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        image = request.FILES['image']

        data = Category.objects.get(cat_id=id)
        data.cat_id = id
        data.title = title
        data.url = url
        data.description = description
        data.image = image
        data.save()

        msg = 'Post is edited successfully'
        return render(request, 'dashboard.html', {'error': msg})

    except Post.DoesNotExist:
        msg = 'Something went wrong'
        return render(request, 'cat_edit.html', {'error': msg})

def delete_cat(request,id):
    c = Category.objects.get(cat_id=id)
    return render(request,'delete_cat.html',{'c':c})


def delete_cat_data(request,id):
    cat = Category.objects.get(cat_id=id)
    cat.delete()
    msg = 'Post deleted successfully'
    return render(request, 'dashboard.html',{'error':msg})

