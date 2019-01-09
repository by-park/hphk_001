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



