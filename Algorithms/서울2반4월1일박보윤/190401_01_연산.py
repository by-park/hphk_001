"""
연산

2019.04.01 PBY 최초작성
"""

from collections import deque
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    if M*2 >= M+10:
        maxlen = M*2
    else:
        maxlen = M+10
    #maxlen = 1000000
    memo = [0] * (maxlen)
    q = deque([N])
    
    # memo를 돌면서 계산한 값을 넣기
    while q:
        num = q.popleft()
        #print(memo)
        if num + 1 <= maxlen: # 자연수 + 1
            if memo[num] == 0:
                memo[num] = memo[num-1]+1 # 최소로 오면 여기
                q.append(num+1)
#            else:
#                memo[num] = min(memo[num], memo[num-1]+1)
        if num -2 > 0: # index 에러가 나지 않게, 내 인덱스는 0부터 시작함
            if memo[num-2] == 0:
                memo[num-2] = memo[num-1]+1
                q.append(num-1)
#            else:
#                memo[num-2] = min(memo[num-2], memo[num-1]+1)
        if num*2 <= maxlen:
            if memo[num*2-1] == 0:
                memo[num*2-1] = memo[num-1]+1
                q.append(num*2)
#            else: 
#                memo[num*2-1] = min(memo[num*2-1], memo[num-1]+1)
        if num - 11 > 0:
            if memo[num-11] == 0:
                memo[num-11] = memo[num-1]+1
                q.append(num-10)
#            else:
#                memo[num-11] = min(memo[num-11], memo[num-1]+1)
                
    #print(memo)
    print("#%d %d" %(tc, memo[M-1]))

"""
# deque로 바꿔도 여전히 런타임 에러... 왜?
from collections import deque
T = int(input())
q = deque()
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maxlen = 1000000
    visited = [False]*(maxlen+1)
     # q에는 연산 값과 몇 번째 연산인지 저장
    cnt = 0
    if N+1 <= 1000000:
        q.append([N+1,1])
        cnt += 1
    if N-1 > 0:
        q.append([N-1, 1])
        cnt += 1
    if N*2 <=1000000:
        q.append([N*2, 1])
        cnt += 1
    if N-10 > 0:
        q.append([N-10, 1])
        cnt += 1
    for i in range(cnt):
        if q[i][0] == M:
            ans = 1
            q = deque()
            break
        
    while q:
        temp = q.popleft()
        visited[temp[0]] = True
        if temp[0]+1 <= 1000000 and not visited[temp[0]+1]:
            q.append([temp[0]+1, temp[1]+1])
            if temp[0]+1 == M:
                ans = temp[1]+1
                break
        if temp[0]-1 > 0 and not visited[temp[0]-1]:
            q.append([temp[0]-1, temp[1]+1])
            if temp[0]-1 == M:
                ans = temp[1]+1
                break
        if temp[0]*2 <= 1000000 and not visited[temp[0]*2]:
            q.append([temp[0]*2, temp[1]+1])
            if temp[0]*2 == M:
                ans = temp[1]+1
                break
        if temp[0]-10 > 0 and not visited[temp[0]-10]:
            q.append([temp[0]-10, temp[1]+1])
            if temp[0]-10 == M:
                ans = temp[1]+1
                break
    
    print("#%d %d" %(tc, ans))
"""

"""
# 런타임 에러 => 인덱스 에러가 나는 것 같다. 2 1000000 이 안 된다.

T = int(input())
q = [[0, 0] for _ in range(2**20)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maxlen = max(M*2, M+10)
    visited = [False]*(maxlen+1)
     # q에는 연산 값과 몇 번째 연산인지 저장
    front = rear = -1
    cnt = 0
    if maxlen >= N+1 and not visited[N+1]:
        rear += 1; q[rear][0] = N+1; q[rear][1] = 1
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    
    if N-1 > 0 and not visited[N-1]:
        rear += 1; q[rear][0] = N-1; q[rear][1] = 1
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    if maxlen >= N*2 and not visited[N*2]:
        rear += 1; q[rear][0] = N*2; q[rear][1] = 1
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    if N-10 > 0 and not visited[N-10]:
        rear += 1; q[rear][0] = N-10; q[rear][1] = 1
        cnt += 1
        if q[rear][0] == M:
            front = rear
            break
    for i in range(cnt):
        if q[i][0] == M:
            front = rear = i
            break
        
    while front != rear:
        temp0 = q[front][0]; temp1 = q[front][1]
        visited[temp0] = True # pop할 때 방문체크
        front += 1
        if maxlen >= temp0 + 1 and not visited[temp0+1]:
            rear += 1; q[rear][0] = temp0+1; q[rear][1] = temp1+1
            if q[rear][0] == M:
                front = rear
                break
        if  temp0-1 > 0 and not visited[temp0-1]:
            rear += 1; q[rear][0] = temp0-1; q[rear][1] =  temp1+1
            if q[rear][0] == M:
                front = rear
                break
        if temp0*2 <= maxlen and not visited[temp0*2]:
            rear += 1; q[rear][0] = temp0*2; q[rear][1] = temp1+1
            if q[rear][0] == M:
                front = rear
                break
        if temp0-10 > 0 and not visited[temp0-10]:
            rear += 1; q[rear][0] = temp0-10; q[rear][1] =  temp1+1
            if q[rear][0] == M:
                front = rear
                break
    
    print("#%d %d" %(tc, q[front][1]))

"""

"""
# 이렇게 하면 #3이 틀리는데, 자연수 N 다음 수 N+1이 뻗어나가는 배열이 최저 경로가 1이면 안 된다!!!!
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    if M*2 >= M+10:
        maxlen = M*2
    else:
        maxlen = M+10
    #maxlen = 1000000
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

"""
# deque 쓰려다가 어차피 런타임 에러는 똑같을 거 같아서 멈췄다.
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
# 런타임 에러 => 배열 크기가 너무 작은 듯하다.
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
