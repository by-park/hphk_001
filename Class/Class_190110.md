# 재귀 함수

#### 2019-01-10



팩토리얼 계산

```python
def factorial(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(factorial(5))
```



피보나치 수열

```python
def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2) # else: 로 넣어도 상관 없다. 

print(fib(10))
```



하노이의 탑

```python
# 내 코드
def hanoi(n):
    if n == 1:
        return 1
    return hanoi(n-1) + 1 + hanoi(n-1)
print(hanoi(4))

# 선생님 코드
def hanoi(n, start, tmp, end):
    if n:
        hanoi(n-1, start, end, tmp)
        print(f'{n}번째 원판을 {start}에서 {end}로')        
        hanoi(n-1, tmp, start, end)        
        
print(hanoi(3, 'a', 'b', 'c'))
```

