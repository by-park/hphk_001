# Workshop 17 - Django

2019-02-12



자신의 반에 있는 사람들의 데이터를 저장하는 Student 모델을 생성합니다. Student 모델이 가져야할 필드는 다음과 같습니다.



name(이름): CharField

email(이메일): CharField

birthday(생년월일): dateField

age(나이): IntegerField



```python
from django.db import models

class Student(models.Model):
    name = models.CharField()
    email = models.CharField()
    birthday = models.dateField()
    age = models.IntegerField()
```



모델 마이그레이션 작업을 거친 후

Admin 페이지에서 주변 학생들의 이름을 세명 저장합니다.

```shell
python manage.py makemigrations
python manage.py migrate

python manage.py runserver $IP:$PORT
```

_admin.py_

```python
admin.site.register(Student)
```



저장 후 Admin 페이지에서 학생들의 목록을 보기 쉽게 만들기 위해서 `__str__`메소드를 오버라이드하여 name이 출력되게 만듭니다.

_models.py_

```python
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
```

_admin.py_

```python
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)
        
admin.site.register(Student, StudentAdmin)
```



참고: https://docs.djangoproject.com/ko/2.1/releases/1.0-porting-guide/