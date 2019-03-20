data = '0000000111100000011000000111100110000110000111100111100111111001100111' #input()
#data2 = ['0000000', '1111000', '0001100', '0000111', '1001100', '0011000', '0111100', '1111001', '1111100', '1100111']
arr = data

"""
t  = 0
for j in range(len(data2)):
    arr = data2[j]
    for i in range(len(arr)):
        t = t*2 + int(arr[i])
        if (t+1)%7 == 0:
            print(t, end= ' ')
            t = 0
"""

"""
선생님 답
"""
t  = 0
for i in range(len(arr)):
    t = t*2 + int(arr[i])
    if (t+1)%7 == 0:
        print(t, end= ' ')
        t = 0
"""
내 답
"""
for start in range(0, len(data), 7):
    ans = 0
    for j in range(6, -1, -1):
        if data[start+j] == '1':
            ans += 2**(6-j)
    print(ans)

# 4bit 4bit.... 0 F일 때 F를 다 쓰라는 얘기가 아님!
data = '01D06079861D79F99F' # 입력
# 비트로 변환
arr = ''
for i in data:
    if ord(i) >= 65: # 알파벳이면
        arr += bin(ord(i)-ord('A')+10)[2:]
    else:
        arr += bin(ord(i)-ord('0'))[2:]
print(arr)

for start in range(0, len(arr), 7):
    ans = 0
    for j in range(6, -1, -1):
        if arr[start+j] == '1':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            ans += 2**(6-j)
    print(ans)

# 두 가지 접근 방법으로 접근해보았다.
# 1. 답이 맞다.

# 2. 범위를 확장해서 한다.
# python에 replace라는 메소드가 있다. 거꾸로 하면 안 된다. 2 다음에 1 하면 안 된다.
# 매핑테이블을 만들어넣고 한 글자씩 읽는다. 4배씩 늘어나니까 원래 길이의 4배한 것은 잡아둔다.

# for문 4번 돌면서 거기다가 쓰겠다.
# 아닛 이런 건 또 빨라....

