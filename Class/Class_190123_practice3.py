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

    

