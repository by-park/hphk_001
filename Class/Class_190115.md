# tkinter 사용법

#### 2019-01-15

_widget.py_

```python
# import tkinter 쓰면 아래에서 부를 때마다 tkinter. 쓰기 귀찮으니까!
from tkinter import *
# 버튼 누르면 brower 켜지게 할 거임
import webbrowser

# 이 함수를 button의 세 번째 인자로 넣어줄 수 있다.
def browser():
    webbrowser.open("https://www.daum.net")

# root라는 윈도우를 만들었다.
root = Tk()

# Label(어떤 tkinter 윈도우/프로그램에 넣을지, text = "")
# label = Label이라는 클래스를 이니셜라이즈!
label = Label(root, text = "Hello", fg="red", bg="blue")
label2 = Label(root, text = "John Kang's widget")

# 버튼 만들기 (라벨 만드는 과정과 비슷하다)
# command에 버튼 눌렸을 때 작동할 함수 이름을 그대로 써준다.
btn = Button(root, text="This is a button", command = browser)

# 좌표값 지정 (.pack()이라는 메소드, 가장 위에서부터 쌓아나가준다.)
label.pack()
label2.pack()
btn.pack()

# 사람들의 클릭이 있을 때, 그걸 계속 확인하고 실행해주는 조그만 위젯
root.mainloop()
```



# 클래스

#### 2019-01-15

- 클래스 - 인스턴스 간의 이름공간

```python
name = '?'
class Person:
    species = "인간"
    
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        print(f'{self.name}')
        print(f'{self.species}')
cr = Person('호날두')
cr.greeting()
```

class 안의 def면은 {name} 나 아니면 밖에 이렇게만 찾고, {self.name}이면 인스턴스 안에서 찾고 없으면 클래스까지 간다.



- 생성자 / 소멸자

```python
# 생성자에서 이름을 추가적으로 받아서 출력해봅시다.
class Person:
    def __init__(self, name):
        print("사람이 생성되었습니다.")
        self.name = name

    def __del__(self):
        print("사람이 죽었습니다.")

# 홍길동이라는 이름을 가진 hong 을 만들어봅시다.
hong = Person("홍길동")
del hong
```



- 클래스 변수 / 인스턴스 변수

클래스 변수는 모든 인스턴스가 공유하는 것이다.

인스턴스 변수는 인스턴스 별로 각각 가지는 변수이다.

```python
# 위의 생성자와 인사하는 메소드를 만들어봅시다. 
class Person:
    name = "john"            # 클래스 변수 : 모든 인스턴스가 공유함.
    population = 0
    
    def __init__(self, name = "no name"):   
        # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
        self.name = name 
        Person.population += 1
        print(f'인구가 증가하여 {Person.population}명이 되었습니다.')
        # print('생성될 때 자동으로 호출되는 메서드입니다.')
        
    def __del__(self):
        Person.population -= 1
        print(f'인구가 감소하여 {Person.population}명이 되었습니다.')
        # print('소멸될 때 자동으로 호출되는 메서드입니다.')
        
Person()
```



- 정적 메소드 / 클래스 메소드

인스턴스 메서드: 첫번째 인자로 인스턴스를 받는 메서드

정적 메서드: 인자로 아무것도 받지 않는 메서드 (데이터 조작을 하지 않은 메서드)

```python
class Dog:
    num_of_dogs = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs += 1
        
    def bark(self):
        print(f"멍멍, 저는 {self.name}, {self.age}살 입니다.")
   
    @staticmethod
    def info(): # self를 넣지 않은 메소드, 이름 공간의 하나의 메소드처럼 작용한다. -> static method
        print("강아지입니다.")
```

클래스 메서드: 첫번째 인자로 클래스를 받는 메서드

```python
class Dog:
    num_of_dogs = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs += 1
    def bark(self):
        print(f"멍멍, 저는 {self.name}, {self.age}살 입니다.")
    
    @classmethod
    def count(klass): # 이름이 꼭 cls일 필요는 없다. => 첫번째 인자로 클래스를 넣어준다. 이게 핵심.
        print(f"{klass.num_of_dogs}마리 생존중")
```



연산자 오버로딩 (중복 정의)

```python
class Person:
    def __init__(self, name, age, asset, height, gpa):
        self.name = name
        self.age = age
        self.asset = asset
        self.height = height
        self.gpa = gpa
    def __gt__(self, obj): #다른 객체가 들어올 것이다. object의 줄임말 obj로 넣었다.
        if self.age > obj.age:
            return True
        else:
            return False
    def __add__(self, obj):
        print("하트 뿅뿅")

minsu = Person('minsu', 28, 700000, 178, 4.2)
insung = Person('insung', 38, 70000000, 189, 1.8)

minsu > insung

# 이것은 실제로 다음과 동일하다.
insung.__gt__(minsu)
insung > minsu

insung.__add__(minsu)
insung + minsu
```



- 상속

메소드 오버라이딩

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id
    
    def greeting(self):
        print(f'안녕하세요, 저는 {self.name}입니다.')

p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')

p1.greeting()
s1.greeting()

```

