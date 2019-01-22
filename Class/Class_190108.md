# Python 연습 문제

#### 2019-01-08

jupyter notebook을 활용한 연습 문제 풀이

- 달력 출력하기에 대한 코드

아래의 코드에서 사용된 print(f'{변수이름:2}')은 2 칸 안에 변수의 내용을 넣는다는 것이다. 기본적으로 오른쪽 정렬처럼 앞부분이 공백으로 채워진다. <2, >2, ^2 등을 사용하면 다른 정렬도 가능하다.

```python
calendar = {
1: 31, 2:28, 3: 31, 4: 30, 5:31, 6:30,
7: 31, 8:31, 9: 30, 10:31, 11:30, 12:31
}
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

for month, count_day in calendar.items():
    count = 0
    print(f'{month:10}', '월')
    
    for day in weeks:
        print(f'{day:2}', end=' ')
    print()

for i in range(1, count_day + 1):
    print(f'{i:2}', end = ' ')
    count += 1
    if count == 7:
        print()
        count = 0
print()
```



# 함수

#### 2019-01-08

- 코드가 복잡해질 수록 에러가 날 확률이 높다. 매번 붙여넣기 해서 사용하면 틀렸을 때, 붙여넣기 한 부분을 다 찾아서 수정해야 한다.
- `def 함수이름(함수 파라미터):` 로 시작하고 `return 반환할 값 이름` 으로 작성한다.

```python
def my_sum(a, b):
    return a + b

my_sum(3, 6)
```

- 함수의 인자를 지정하지 않아도 기본값을 설정할 수 있다.

```python
# 키워드 인자 예시
def greeting(age, name='ssafy'):
    print(f'{name}은 {age}살입니다.')

# 다양하게 함수를 호출해봅시다.
greeting(39, '태형')
greeting(name = '태형', age = 39) # 순서를 지키지 않고 쓸 수 있다.
greeting(39, name = '태형') # 하나만 써줘도 된다.
greeting(23)
greeting(age = 39, '태형') # 앞에는 맞게 하고 뒤에 이렇게 호출하면 오류가 난다.
```

- 가변 인자: `def func(*args):` 식으로 작성하면 임의의 개수의 인자를 받을 수 있다.

```python
def my_max(*args):
    result = 0
    for idx, value in enumerate(args):
        if idx == 0:
            result = value
        else:
            if result < value:
                result = value

# 만든 함수를 호출해보세요.
my_max(1, 2, 3, 4)
```

- 정의되지 않은 인자들 처리하기: `def func(**kwars):`를 하면 딕셔너리 형태로 받는다.

```python
def my_fake_dict(**kwargs):
    return(kwargs)

# 만든 함수를 호출해보세요.
my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
```

- 이름 공간 및 스코프: 파이썬에서 사용되는 이름들은 이름공간, namespace에 저장이 되어있고, LEGB Rule 을 가지고 있다.
  - Local scope: 정의된 함수
  - Enclosed scope: 상위 함수
  - Global scope: 함수 밖의 변수 혹은 import 된 모듈
  - Built-in scope: 파이썬 안에 내장되어있는 함수 또는 속성

