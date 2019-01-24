# Workshop Homework 1

#### 2019-01-07



1. Python에서 사용할 수 없는 식별자 (예약어)를 찾아 3개만 작성하세요.

> for, import, if, while



2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

   a = 0.1 * 3

   b = 0.3

> a - b < 1e-10



3. "안녕, 철수야"를 String Interpolation을 사용하여 출력하세요.

name = "철수"

> print(f'안녕, {name}야')



4. 다음 중 형변환시 오류가 발생하는 것은?

1)  str(1)

2) int('30')

3) int(5)

4) bool('50')

5) int('3.5')

> 5번만 오류가 발생한다.



5. 변경할 수 있는 (mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.

String, List, Tuple, Range, Set, Dictionary

> 이 중에 인덱스로 변경이 불가능한 것은 String, Tuple, Range이다.
>
> Dictionary는 key값을 통해 변경 가능하다. Set은 요소를 추가하거나 뺄 수 있다.

