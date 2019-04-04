"""Splving Club"""
"""
핀볼 게임

2019.04.04 PBY 최초작성

# 벽에 부딪히면 끝나는 거라고 생각했는데, 사방이 경사이면 벽에 한 번도 안 부딪히고 계속 돌 수 있다!!!!
# 블록 방향도 자꾸 잘못 생각했다.... bd 채울 때

# 49번 케이스에서 틀리는 건 웜홀 때문이라고 한다. (1,1)과 (1,2) 일 때, 1에서 2로 가면 다시 1로 반복하지 않도록....!

# 재귀로 짜면 49번 케이스에서 못 돈다!!!!!!
"""

import sys
sys.stdin = open('190404_03_input.txt', 'r')

def goPinball(nextx, nexty, nextd, score, startx, starty):
    while True:
        # print(x, y, d)
        global maxscore
        # x, y 지점에 있는게 블랙홀이면 maxvalue 업데이트
        # 방향이 99면 시작점으로 돌아올 거기 때문에 maxvalue 업데이트
        if nextd == 99 or gameboard[nextx][nexty] == -1:
            if score > maxscore:
                maxscore = score
            break # while문 탈출

        # 아니면 그 지점으로 갈 수 있는 만큼 간다.
        while gameboard[nextx][nexty] == 0:
            # x, y에 대한 처리를 해준다.
            # 나한테 들어온 d로 계속 간다.
            nextx += dx[nextd]; nexty += dy[nextd]
            if nextx == startx and nexty == starty:
                nextd = 99 # 더이상 가지 않고 원래 출발점이라는 것을 표시해준다.
                break
            # 뭔가를 만날 때까지 while 문을 돈다.

        # 블록에 부딪히면 점수 증가!
        if 1 <= gameboard[nextx][nexty] <= 5:
            # 딕셔너리 들어가서 다음 방향 데려오기
            nextd = bd[gameboard[nextx][nexty]][nextd] # 반대로 튕겨나옴
            # 여기서 멈추면 블록에 계속 멈춰있게 된다. while을 돌지 않으니까
            nextx += dx[nextd]; nexty += dy[nextd]
            score += 1

        # 웜홀에 들어가서 나오기
        elif 6 <= gameboard[nextx][nexty] <= 10:
            nextx, nexty = wormholes[nextx][nexty]
            nextx += dx[nextd]; nexty += dy[nextd]
            # 웜홀에 들어가서 나왔는데 블록이나 벽이면?

        # 부딪혀서 나왔는데 시작점이면?
        if nextx == startx and nexty == starty:
            nextd = 99


# 게임에 필요한 도구들
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

# 방향과 부딪히는 블록의 관계 설정
bd = {
         1: {0: 1, 1: 3, 2: 0, 3: 2},
         2: {0: 3, 1: 0, 2: 1, 3: 2},
         3: {0: 2, 1: 0, 2: 3, 3: 1},
         4: {0: 1, 1: 2, 2: 3, 3: 0},
         5: {0: 1, 1: 0, 2: 3, 3: 2}

} # 블록: 방향 => 새로운 방향
# 상 0 하 1 좌 2 우 3

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 게임 준비~~~!!!
    gameboard = [[5] * (N+2)]
    for _ in range(N):
        gameboard.append([5]+list(map(int, input().split()))+[5])
    gameboard.append([5]*(N+2))
    maxscore = 0
    N += 2
    # 웜홀 위치 저장하기
    # wormholes = {}
    wormholes = [[0] * N for _ in range(N)]
    for w in range(6, 11):  # 가능한 웜홀 중 누가 있는지 확인
        wormhole = []
        for i in range(N):
            for j in range(N):
                if gameboard[i][j] == w:
                    wormhole.append([i, j])
        # 다 돌고 나면 wormhome에 0개 혹은 2개가 들어있다.
        if len(wormhole) > 0:
            wormholes[wormhole[0][0]][wormhole[0][1]] = wormhole[1]
            wormholes[wormhole[1][0]][wormhole[1][1]] = wormhole[0]


    # 게임 시작~~~~!!!!
    for i in range(1, N-1): # padding을 제외하고
        for j in range(1, N-1):
            if gameboard[i][j] == 0:  # 시작할 수 있는 지점이어야 시작
                goPinball(i, j, 0, 0, i, j)  # 상
                goPinball(i, j, 1, 0, i, j)  # 하
                goPinball(i, j, 2, 0, i, j)  # 좌
                goPinball(i, j, 3, 0, i, j)  # 우

    print("#%d %d" % (tc, maxscore))

