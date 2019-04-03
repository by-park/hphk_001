"""
Ladder1과 뭐가 다르지? => 전체 다 내려가보고 최단 거리를 찾는 게 다르다.
"""

import sys
sys.stdin = open('190307_04_input.txt','r')

def findDistance(startpoint):
    row = 0; col = startpoint
    length = 0
    while row < 100: # 100줄을 내려가면서
        if col-1 >= 0 and ladder[row][col-1] == '1': # 왼쪽에 길이 있으면
            while col -1 >= 0 and ladder[row][col-1] == '1':
                col -= 1
                length += 1
            # 왼쪽 끝까지 가고 나왔으면 아래로 내려가기
            row += 1
            length += 1

        elif col + 1 < 100 and ladder[row][col+1] == '1': # 오른쪽에 길이 있으면
            while col+ 1 < 100 and ladder[row][col+1] == '1':
                col += 1
                length += 1
            # 오른쪽 끝까지 가고 나왔으면 아래로 내려가기
            row += 1
            length += 1
        else: # 아무데도 길이 없으면 내려가기
            row += 1
            length += 1
    return length


for tc in range(10):
    t = input()
    ladder = []
    for _ in range(100):
        ladder.append(input().split())

    # 존재하는 모든 시작점 찾기
    start = []
    for s in range(100):
        if ladder[0][s] == '1':
            start.append(s)

    # 시작점에서 가면서 거리가 얼마나 되는지 반환하기
    length = []
    for s in start:
        length.append(findDistance(s))

    # 짧은 시작점
    minvalue = min(length)
    for idx in range(len(length)):
        if length[idx] == minvalue:
            ans = start[idx]

    print("#%d %d" %(tc+1, ans))

"""
input을 문자로 받아놓고 함수 내에서 == 1 이 비교를 해서 사다리를 아래로만 내려갔다....
"""


# Ladder 1
"""
di = [0, 0, -1]
dj = [-1, 1, 0]

def findnext(i, j):
    if i == 0:
        print("#%d %d" %(tc+1, j))
    else:
        # 한쪽으로 갈 거면 나머지 길을 다 막아야한다. 안 그러면 재귀로 다시 돌아와서
        # 다른 길을 자꾸 탐색한다.

        for d in range(3):
            if 0<=i+di[d]<100 and 0<=j+dj[d]<100 and array[i+di[d]][j+dj[d]] == '1' : # 길이 있으면
                if 0<=j-1<100:
                    array[i][j-1] = '0'
                if 0<=j+1<100:
                    array[i][j+1] ='0'
                if 0<=i-1<100:
                    array[i-1][j] = '0' # 가능한 세 경로 다 막기
                findnext(i+di[d], j+dj[d])

for tc in range(10):
    n = input()
    array = []
    for _ in range(100):
        array.append(input().split())

    # 맨 아래에서 출발점 찾기
    for j in range(100):
        if array[99][j] == '2':
            array[99][j] = '0'
            start = j
            break

    # 재귀 호출로 다음 길 찾기
    findnext(99, j)
"""



# 선생님 코드
"""
#import sys; sys.stdin = open('input.txt')
def dfs(x, y):		# x = 행, y = 열
    if x == 0: return y
    arr[x][y] = 0
    ret = 0
    if y-1 >= 0 and arr[x][y-1] and arr[x][y-1]:
        ret = dfs(x, y-1)
    elif y + 1 < 100 and arr[x][y+1] and arr[x][y+1]:
        ret =  dfs(x, y+1)
    else:
        ret = dfs(x-1, y)
    # arr[x][y] = 1 # 복구하고 싶으면 여기에 넣으면 된다.
    return ret
    
for tc in range(1, 11):
    case = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(100)]
    sx = sy = 0		# 시작점 (실제로는 도착점이지만 우리는 시작하는 위치)
    for i in range(100):
        if arr[99][i] == 2:
            sx, sy = 99, i
            break
    print("#%d %d" %(case, dfs(sx, sy)))

"""
