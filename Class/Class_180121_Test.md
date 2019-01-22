# Python 문제

2019-01-21



1. 보기의 파이썬 코드를 실행하였을 때 틀린 것?

```python
import copy

list1 = [3, 'a', 'b']
list2 = [1, 2, list1]

list3 = list1[:]
list4 = copy.copy(list2) # 위랑 같은 것
list5 = copy.deepcopy(list2)
```

(1) list1 == list3의 결과는 True이다.

(2) list4[2][0] == 4라는 코드 입력 후 print(list2[2][0])의 출력값은 4이다.

(3) list4[2]라는 코드 입력 후, print(list2[2])의 출력값은 5이다.

(4) list5[2][1] = 3이라는 코드 입력 후, print(list2[2][1])의 결과값은 'a'이다.



2. 보기의 파이썬 코드를 실행하였을 때, 화면에 출력되는 결과를 작성하시오.

```python
a = 1
def my_func_1():
    a = 5
    my_func_2()
def my_func_2():
    print(a, end='')
my_func_1()
print(a)
```



