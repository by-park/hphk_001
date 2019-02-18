# Django 데이터베이스 & CRUD 응용

2019-02-18



### 전생 앱 만들기

cloud9에 BONBON이라는 폴더를 만든다. 그리고 startapp이라는 앱을 만든다.

```shell
cd BONBON/
pyenv virtualenv 3.6.7 bonbon-venv
pyenv local bonbon-venv
pip install django
django-admin startproject bonbon .

python manage.py startapp pastlife
```

앱을 생성한 후에는 settings.py에 필요한 내용들을 적어준다.

```python
ALLOWED_HOSTS = ['first-django-bypark.c9users.io']
INSTALLED_APPS = [
    ...
    'pastlife'
]
```

urls.py에 필요한 url 주소들을 설정해준다.

```python
from pastlife import views

urlpatterns = [
    ...
    path('', views.index),
    path('pastlife/', views.pastlife)
]
```

fake 정보를 위해 faker를 설치한다.

```shell
pip install faker
```

views.py에 다음과 같이 작성하고,

```python
from faker import Faker

def index(request):
    return render(request, 'index.html')

def pastlife(request):
    name = request.GET.get('name')
    fake = Faker('ko_KR')
    job = fake.job()
    
    context = {
        'name': name,
        'job': job
    }
    
    return render(request, 'pl.html', context)
```

index.html과 pl.html을 작성한다.

_index.html_

```html
<h1>전생앱!!</h1>
<p>전생을 알려드립니다.</p>
<form action="/pastlife">
    <input type="text" name="name"/>
    <input type="submit" value="submit"/>
</form>
```

_pl.html_

```html
<h1>
    {{name}}님의 전생은 {{job}}이었습니다.
</h1>
```



### 전생 앱 만들기 - DB활용

_models.py_

```python
class Job(models.Model):
    name = models.TextField()
    job = models.TextField()
```

python manage.py makemigrations와 python manage.py migrate 명령어를 shell에 입력해준다.

그리고 모델이 생성되면 views.py를 다음과 같이 작성한다.

```python
from .models import Job
from faker import Faker

...

def pastlife(request):
    name = request.GET.get('name')
    person = Job.objects.filter(name=name).first()
    
    if person:
        job = person.job
    else:
        fake = Faker('ko_KR')
        job = fake.job()
        j = Job(name=name, job=job)
        j.save()
        
        context = {
            'name': name,
            'job': job
        }
        
    return render(request, 'pl.html', context)
```



