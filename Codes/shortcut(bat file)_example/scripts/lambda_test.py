# my_map 쓸거라서 print() 문은 주석처리해줘야한다.
import hof

# lambda랑 완전히 똑같은 예시 - def 사용
def add_two(num):
    return num + 2

# 2를 더하는 것이라 6이 나오고, 리스트의 모든 값에 2가 더해진다.
print(add_two(4))
print(hof.my_map(add_two, [1, 2, 3, 4]))

# 특정 함수를 넘겨줄 때 매번 정의하기가 귀찮다.
# 람다를 쓰면 다음 같이 입력, 출력으로 핵간단하게 만들 수 있다.
# print(hof.my_map(lambda 입력: 출력, [1, 2, 3, 4]))
print(hof.my_map(lambda num: num + 2, [1, 2, 3, 4]))

# 람다 함수를 집어넣을 수도 있다.
# ★코드 가독성을 흐리므로, 한 줄로 끝나지 않으면 람다 쓰지 마세요! - 파이썬 공식 추천
add_two = lambda num: num + 2
print(hof.my_map(add_two), [1, 2, 3, 4]))

# 연습
# 1. square 라는 변수에 lambda를 통해 제곱하는 함수를 할당
# 2. cube라는 변수에 세제곱
# 3. sqrt 변수에 제곱근 (math 활용)
square = lambda x: x ** 2
cube = lambda x: x ** 3
import math
sqrt = lambda x: math.sqrt(x)

print(hof.my_map(sqrt, [1, 2, 3, 4]))