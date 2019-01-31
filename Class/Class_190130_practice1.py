"""
패턴 매칭

고지식한 방법을 이용하여 패턴을 찾아 봅시다.
임의의 본문 문자열과 찾을 패턴 문자열을 만듭니다.
결과 값으로 찾은 위치값을 결과로 출력합니다.
"""

# 임의의 본문 문자열
s = 'This is a sample sentence'
p = 'sample'

# 고지식한 방법
i = j = 0
N = len(s)
M = len(p)

while j < M and i < N:
    if s[i] != p[j]:
        i = i-j
        j = -1
    i += 1
    j += 1

# 인덱스값 출력
if j == M:
    print(i-j)
else:
    print(-1)


# 선생님 코드
def BruteFore(t,p):
    i=j=0
    N = len(t)
    M = len(p)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j #j는 맨 앞으로 # i는 중간에 멈춤
            j = -1
        i += 1
        j += 1
    if j == M: return i-M
    else: return i # 못찾았다 대신 본문의 길이 리턴

T = "abdvdfdfd"
P ="dddd"
print(T[BrueteForce(T,P):])