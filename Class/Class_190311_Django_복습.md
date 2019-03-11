# Django 복습

2019-03-11



- pycharm pro 버전 설치. github에 student 인증을 받았으면 pro 버전을 설치할 수 있다.
- Django로 프로젝트를 생성하고, git init을 해준다.
- 프로젝트 내에 django-admini startapp board로 새로운 app을 생성한다.
- 오늘의 목표는 Django를 복습하기 위해 게시글과 댓글 CRUD를 구현할 것이다.



_first_loca/urls.py_

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
]
```



_frist_local/settings.py_

```python
INSTALLED_APPS = [
    'django_extensions', # 새로 추가한 부분
    'IPython',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board', # 새로 추가한 부분
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False # use timezone
```



_board/urls.py_

```python
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),  # list.html
    path('create/', views.create_article, name='create_article'),  # Create
    path('<int:article_id>/', views.article_detail, name='article_detail'),  # detail.html
    path('<int:article_id>/update/', views.update_article, name='update_article'),  # Update
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),  # Destroy
    path('<int:article_id>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:article_id>/delete_comment/<int:comment_id>',
         views.delete_comment,
         name="delete_comment"),
]
```



_board/models.py_

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(default='') # nullable을 따로 안 써주면 알아서 빈 건 안 넣어준다.
    content = models.TextField(default='')
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.title[:20]}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.article.title}: {self.content}'
```



_board/views.py_

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from IPython import embed

# Create your views here
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id) # 찾아 없어? 없는 걸 어떻게 찾아
    comments = article.comment_set.all()
    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
    })
#    article = Article.objects.get(id=article_id)

def new_article(request):
    # print(request.method)
    # embed()
    return render(request, 'board/new.html')

def create_article(request):
    if request.method == 'GET': # 사용자가 내놔했으면 주면 되고
        return render(request, 'board/new.html')
    elif request.method == 'POST': # 받아라 했으면 받아서 처리하면 된다.
        # print(request.method)
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        # embed()
        return redirect('board:article_detail', article.id)

def edit_article(request, article_id):
    pass

def update_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    if request.method == 'GET':
        return render(request, 'board/edit.html', {
            'article': article,
        })
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)

def delete_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
    return redirect('board:article_list')

def create_comment(request, article_id):
    article = get_object_or_404(Article, id = article_id) # 이걸 리팩토링하면 바로 73번 줄에 넣어주면 됨
    if request.method == 'POST':
        comment = Comment()
        #comment.article_id = article.id
        comment.article = article # ORM이 데이터베이스와 파이썬 세계의 접점을 해줘서 토스토스 하는 느낌. 의미론 적으로도 이 댓글의 글은 이 글이야가 와닿는다.
        comment.content = request.POST.get('comment')
        comment.save()
    return redirect('board:article_detail', article_id)

def delete_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, id = article_id)
    if request.method == "POST":
        comment = get_object_or_404(Comment, id = comment_id)
        comment.delete()
    return redirect('board:article_detail', article.id) # article_id 대신 한 번 더 검증해서 넣음
```



_board/admin.py_

```python
from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
```



_board/templates/board/base.html_

```html
<!doctype html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    {%  block body %}

    {%  endblock %}
</body>
</html>
```



_board/templates/board/list.html_

```python
{% extends 'board/base.html' %}

{% block body %}
<h1>New article</h1>

<form method="POST">                            <!--action="{% url 'board:create_article' %}" -->
    {% csrf_token %}
    <div>
        <label for="title">Title</label>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label  for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}

```



_board/templates/board/detail.html_

```python
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
    <a href="{% url 'board:article_list' %}"><button>목록으로 가기</button></a>
    <a href="{% url 'board:update_article' article.id %}"><button>수정하러 가기</button></a>
    <form action="{% url 'board:delete_article' article.id %}" method = "POST">
        {% csrf_token %}
        <button type="submit">삭제하러 가기</button>
    </form>
<hr>
{% include 'board/_comment.html' %}
{%  endblock %}
```



_board/templates/board/new.html_

```python
{% extends 'board/base.html' %}

{% block body %}
<h1>New article</h1>

<form method="POST">                            <!--action="{% url 'board:create_article' %}" -->
    {% csrf_token %}
    <div>
        <label for="title">Title</label>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label  for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}

```



_board/templates/board/edit.html_

```python
{% extends 'board/base.html' %}

{% block body %}
<h1>Edit article</h1>
<form method="POST">
    {% csrf_token %}
    <div>
        <label for="title">Title</label>
        <input type="text" name="title" id="title" value  = {{ article.title }}>
    </div>
    <div>
        <label  for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}

```



_board/templates/board/comment.html_

```python
<form action="{% url 'board:create_comment' article.id %}" method = "POST">
        {% csrf_token %}
        <label for="comment">comment</label>
        <input type="text" name="comment" id="comment">
</form>

{% if comments %}
    <ul>
    {% for comment in comments %}
        <li>{{ comment.content }}</li>
        <form
            action="{% url 'board:delete_comment' article_id=article.id comment_id=comment.id %}"
            method = "POST">
        {% csrf_token %}
        <button type="submit" onclick="return confirm('진짜 지움?');">DEL</button> <!--onsubmit도 가능-->
        </form>
    {% endfor %}
    </ul>
{% endif %}
```

