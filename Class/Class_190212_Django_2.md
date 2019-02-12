# Django 2일차

2019-02-12



프로젝트 만드는 구조 다시 복습

1. 프로젝트 진행할 폴더 생성 (TEST)
2. 해당 폴더로 이동 (cd TEST)
3. 가상 환경 설정

   - pyenv virtualenv 3.6.7 <가상환경 이름>
   - pyenv local <가상환경 이름>
4. Django 설치

   - pip install django
5. Django 프로젝트 test 생성
   - django-admin startproject test .



프로젝트 만드는 방법 코드

```shell
> mkdir TEST
> cd TEST
> pyenv virtualenv 3.6.7 test-venv
> pyenv local test-venv
> pip install django
> django-admin startproject test .
```



## Model

Django의 테이블 생성

_models.py_

```python
from django.db import models

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
```



마이그레이션

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```



Django의 CRUD코드

shell에 먼저 접속

```shell
$ python manage.py shell
```

CRUD 코드 작성

```python
>> from articles.models import Article
>> article = Article(title="Happy", content="Hacking")
>> article.save()
>> articles = Article.objects.all()
>> articles[0].title
>> articles[0].content

>> a2 = Article.objects.get(pk=2)
>> a2.delete()

>> article = Article.objects.get(title="hey")
>> article.title = "dong"
>> article.save()

```

