# python 켜지 않고 .py 바로 실행하기

#### 2019-01-14

- batch 파일을 만든다. (윈도우에서 .bat으로 보이는 파일들이다.)

- hello.py 파이썬 파일을 만든다.

  ```python
  # hello.py
  print("Hello!")
  ```


- hello.py를 실행할 hello.bat을 만든다.

  ```bash
  python C:\Users\student\scripts\hello.py %*
  pause
  ```



- 내 PC - 속성 - 고급 시스템 설정 - 환경 변수에서 hello.bat이 들어간 폴더를 추가해준다.
- 그러면 이제 window + R을 누른 실행에서 hello만 쳐도 자동으로 hello.py가 실행된다.



# 모듈

#### 2019-01-14

```python
# a.py
def cube(num):
    return num ** 3
def square(num):
    return num ** 2

if __name__ == "__main__":
    print(cube(2))
    print(square(2))
    
print(__name__)
```



```python
# b.py
from a import cube, square

print(cube(2))
print(square(2))
```



a.py에서 print(__name__)을 돌려보면 __main__이 나오지만, b.py에서 불러와서 돌려졌을 때는 a라는 파일 이름이 출력된다.



# OOP

#### 2019-01-14

세상을 요약하면 정말 작게 보면 주어와 동사로 나뉜다.

- 주어와 동사
- 주부와 술부
- subject & predicate
- object & method



Instance 는 하나의 분류체계 속의 예시같은 것이다. 전체 나무 분류 체계 중에서 하나의 구체적인 나무 예시인 것이다. Class는 나무 분류에 해당한다. Method는 행위, 동사 파트에 속한다.