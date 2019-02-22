from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
# 모델로부터 객체를 받을 수 있다.


def home(request):
    blogs = Blog.objects
    # 객체들의 목록을 받을 수 있다. 이것을 쿼리셋이라고 한다. 이 쿼리셋을 사용하는 것을 .objects 이다.
    blog_list = Blog.objects.all()
    # 블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list, 3)
    # 블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page')
    # request 된 페이지가 뭔지를 알아내고 (request 페이즈를 변수에 담아내고)
    posts = paginator.get_page(page)
    # request 된 페이지를 얻어온 뒤 return 해 준다.
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드


def detail(request, blog_id):
    # blog_id 인자를 하나 더 받는다. path_converter
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # 어떤 클래스에서 받아올 건지?, pk값을 blog_id 값으로 가져온다.
    # 몇 번 객체를 받아 줄 건지? 없는 객체를 사용하면 404 에러를 띄운다.
    return render(request, 'detail.html', {'blog': blog_detail})


def new(request):  # new.html 띄워주는 함수
    return render(request, 'new.html')


def create(request):  # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    # blog title이라는 변수안에다가 가져온다. new html에 입력한 데이터를
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    # redirect 는 함수를 다 처리하고 지정해준 url 로 넘어간다.


def search(request):
    blog_all = Blog.objects.all()
    keyword = request.GET.get('search', '')
    if keyword:
        blog_all = blog_all.filter(title__icontains=keyword)
    return render(request, 'search.html', {'blog_all': blog_all, 'keyword': keyword})


def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})
