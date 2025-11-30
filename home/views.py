from django.shortcuts import render,redirect
from home.models import Article,Author
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/login/')
def index(req):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(req,'index.html',context)

@login_required(login_url='/admin/login/')
def detail(request,slug):
    article = Article.objects.get(slug = slug)
    context = {
        'article':article
    }
    return render(request,'detail.html',context)

@login_required(login_url='/admin/login/')
def create(request):
    if request.method=="POST":
        title = request.POST.get('title','default title')
        content = request.POST.get('content')
        email = request.POST.get('email')
        author = Author.objects.get(id = request.POST.get('author'))
        editor = Author.objects.get(id = request.POST.get('editor'))
        Article.objects.create(
            title = title,
            content = content,
            author_email = email,
            author = author,
            editor = editor,
        )

        return redirect('home')

    authors = Author.objects.all()
    context = {
        'authors':authors
    }
    return render(request,'create.html',context)

@login_required(login_url='/admin/login/')
def update(request,id):
    article = Article.objects.get(id=id)
    if request.method=="POST":
        article.title = request.POST.get('title','default title')
        article.content = request.POST.get('content')
        article.author_email = request.POST.get('email')
        article.author = Author.objects.get(id = request.POST.get('author'))
        article.editor = Author.objects.get(id = request.POST.get('editor'))
        article.save()
        return redirect('home')

    authors = Author.objects.all()
    context = {
        'authors':authors,
        'article':article
    }
    return render(request,'create.html',context)

def delete(request,id):
    if request.method == "POST":
        Article.objects.get(id = id).delete()
    return redirect('home')

