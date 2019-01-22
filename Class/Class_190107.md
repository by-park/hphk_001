# 파이썬 기초

#### 2019-01-07



##### <식별자>

변수명에는 작명룰이 있다. 

- 식별자의 이름은 영문알파벳, _, 숫자로 구성된다.

- 첫 글자에 숫자가 올 수 없다. 

- 대소문자를 구별한다

이 룰을 어기지 않았어도 아예 사용할 수 없는 "예약어"들이 있다.  다음과 같이 쳐보면 리스트를 확인할 수 있다.

> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

위 내용을 확인해보기 위해서는 다음의 코드를 작성하면 된다.

```python
import keyword
print(keyword.kwlist)
```



##### <코드라인>

print() 함수를 이어 쓰면 Syntax Error가 뜨는데 가운데 세미콜론 ; 을 넣어주면 가능하다.

```python
print("hello"); print("world")
```

혹은 다음과 같이 여러 줄을 출력할 수 있다.

```python
print('dfdfdf\ndd')
```



##### <변수 및 자료형>

-5 ~ 256 까지는 파이썬에 주소가 정해져있으나, 그 외의 숫자는 메모리에 매번 올려야한다.

```python
x = 100
print(x)
print(id(x))

x = 1004
print(x)
print(id(x))

y = 1004
print(id(y))
```

여러 값을 할당할 때 다음과 같이 할 수 있다.

```python
x = y = 1004

x, y = 1,2
x, y = (1,2)
x, y = [1,2]

print(x, y)
```

- 수치형 (int, float, complex)
- Bool
- 문자형 (string)



##### <이스케이프 문자열>

| 예약문자 | 내용(의미)      |
| -------- | --------------- |
| \n       | 줄바꿈          |
| \t       | 탭              |
| \r       | 캐리지리턴      |
| \0       | 널(Null)        |
| `\\`     | `\`             |
| '        | 단일인용부호(') |
| "        | 이중인용부호(") |



##### String interpolation

1) %-formatting

2) str.format()

3) f-strings : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.



##### 연산자

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| *      | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| **     | 거듭제곱       |



##### 조건문

조건문 예시

```python
a = 5
if a > 5:
    print('5 초과')
else:
    print('5 이하')
```

조건 표현식 예시 (if문을 한 줄로 작성하는 방법)

```python
num = int(input("숫자를 입력하세요 : "))
value = num if num >= 0 else 0
print(value)
```



##### 반복문

while문 예시

```python
a = 0
while a < 5: # a가 5보다 작은 동안
    print(a)
    a += 1
print('끝')
```



enumerate를 활용한 예시

```python
fruit = ['apple', 'orange', 'banana']
for idx, menu in enumerate(fruit):
    print(idx, menu)
```



for 와 else를 사용한 예시

```python
for num in numbers:
    if num == 5: # 3 또는 5를 넣고 테스트해보기
        print('True')
        break
else:
    print('False')
```

