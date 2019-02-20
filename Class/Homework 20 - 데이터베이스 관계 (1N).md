# Homework 20 - 데이터베이스 관계 (1:N)

2019-02-19



1. Class 모델과 Student 모델을 1:N 관계로 설정하려고 한다. models.py에 넣어야하는 코드를 작성하세요. (1:N의 관계중 N의 클래스를 작성해주세요.)

```python
class Student(models.Model):
    name = models.CharField()
    email = models.CharField()
    birthday = models.dateField()
    age = models.IntegerField()
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="classes")
```



2. Question 모델과 Comment 모델은 1:N 관계를 가지고 있다.

   A = Question.objects.get(id=id)

   위의 코드가 있을 때 views.py에서 Comment를 모두 가져오기 위한 코드를 작성하세요. (related_name은 설정하지 않았다고 가정한다.)

   ```shell
   A.comment_set.all()
   ```



3. 기본적으로 1:N 관계를 설정을 할 때 ForeignKey를 이용해서 1에 해당하는 클래스를 지정해준다. 지정한 클래스가 Movie일 때 ForeignKey로 지정된 컬럼의 이름은 무엇인가?

> movie_id