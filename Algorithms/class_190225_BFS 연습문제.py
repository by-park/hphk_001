node = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()
node = list(map(int, node))

# 인접행렬 만들기
array = [[0 for j in range(7)] for i in range(7)]
for n in range(0, len(node), 2):
        array[node[n]-1][node[n+1]-1] = 1
        array[node[n+1]-1][node[n]-1] = 1

# BFS 구현
Q = [0] * (7*7)
visited = [0]* 7
front = 0
rear = 1

# Q의 초기값
Q[front] = 1

while front != rear:
    print(Q)
    print(visited)
    # 자기 자신 처리
    visited[Q[front]-1] = 1
    
    # 주변 이웃 처리
    for j in range(7):
        if array[Q[front]-1][j] == 1 and not visited[j]:
            Q[rear] = j+1
            rear += 1

    print(Q[front]) # 매번 출력 결과
    front += 1 # 나를 처리한 후에는 꺼낸다.
