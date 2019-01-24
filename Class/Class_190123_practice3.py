a = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7],
[15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# 이렇게 하면 문제? [[0] * 5]*5
newa = []
# 이거를 다 한 정렬로 이어서 정렬을 하고, 
# 그거를 5개씩 새로 넣는다.
for n in a:
    newa += n

for i in range(len(newa)-1):
    minI = i
    for j in range(i+1, len(newa)):
        if (newa[j] < newa[minI]):
            minI = j
    newa[i], newa[minI] = newa[minI], newa[i]

# 가는 루트 짜놓기 0, 1, 2, 3을 하면 1, 2, 3, 0 으로 다음 자리를 알려주는 것 0: 오른쪽 1: 아래 2: 왼쪽 3: 위
route = [1, 2, 3, 0]

x = y = 0
curroute = 0 # 오른쪽 가는 것으로 시작
for item in newa:
    result[x][y] = item
    if curroute == 0:  # 오른쪽으로 가는 중인데, 
        if y+1 > len(a[0])-1 or result[x][y+1] != 0: # 오른쪽 가는 중인데 길이 막혔다
            curroute = 1 # 아래로 내려간다 - 경로 변경
            x += 1
        else: # 길이 안 막혔다.
            y += 1
    elif curroute == 1: # 아래로 가는 중인데,
        if x+1 > len(a)-1 or result[x+1][y] != 0: # 아래 막힘
            curroute = 2 # 왼쪽으로 간다 - 경로 변경
            y -= 1
        else:
            x += 1
    elif curroute == 2: # 왼쪽으로 가는 중인데,
        if y-1 < 0 or result[x][y-1] != 0: # 왼쪽 막힘
            curroute = 3 # 위로 간다 - 경로 변경
            x -= 1
        else:
            y -= 1
    elif curroute == 3: # 위로 가는 중인데
        if x-1 < 0 or result[x-1][y] != 0: # 위쪽 막힘
            curroute = 0 # 오른쪽으로 간다 - 경로 변경
            y += 1
        else:
            x -= 1
print(result)


# 선생님 코드
sorted_ary = [[0]*5 for _ in range(5)]

def sel_min(): # select min
    minX, minY = 0, 0
    for i in range(5):
        for j in range(5):
            # 2차 배열을 다 돌면서 min 인덱스를 찾는다.
            if ary[minX][minY] > ary[i][j]:
                minX, minY = i, j
    # 주어진 매트릭스에서 가장 작은 값을 반환
    min = ary[minX][minY]
    # 25번 부를 때, 한 번 찾았다는 정보는 처리를 해야 한다.
    ary[minX][minY] = 99
    return min

def isWall(x, y): # 벽인지 확인
    if x<0 or x>=5: return True
    if y<0 or y>=5: return True
    if sorted_ary[x][y] != 0: return True
    return False

X, Y = 0, 0 # 달팽이 최초 시작점
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_stat = 0 # 벡터 중에 어떤 것을 취할 것인지. 최초 디렉션은 0방향

for i in range(25):
    cur_min = sel_min() # 처음에 부르면 전체 min 값은 1이 나온다. (함수 안에서 99로 표시됨)
    sorted_ary[X][Y] = cur_min
    X += dx[dir_stat] # x, y 에서 x,y + (0,1)을 하면 옆의 좌표로 간다.
    Y += dy[dir_stat] # 크기 1만큼 한 방향으로 가는 벡터가 되는 것이다.

    if isWall(X,Y): # 벽에 닿으면, 벗어났으면 어떻게 할지 로직
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4 # 0, 1, 2, 3 뺑글뺑글 돌게 모듈라 연산
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]

for i in range(5):
    for j in range(5):
        print(sorted_ary[i][j], end=" ")
    print()
# 아래 코드는 17부터 못 돌아간다.
# result[0][:] = newa[0:5]
# x, y = 1, 4
# for item in newa[5:]:
#     result[x][y] = item
#     if y-1 < 0 or result[x][y-1] != 0: # 왼쪽 막힘
#         x -= 1 if x-1 >= 0 and result[x-1][y] == 0 else 0 # 위로
#     elif x+1 > len(a)-1 or result[x+1][y] != 0: # 아래 막힘
#         y -= 1 if y-1 >= 0 and result[x][y-1] == 0 else 0 # 왼쪽으로
#     elif y+1 > len(a[0])-1 or result[x][y+1] != 0: # 오른쪽 막힘
#         x += 1 if x+1 <= len(a)-1 and result[x+1][y] == 0 else 0 # 아래로
#     elif x-1 < 0 or result[x-1][y] != 0: # 위쪽 막힘
#         y += 1 if y+1 <= len(a[0])-1 or result[x][y+1] ==0 else 0 # 오른쪽으로 

    

