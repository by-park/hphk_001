"""
재미있는 오셀로 게임

2019.03.07 PBY 최초작성
"""

import sys
sys.stdin = open('190307_01_input.txt','r')

def changeDol(mycolor, start, othercolor):
    global N

#    for j in range(N):
#        check = 0
    end = start
    # 오른쪽으로
    check = 0
    for j in range(1, N-start[1]):
        if osello[start[0]][start[1] + 1] == othercolor:
            check = 1
        if osello[start[0]][start[1]+j] == mycolor:
            end = (start[0], start[1]+j)
            break
        if osello[start[0]][start[1]+j] == 0:
            check = 0
            break
    if check == 1:
        for j in range(start[1], end[1]):
            osello[start[0]][j] = mycolor

    # 왼쪽으로
    end = start
    check = 0
    for j in range(1, start[1]+1):
        if osello[start[0]][start[1] - 1] == othercolor:
            check = 1
        if osello[start[0]][start[1]-j] == mycolor:
            end = (start[0], start[1]-j)
            break
        if osello[start[0]][start[1]-j] == 0:
            check = 0
            break
    if check == 1:
        for j in range(end[1], start[1]):
            osello[start[0]][j] = mycolor

    # 아래쪽으로
    end = start
    check = 0
    for i in range(1, N-start[0]):
        if osello[start[0]+1][start[1]] == othercolor:
            check = 1
        if osello[start[0]+i][start[1]] == mycolor:
            end = (start[0]+i, start[1])
            break
        if osello[start[0] + i][start[1]] == 0:
            check = 0
            break
    if check == 1:
        for i in range(start[0], end[0]):
            osello[i][start[1]] = mycolor

    # 위쪽으로 => 왜 위쪽 안 바꾸지...
    end = start
    check = 0
    for i in range(1, start[0]+1): # +1로 범위를 안 잡으면 0 까지 들어가지 않는다.....
        if osello[start[0]-1][start[1]] == othercolor:
            check = 1
        if osello[start[0]-i][start[1]] == mycolor: # 시작점이 (2,0) 일 때 왜 거짓말하지...
            end = (start[0]-i, start[1])
            break
        if osello[start[0]-i][start[1]] == 0:
            check = 0
            break

    if check == 1:
        for i in range(end[0], start[0]):
            osello[i][start[1]] = mycolor

    # 오른쪽 대각 아래로
    i = 1
    check = 0
    while start[0]+i < N and start[1]+i < N:
        if osello[start[0]+i][start[1]+i] == mycolor:
            check = 1
            end = (start[0]+i, start[1]+i)
            break
        elif osello[start[0]+i][start[1]+i] == 0:
            i = 0
            break
        i += 1

    if check == 1:
        for i2 in range(i):
            osello[start[0]+i2][start[1]+i2] = mycolor

    # 왼쪽 대각 아래로
    i = 1
    check = 0
    while start[0]+i < N and start[1]-i >= 0:
        if osello[start[0]+i][start[1]-i] == mycolor:
            check = 1
            end = (start[0]+i, start[1]-i)
            break
        elif osello[start[0]+i][start[1]-i] == 0:
            i = 0
            break
        i += 1

    if check == 1:
        for i2 in range(i):
            osello[start[0]+i2][start[1]-i2] = mycolor

    # 오른쪽 대각 위로
    i = 1
    check = 0
    while start[0]-i >= 0 and start[1]+i < N:
        if osello[start[0]-i][start[1]+i] == mycolor:
            end = (start[0]-i, start[1]+i)
            check = 1
            break
        elif osello[start[0]-i][start[1]+i] == 0:
            i = 0
            break
        i += 1

    if check == 1:
        for i2 in range(i):
            osello[start[0]-i2][start[1]+i2] = mycolor

    # 왼쪽 대각 위로
    i = 1
    check = 0
    while start[0]-i >= 0 and start[1]-i >= 0:
        if osello[start[0]-i][start[1]-i] == mycolor:
            end = (start[0]-i, start[1]-i)
            check = 1
            break
        elif osello[start[0]-i][start[1]-i] == 0:
            i = 0
            break
        i += 1

    if check == 1:
        for i2 in range(i):
            osello[start[0]-i2][start[1]-i2] = mycolor



    """            
    for i in range(N):
        for j in range(N-2):
            if osello[i][j] == mycolor and osello[i][j+1] == othercolor and osello[i][j+2] == mycolor:
                osello[i][j+1] = mycolor
            if osello[j][i] == mycolor and osello[j+1][i] == othercolor and osello[j+2][i] == mycolor:
                osello[j+1][i] = mycolor

    for i in range(N-2):
        for j in range(N-2):
            if osello[i][j] == mycolor and osello[i+1][j+1] == othercolor and osello[i+2][j+2] == mycolor:
                osello[i+1][j+1] = mycolor

    for i in range(N-1, 1, -1):
        for j in range(N-2):
            if osello[i][j] == mycolor and osello[i-1][j+1] == othercolor and osello[i-2][j+2] == mycolor:
                osello[i-1][j+1] = mycolor
    """

# 흑돌 1 백돌 2
T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    osello = [[0 for _ in range(N)] for __ in range(N)]
    # 가운데 돌 배치
    osello[N//2-1][N//2-1] = 2
    osello[N//2][N//2] = 2
    osello[N//2-1][N//2] = 1
    osello[N//2][N//2-1] = 1

    for _ in range(M):
        current_input = list(map(int, input().split()))
        osello[current_input[1]-1][current_input[0]-1] = current_input[2]
        if current_input[2] == 1: # 흑돌
            changeDol(1, (current_input[1]-1, current_input[0]-1), 2)
        #changeDol(2, 1)
        else:
            changeDol(2, (current_input[1]-1, current_input[0]-1), 1)
        #    changeDol(1, 2)


    # countDol
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if osello[i][j] == 1:
                black += 1
            elif osello[i][j] == 2:
                white += 1

    print("#%d" %(tc+1), black, white)


"""
천재 전세환님 코멘트
오셀로 게임은 처음 나랑 같은 돌을 만날 때까지만 색을 변경시킬 수 있다. break가 필요하다.
○●○●●○ 이런 식인 경우가 예외 케이스
"""