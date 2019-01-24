# Workshop 06

#### 2019-01-09

양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요.

sqrt () 사용 금지

```python
def square_root(x):
    startn = 1
    endn = x
    for i in range(100):
        if x > ((endn + startn)/2)**2:
            startn = (endn + startn)/2
        else:
            endn = (endn + startn)/2
    return (startn + endn) / 2
```



#### 2019-01-10

선생님 코드 1

```python
def my_sqrt(n):
    x, y = 0, n
    answer = 0
    
    while abs(answer ** 2 - n) > 0.0001:
        answer = (x + y) / 2
        if answer ** 2 < n:
            x = answer
        else:
            y = answer
    return answer
```



선생님 코드 2

```python
def my_sqrt(n):
    minimum, maximum = 0, 1
    while 1:
        if n == maximum ** 2:
            return maximum
        elif minimum ** 2 < n < maximum ** 2:
            guess = (minimum + maximum) / 2
            
            if round(minimum, 5) == round(maximum, 5):
                return round(guess, 5)
            elif guess ** 2 > n:
                maximum = guess
            else:
                minimum = guess
        else:
            minimum += 1
            maximum += 1
```

