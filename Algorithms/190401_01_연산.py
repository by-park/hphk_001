"""
연산

2019.04.01 PBY 최초작성
"""
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    if M*2 >= M+10:
        maxlen = M*2
    else:
        maxlen = M+10
    memo = [0] * (maxlen)
    # memo를 돌면서 계산한 값을 넣기
    for num in range(N, maxlen+1):
        #print(memo)
        if num + 1 <= maxlen: # 자연수 + 1
            if memo[num] == 0:
                memo[num] = memo[num-1]+1 # 최소로 오면 여기
            else:
                memo[num] = min(memo[num], memo[num-1]+1)
        if num -2 > 0: # index 에러가 나지 않게, 내 인덱스는 0부터 시작함
            if memo[num-2] == 0:
                memo[num-2] = memo[num-1]+1
            else:
                memo[num-2] = min(memo[num-2], memo[num-1]+1)
        if num*2 <= maxlen:
            if memo[num*2-1] == 0:
                memo[num*2-1] = memo[num-1]+1
            else: 
                memo[num*2-1] = min(memo[num*2-1], memo[num-1]+1)
        if num - 11 > 0:
            if memo[num-11] == 0:
                memo[num-11] = memo[num-1]+1
            else:
                memo[num-11] = min(memo[num-11], memo[num-1]+1)
                
    #print(memo)
    print("#%d %d" %(tc, memo[M-1]))

"""
from collections import deque
T = int(input())
q = deque()
for tc in range(1, T+1):
    N, M = map(int, input().split())
     # q에는 연산 값과 몇 번째 연산인지 저장
    q.append([N+1,1])
    q.append([N-1, 1])
    q.append([N*2, 1])
    q.append([N-10, 1])
    for i in range(4):
        if q[i][0] == M:
            ans = 1
            q = deque()
            break
        
    while q:
        temp = q.popleft()
        q.append([temp[0]+1, temp[1]+1]
        if temp[0] == M:
            ans = temp[1]
            break
        if temp[0]-1 > 0:
            q.append([temp[0]-1, temp[1]+1])
            if temp[0] == M:
                ans = temp[1]
                break
        q.append(temp[0]*2, temp[1]+1)
        if temp[0] == M:
            ans = temp[1]
            break
        if q[front][0]-10 > 0:
            rear += 1; q[rear] = [q[front][0]-10, q[front][1]+1]
            if q[rear][0] == M:
                front = rear
                break
    
    print("#%d %d" %(tc, ans))
"""    
# 2를 곱해서 몇 번 하면 1,000,000이 나오는가?
"""
T = int(input())
q = [[0, 0] for _ in range(2**20)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
     # q에는 연산 값과 몇 번째 연산인지 저장
    front = rear = -1
    cnt = 0
    if 1000000 >= N+1:
        rear += 1; q[rear] = [N+1,1]
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    
    if N-1 > 0:
        rear += 1; q[rear] = [N-1, 1]
        cnt += 1 
        if q[rear][0] == M:
            front = rear
            break
    if 1000000 >= N*2:
        rear += 1; q[rear] = [N*2, 1]
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    if N-10 > 0:
        rear += 1; q[rear] = [N-10, 1]
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    for i in range(cnt):
        if q[i][0] == M:
            front = rear = i
            break
        
    while front != rear:

        front += 1
        if 1000000 >= q[front][0] + 1:
            rear += 1; q[rear] = [q[front][0]+1, q[front][1]+1]
            if q[rear][0] == M:
                front = rear
                break
        if  q[front][0]-1 > 0:
            rear += 1; q[rear] = [q[front][0]-1, q[front][1]+1]
            if q[rear][0] == M:
                front = rear
                break
        if q[front][0]*2 <= 1000000:
            rear += 1; q[rear] = [q[front][0]*2, q[front][1]+1]
            if q[rear][0] == M:
                front = rear
                break
        if q[front][0]-10 > 0:
            rear += 1; q[rear] = [q[front][0]-10, q[front][1]+1]
            if q[rear][0] == M:
                front = rear
                break
    
    print("#%d %d" %(tc, q[front][1]))
"""

"""
        # 하나씩 pop하기
        front += 1
        if q[front][0] == M:
            break # while 나가기
        else:
"""
