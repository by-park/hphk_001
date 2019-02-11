# Workshop 14 - Django

2019-02-11



1. 이름이 first_workshop인 프로젝트를 생성해주세요.

```bash
cd first_workshop/
pip install django
django-admin startproject first_workshop .
```



2. https://`<your-server-url>`/info의 경로로 들어갔을 때 다음과 같이 반 정보를 보여주는 페이지를 만들어 주세요.

_Terminal_

```bash
python manage.py startapp pages
```

_settings.py_

```python
ALLOWED_HOSTS = ["first-django-bypark.c9users.io"]
...
INSTALLED_APPS = [
    'pages.apps.PagesConfig'
]
```

_views.py_

```python
teacher = 'John'
students = {'홍길동': 29, '김길동':27, '박길동':28}

def info(request):
    return render(request, 'info.html', {'teacher':teacher, 'students':students})
```

_templates/info.html_

```html
<h1>우리반정보</h1>
<h2>Teacher</h2>
<ul>
    <li>{{ teacher }}</li>
</ul>

<h2>Student</h2>
<ul>
    {% for i in students %}
    <li>{{ i }}</li>
    {% endfor %}
</ul>
```

_urls.py_

```python
from pages import views

urlpatterns = [
    ...
    path('info/', views.info)
]

```

_Terminal_

```bash
python manage.py runserver $IP:$PORT
```



3. https://`<your-server-url>`/student/`<학생이름>`의 경로로 들어갔을 때 다음과 같이 학생의 이름과 나이를 보여주는 페이지를 만들어주세요.

_urls.py_

```python
from pages import views
...
urlpatterns = [
    path('admin/', admin.site.urls),
	...
    path('student/<str:name>/', views.student)
]
```

_views.py_

```python
teacher = 'John'
students = {'홍길동': 29, '김길동':27, '박길동':28}

def student(request, name):
    return render(request, 'student.html', {'name': name, 'age':students[name]})
```

_student.html_

```html
<h1>이름: {{ name }}</h1>
<h2>나이: {{ age }}</h2>
```