# 49번까지 맞는 케이스
"""
def goPinball(x, y, d, score, startx, starty):
    # print(x, y, d)
    global maxscore
    # x, y 지점에 있는게 블랙홀이면 maxvalue 업데이트
    # 방향이 99면 시작점으로 돌아올 거기 때문에 maxvalue 업데이트
    if d == 99 or gameboard[x][y] == -1:
        if score > maxscore:
            maxscore = score
        return

    # 아니면 그 지점으로 갈 수 있는 만큼 간다.

    nextx = x; nexty = y; nextd = d; nextscore = score
    while gameboard[nextx][nexty] == 0:
        # x, y에 대한 처리를 해준다.
        # 나한테 들어온 d로 계속 간다.
        nextx += dx[d]; nexty += dy[d]
        if nextx == startx and nexty == starty:
            nextd = 99 # 더이상 가지 않고 원래 출발점이라는 것을 표시해준다.
            break
        # 뭔가를 만날 때까지 while 문을 돈다.

    # 블록에 부딪히면 점수 증가!
    if 1 <= gameboard[nextx][nexty] <= 5:
        # 딕셔너리 들어가서 다음 방향 데려오기
        nextd = bd[gameboard[nextx][nexty]][d] # 반대로 튕겨나옴
        # 여기서 멈추면 블록에 계속 멈춰있게 된다. while을 돌지 않으니까
        nextx += dx[nextd]; nexty += dy[nextd]
        nextscore += 1

    # 웜홀에 들어가서 나오기
    elif 6 <= gameboard[nextx][nexty] <= 10:
        nextx, nexty = wormholes[nextx][nexty]
        nextx += dx[nextd]; nexty += dy[nextd]
        # 웜홀에 들어가서 나왔는데 블록이나 벽이면?

    # 부딪혀서 나왔는데 시작점이면?
    if nextx == startx and nexty == starty:
        nextd = 99

    goPinball(nextx, nexty, nextd, nextscore, startx, starty)  # -1을 만나거나, 벽에 부딪혀서 while 문이 끝난 경우는 else에 해당


# 게임에 필요한 도구들
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

# 방향과 부딪히는 블록의 관계 설정
bd = {
         1: {0: 1, 1: 3, 2: 0, 3: 2},
         2: {0: 3, 1: 0, 2: 1, 3: 2},
         3: {0: 2, 1: 0, 2: 3, 3: 1},
         4: {0: 1, 1: 2, 2: 3, 3: 0},
         5: {0: 1, 1: 0, 2: 3, 3: 2}

} # 블록: 방향 => 새로운 방향
# 상 0 하 1 좌 2 우 3

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 게임 준비~~~!!!
    gameboard = [[5] * (N+2)]
    for _ in range(N):
        gameboard.append([5]+list(map(int, input().split()))+[5])
    gameboard.append([5]*(N+2))
    maxscore = 0
    N += 2
    # 웜홀 위치 저장하기
    # wormholes = {}
    wormholes = [[0] * N for _ in range(N)]
    for w in range(6, 11):  # 가능한 웜홀 중 누가 있는지 확인
        wormhole = []
        for i in range(N):
            for j in range(N):
                if gameboard[i][j] == w:
                    wormhole.append([i, j])
        # 다 돌고 나면 wormhome에 0개 혹은 2개가 들어있다.
        if len(wormhole) > 0:
            wormholes[wormhole[0][0]][wormhole[0][1]] = wormhole[1]
            wormholes[wormhole[1][0]][wormhole[1][1]] = wormhole[0]


    # 게임 시작~~~~!!!!
    for i in range(1, N-1): # padding을 제외하고
        for j in range(1, N-1):
            if gameboard[i][j] == 0:  # 시작할 수 있는 지점이어야 시작
                goPinball(i, j, 0, 0, i, j)  # 상
                goPinball(i, j, 1, 0, i, j)  # 하
                goPinball(i, j, 2, 0, i, j)  # 좌
                goPinball(i, j, 3, 0, i, j)  # 우

    print("#%d %d" % (tc, maxscore))
"""

