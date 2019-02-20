# Workshop 19 - Python 활용 SQL

2019-02-19



자신의 반에 있는 사람들의 데이터를 저장하는 Student 모델을 생성합니다.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField()
    email = models.CharField()
    birthday = models.dateField()
    age = models.IntegerField()
```



17 workshop에서 만든 모델을 활용해서 학생들의 정보를 저장하는 CRUD 페이지를 구현하세요

_urls.py_

```python
from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:articlenum>', views.show, name='detail'),
    path('<int:articlenum>/edit/', views.edit),
    path('<int:articlenum>/update/', views.update),
    path('<int:articlenum>/delete/', views.delete),
]
```



_view.py_

```python
from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students':students})

def new(request):
    return render(request, 'new.html')

def create(request):
    student = Student(name=request.GET.get("name"), email=request.GET.get('email'), birthday=request.GET.get('birthday'), age=request.GET.get('age'))
    student.save()
    return redirect('/')

def show(request, student_id):
    return render(request, 'show.html', {'student':Student.objects.get(id=student_id)})
    
def edit(request, student_id):
    return render(request, 'edit.html', {'student':Student.objects.get(id=student_id)})

def update(request, student_id):
    student = Student.objects.get(id=student_id)
    student.name=request.GET.get("name")
    student.email=request.GET.get("email")
    student.birthday=request.GET.get("birthday")
    student.age=request.GET.get("age")
    student.save()
    return redirect(f'/{student_id}/')
    
def delete(request, student_id):
    Article.objects.get(id=student_id).delete()
    return redirect('/')
```



_index.html_

```html
<h1>게시판입니다.</h1>
<a href="/new/">새 글 쓰기</a>
<table>
    {% for i in students %}
    <tr>
        <td><a href="/{{i.id}}">{{ i.title }}</a> <a href="/{{i.id}}/edit">수정</a> <a href="/{{i.id}}/delete">삭제</a></td>
    </tr>
    {% endfor %}
</table>
```



_new.html_

```html
<h1>새 게시물 쓰기</h1>
<form action="/create/">
    이름: <input type="text" name="name"/>
    이메일: <input type="text" name="email"/>
    생일: <input type="date" name="birthday"/>
    나이: <input type="number" name="age"/>
    <input type="submit" value="Submit"/>
</form>
```



_show.html_

```html
<h1>글 상세보기</h1>
제목: {{ student.title}}
내용: {{ student.content }}

<a href="/">메인 페이지로</a>
```



_edit.html_

```html
<h1>게시물 수정</h1>
<form action="/{{article.id}}/update/">
    이름: <input type="text" name="name" value="{{article.name}}"/>
    이메일: <input type="text" name="email" value="{{article.email}}"/>
    생일: <input type="date" name="birthday" value="{{article.birthday}}"/>
    나이: <input type="number" name="age" value="{{article.age}}"/>
    <input type="submit" value="Submit"/>
</form>
```

