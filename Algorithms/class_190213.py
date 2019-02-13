# stack 구현하기

# input
#s = input()
s = '()()((()))'
#s = '((()((((()((()()))((())))))'

# stack 만들기
stack = [-1]*len(s)
top = 0

# 괄호
bracket_l = ['(', '{', '[']
bracket_r = [')', '}', ']']

ans = True
# stack 이용
for i in s:
    # 괄호 종류 하나씩 검사
    for b in range(3):
        # 여는 괄호를 만나면 스택에 넣음
        if i == bracket_l[b]:
            stack[top] = b
            top += 1
        elif i == bracket_r[b]:
            # 스택에 정상적으로 만난 경우
            if stack[top-1] == b:
                stack[top-1] = -1 # 그 칸은 초기화
                top -= 1
            # 여는 괄호가 맞지 않는 오류 찾기
            else:
                ans = False

if top != 0:
    ans = False
print(ans)