"""
def goPinball(x, y, d, score):
    global maxscore, N
    # x, y 지점에 있는게 블랙홀이면 maxvalue 업데이트
    # 방향이 99면 시작점으로 돌아올 거기 때문에 maxvalue 업데이트
    if gameboard[x][y] == -1:
        if score > maxscore:
            maxscore = score
        return
    if d == 99:
        if score*2 + 1 > maxscore:
            maxscore = score*2 + 1
        return

    # 아니면 그 지점으로 갈 수 있는 만큼 간다.
    if x + dx[d] < 0 or x + dx[d] >= N or y + dy[d] < 0 or y + dy[d] >= N:
        nextx = x; nexty = y;
        # 벽에 부딪혔으면
        nextd = 99; nextscore = score
    else:

        nextx = x + dx[d]; nexty = y + dy[d]; nextd = d;
        while gameboard[nextx][nexty] == 0:
            # 나한테 들어온 d로 계속 간다.
            if nextx + dx[d] < 0 or nextx + dx[d] >= N or nexty + dy[d] < 0 or nexty + dy[d] >= N:
                nextd = 99 # 벽에 부딪히면!
                break
            nextx += dx[d]; nexty += dy[d]
        # 뭘 만나면
        # 그걸로 다음 재귀를 들어간다.
        nextscore = score

        # 블록에 부딪히면 점수 증가!
        if nextd != 99 and 1 <= gameboard[nextx][nexty] <= 5:
            # 딕셔너리 들어가서 다음 방향 데려오기
            nextd = bd[gameboard[nextx][nexty]][d]
            # 벽에 부딪혀서 나온 d가 99면 score를 업데이트 하지 않음
            if nextd != 99:
                nextscore += 1

        # 웜홀에 들어가서 나오기
        elif nextd != 99 and 6 <= gameboard[nextx][nexty] <= 10:
            nextx, nexty = wormholes[nextx][nexty]

    goPinball(nextx, nexty, nextd, nextscore)  # -1을 만나거나, 벽에 부딪혀서 while 문이 끝난 경우는 else에 해당


# 게임에 필요한 도구들
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

# 방향과 부딪히는 블록의 관계 설정
bd = {
         1: {0: 99, 1: 3, 2: 99, 3: 0},
         2: {0: 3, 1: 99, 2: 99, 3: 1},
         3: {0: 2, 1: 99, 2: 1, 3: 99},
         4: {0: 99, 1: 2, 2: 0, 3: 99},
         5: {0: 99, 1: 99, 2: 99, 3: 99}

} # 블록: 방향 => 새로운 방향
# 상 0 하 1 좌 2 우 3

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 게임 준비~~~!!!
    gameboard = []
    for _ in range(N):
        gameboard.append(list(map(int, input().split())))
    maxscore = 0

    # 웜홀 위치 저장하기
    # wormholes = {}
    wormholes = [[0] * N for _ in range(N)]
    for w in range(6, 11):  # 가능한 웜홀 중 누가 있는지 확인
        wormhole = []
        for i in range(N):
            for j in range(N):
                if gameboard[i][j] == w:
                    wormhole.append([i, j])
        # 다 돌고 나면 wormhome에 0개 혹은 2개가 들어있다.
        if len(wormhole) > 0:
            wormholes[wormhole[0][0]][wormhole[0][1]] = wormhole[1]
            wormholes[wormhole[1][0]][wormhole[1][1]] = wormhole[0]


    # 게임 시작~~~~!!!!
    for i in range(N):
        for j in range(N):
            if gameboard[i][j] == 0:  # 시작할 수 있는 지점이어야 시작

                goPinball(i, j, 0, 0)  # 상
                goPinball(i, j, 1, 0)  # 하
                goPinball(i, j, 2, 0)  # 좌
                goPinball(i, j, 3, 0)  # 우

    print("#%d %d" % (tc, maxscore))
"""


