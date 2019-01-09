# 파이썬 문제 풀기

#### 2019-01-09

- Generator object 이용 예시

_자연수 N의 각 자릿수의 합을 구해서 return하기

```python
def solution2(n):
    return sum([int(i) for i in str(n)])
print(solution2(1234))
```



_양의 정수 x가 하샤드 수인지 검사하기_

```python
def solution1(x):
    return x % sum(int(x) for x in str(x)) == 0
print(solution1(18))
```



```python
def solution2(n):
    return sum([int(i) for i in str(n)])

print(solution2(1234))
```

- 익명함수 lambda 사용 예시

_정수를 저장한 배열에서 가장 작은 수를 제거한 배열 return하기_

```python
def solution1(arr):
    return list(filter(lambda x: x > min(arr), arr))
print(solution1([4, 3, 2, 1]))
```



- 문자열을 join하는 함수

_각 문자를 한 번씩 반복하여 반환_

```python
def double_char2(word):
    return ''.join(s*2 for s in word)
print(double_char2('Python'))
```



- 소수점 포맷팅

_달러와 센트의 문자열 서식으로 return 하기_

```python
def format_money(amount):
    return f'{amount:.2f}'
print(format_money(5))

def format_money(amount):
    return '${:.2f}'.format(amount)
print(format_money(5))
```



- 숫자 계산시 사용하기 좋은 꼼수!

_주어진 연도 값에서 세기를 반환하는 함수_

```python
def Century_from_year(year):
    return (year + 99) // 100
print(Century_from_year(2019))


def Century_from_year(year):
    return (year - 1) // 100 + 1
print(Century_from_year(2019))
```

