# Python 문제 풀기

#### 2019-01-11



##### Arara 셈

Arara는 셈을 한쌍으로 하는 아마존에 살고 있는 부족입니다. 이들이 행하는 셈의 방식은 다음과 같습니다.

예를 들어, 1에서 8까지는 셈을 한다면,

•1 = anane 

•2 = adak 

•3 = adak anane 

•4 = adak adak 

•5 = adak adak anane 

•6 = adak adak adak

•7 = adak adak adak anane

•8 = adak adak adak adak 

주어진 숫자 인수를 통해 다음과 같은 함수를 작성하세요.

예시

•count_arara(3) # -> 'adak anane'

•count_arara(8) # -> 'adak adak adak adak'

```python
# 내 코드
def count_arara(n):
    return 'adak ' * (n // 2) + 'anane' * (n % 2)
print(count_arara(3))
print(count_arara(8))
```



##### 알파벳만 남기고 뒤집기

문자열이 주어지면, 해당 문자열 중에서 알파벳이 아닌 문자는 전부 빼고 거꾸로 뒤집어 반환하는 함수를 작성하세요.

예시) 

reverse_letter("krishan")

"nahsirk"

reverse_letter("ultr53o?n")

"nortlu"

```python
# 내 코드
def reverse_letter(words):
    result = ""
    for letter in words:
        if letter.isalpha():
            result += letter
    return result[::-1]

# 선생님 코드
def reverse_letter2(s):
    a = [c for c in s if c.isalpha()]
    return "".join(a[::-1])
```



##### 숫자가 좋아

스트링과 함께 섞여있는 문자열들 속에서 정수만 뽑아내 합을 반환하는 함수 pick_and_sum를 작성하세요.

```python
# 내 코드
def pick_and_sum(words):
    numbers = ''.join([" " if x.isalpha() else x for x in words])
    return sum(map(int,numbers.split()))

# 선생님 코드
def pick_and_sum(s):
    for x in s:
        if not x.isdecimal():
            s = s.replace(x, ' ')
    return sum(map(int, s.split()))

# 선생님 코드 2
def pick_and_sum1(s):
    return sum(map(int, ''.join(c if c.isdigit() else ' ' for c in s).split()))


# 선생님 코드 3
import re
def pick_and_sum2(s):
    return sum(int(x) for x in re.findall(r'(\d+)',s)) # d = decimal로 된 모든 문자열을 찾아 준다.
print(pick_and_sum2("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))


# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")) #=> 3635
print(pick_and_sum1("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
print(pick_and_sum2("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```





# 올림피아드 RGB 문제

#### 2019-01-11

색이 칠해진 삼각형은 각각 빨강, 녹색 또는 파랑 색의 행에서 만들어집니다. 마지막 행보다 하나 적은 색을 각각 포함하는 연속 행은 이전 행에서 두 개의 색을 고려하여 생성됩니다. 이 색상이 동일하면 동일한 색상이 새 행에 사용됩니다. 색상이 다른 경우 누락 된 색상이 새 행에 사용됩니다. 단 하나의 색상으로 최종 행이 생성 될 때까지 계속됩니다.



''''

Colour here:        G G        B G        R G        B R

Becomes colour:    G           R           B            G

   

처리 과정 

R R G B R G B B

 R B R G B R B

  G G B R G G

   G R G B G

​    B B R R

​     B G R

​      R B

​       G

'''

```python
# 내 코드

def triangle2(colors):
    colors_dict = {'GG':'G', 'BB':'B', 'RR':'R', 'BG':'R', 'GB': 'R', 'RG':'B', 'GR': 'B', 'BR':'G', 'RB':'G'}
    if len(colors) == 2: return colors_dict[colors]
    return triangle2(''.join([colors_dict[colors[idx:idx+2]] for idx in range(len(colors)-1)]))



# 내 코드 한 줄 더 줄여보기
def triangle2(colors):
    if len(colors) == 1: return colors
    return triangle2(''.join([list({'R','G','B'} - {colors[idx], colors[idx+1]})[0] if colors[idx] != colors[idx+1] else colors[idx] for idx in range(len(colors)-1)]))

print(triangle2('RRR')) #=> R       
print(triangle2('RRGBRGBB')) #=> G
print(triangle2('RRRGGGBBBBBB')) #=> G
print(triangle2('RG')) #=> B



# 선생님 코드
def triangle(r):
    dictionary = {'GG':'G', 'BB':'B', 'RR':'R', 'BG':'R', 'GB': 'R', 'RG':'B', 'GR': 'B', 'BR':'G', 'RB':'G'}
    if len(r) > 2:
        s = ''
        for i in range(len(r)-1):
            s = s + dictionary[r[i:i+2]]
        r = s
        return triangle(r)
    elif len(r) > 1:
        return dictionray[r]
    else:
        return r

# 선생님 코드 2
color_set = set("RGB")
def triangle(r):
    while len(r) > 1:
        r = ''.join(a if a==b else (color_set - {a, b}).pop() for a, b in zip(r, r[1:]))
    return r

                   
# if문으로 모든 조건 다 처리 - 재귀 아님
# if문으로 처리하되, 딕셔너리 사용하지 않고, {R, G, B} - 지금 2개 값으로 차집합 이용 방법 - 재귀 아님
# 딕셔너리를 더 줄이고 sort된 애로 찾는 방법 - 재귀 가능
# R = ["RR", 'BG', 'GB'] 이런 식으로 리스트를 만들어서, 속하면 R에 해당한다 조건식을 작성 - 재귀 가능
```