"""
def goPinball(x, y, d, score):
    global maxscore, N, startx, starty
    # x, y 지점에 있는게 블랙홀이면 maxvalue 업데이트
    # 방향이 99면 시작점으로 돌아올 거기 때문에 maxvalue 업데이트
    if gameboard[x][y] == -1 or (x == startx and y == starty):
        if score > maxscore:
            maxscore = score
        return
    # if d == 99:
        # if score*2 + 1 > maxscore:
        #     maxscore = score*2 + 1
        # return

    # 아니면 그 지점으로 갈 수 있는 만큼 간다.
    if x + dx[d] < 0 or x + dx[d] >= N or y + dy[d] < 0 or y + dy[d] >= N:
        nextx = x; nexty = y;
        # 벽에 부딪혔으면
        nextscore = score + 1
        if d == 0: # 상이면
            nextd = 1
        elif d == 1: # 하면
            nextd = 0
        elif d == 2: #좌면
            nextd = 3
        elif d == 3:
            nextd = 2
        # nextd = 99
    else:
        if x+dx[d] == startx and y+dy[d] == starty: # 시작점으로 돌아오면
            
        nextx = x+dx[d]; nexty = y+dy[d]; nextd = d; nextscore = score
        while gameboard[nextx][nexty] == 0:
            # 나한테 들어온 d로 계속 간다.
            if nextx + dx[d] < 0 or nextx + dx[d] >= N or nexty + dy[d] < 0 or nexty + dy[d] >= N:
                nextscore = score + 1
                if d == 0:  # 상이면
                    nextd = 1
                elif d == 1:  # 하면
                    nextd = 0
                elif d == 2:  # 좌면
                    nextd = 3
                elif d == 3:
                    nextd = 2
                # nextd = 99 # 벽에 부딪히면!
                break
            nextx += dx[d]; nexty += dy[d]
        # 뭘 만나면
        # 그걸로 다음 재귀를 들어간다.
        # nextscore = score

        # 블록에 부딪히면 점수 증가!
        if 1 <= gameboard[nextx][nexty] <= 5:
            # 딕셔너리 들어가서 다음 방향 데려오기
            nextd = bd[gameboard[nextx][nexty]][d]
            nextscore += 1

        # 웜홀에 들어가서 나오기
        elif 6 <= gameboard[nextx][nexty] <= 10:
            nextx, nexty = wormholes[nextx][nexty]

    goPinball(nextx, nexty, nextd, nextscore) # -1을 만나거나, 벽에 부딪혀서 while 문이 끝난 경우는 else에 해당


# 게임에 필요한 도구들
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

# 방향과 부딪히는 블록의 관계 설정
# bd = {
#          1: {0: 99, 1: 3, 2: 99, 3: 0},
#          2: {0: 3, 1: 99, 2: 99, 3: 1},
#          3: {0: 2, 1: 99, 2: 1, 3: 99},
#          4: {0: 99, 1: 2, 2: 0, 3: 99},
#          5: {0: 99, 1: 99, 2: 99, 3: 99}
#
# } # 블록: 방향 => 새로운 방향
# 상 0 하 1 좌 2 우 3
bd = {
         1: {0: 99, 1: 3, 2: 99, 3: 0},
         2: {0: 3, 1: 99, 2: 99, 3: 1},
         3: {0: 2, 1: 99, 2: 1, 3: 99},
         4: {0: 99, 1: 2, 2: 0, 3: 99},
         5: {0: 99, 1: 99, 2: 99, 3: 99}

} # 블록: 방향 => 새로운 방향
# 상 0 하 1 좌 2 우 3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 게임 준비~~~!!!
    gameboard = []
    for _ in range(N):
        gameboard.append(list(map(int, input().split())))
    maxscore = 0

    # 웜홀 위치 저장하기
    # wormholes = {}
    wormholes = [[0] * N for _ in range(N)]
    for w in range(6, 11): # 가능한 웜홀 중 누가 있는지 확인
        wormhole = []
        for i in range(N):
            for j in range(N):
                if gameboard[i][j] == w:
                    wormhole.append([i, j])
        # 다 돌고 나면 wormhome에 0개 혹은 2개가 들어있다.
        if len(wormhole) > 0:
            wormholes[wormhole[0][0]][wormhole[0][1]] = wormhole[1]
            wormholes[wormhole[1][0]][wormhole[1][1]] = wormhole[0]
            # wormholes[wormhole[0][0]] = {wormhole[0][1]: wormhole[1]}
            # wormholes[wormhole[1][0]] = {wormhole[1][1]: wormhole[0]}
            # wormholes[wormhole[0]] = wormhole[1] # 딕셔너리에 담아준다.
            # wormholes[wormhole[1]] = wormhole[0]

    # 게임 시작~~~~!!!!
    for i in range(N):
        for j in range(N):
            if gameboard[i][j] == 0: # 시작할 수 있는 지점이어야 시작
                startx = i; starty = j
                goPinball(i, j, 0, 0) # 상
                goPinball(i, j, 1, 0) # 하
                goPinball(i, j, 2, 0) # 좌
                goPinball(i, j, 3, 0) # 우

    print("#%d %d" %(tc, maxscore))
    
"""
