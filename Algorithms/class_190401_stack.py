# stack
# 3개의 데이터를 스택에 넣고
# 3번 꺼내서 출력

# 파이썬 리스트 사용
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop(-1))
print(stack.pop(-1))
print(stack.pop(-1))

# 고정 길이 배열 사용
top = -1
stack = [0] * 3
for i in range(3):
    top += 1
    stack[top] = i+1

for i in range(3):
    print(stack[top])
    top -=1
