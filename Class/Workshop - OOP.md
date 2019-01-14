# Workshop 07

#### 2019-01-14

다음과 같은 클래스 Circle이 있다.

```python
class Circle:
	pi = 3.14
	x = 0
	y = 0
	r = 0
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
	def area(self):
		return self.pi * self.r * self.r
	def circumference(self):
		return 2 * self.pi * self.r
	def center(self):
		return (self.x, self.y)
	def move(self, x, y):
		self.x = x
		self.y = y
```



반지름이 3이고, x, y 좌표가 (2, 4)인 원을 만들어 넓이와 둘레를 출력하세요.



```python
>>> new_circle = Circle(2, 4, 3)
>>> print(new_circle.area())
28.259999999999998
>>> print(new_circle.circumference())
18.84
```

