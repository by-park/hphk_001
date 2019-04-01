lines = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
array = [[0 for _ in range(7)] for __ in range(7)]
visited = [False]*7
for idx in range(0, len(lines), 2):
    array[lines[idx]-1][lines[idx+1]-1] = 1
    array[lines[idx+1]-1][lines[idx]-1] = 1

# 깊이우선탐색
def DFS(v):
    visited[v] = True
    print(v+1, end='-')
    for i in range(7):
        if array[v][i] == 1 and not visited[i]:
            DFS(i)

DFS(0)
