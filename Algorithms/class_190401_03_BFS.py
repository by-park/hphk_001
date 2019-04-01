lines = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
array = [[0 for _ in range(7)] for __ in range(7)]
visited = [False]*7
for idx in range(0, len(lines), 2):
    array[lines[idx]-1][lines[idx+1]-1] = 1
    array[lines[idx+1]-1][lines[idx]-1] = 1

q = [0] * 7
front = -1; rear = -1
rear+=1
visited[0] = True; q[rear] = 0 # 1번 정점 들어감
print(0+1, end='-')
while front != rear:
    # 맨 앞에 있는 걸 꺼내서
    front += 1
    for i in range(7):
        if array[q[front]][i] == 1 and not visited[i]:
            rear += 1
            visited[i] = True
            q[rear] = i
            print(i+1, end='-')
