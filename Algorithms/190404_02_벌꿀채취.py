"""Solving Club"""
"""
벌꿀채취

2019.04.04 PBY 최초작성

계속 실수했던 부분은 벌통 크기를 줄여갈 때, 최대 벌통 크기가 M이라는 것을 함수 안에서 고려를 안 해줬고 (N으로 하는 바람에 내 벌통 넘어가서까지 채취했다)
그 다음에도 1개를 골라도 최대 벌통 크기 M에서 골라야하는데, 1개 고를 때 1개 범위 안에서만 찾게 해서 7 2 9 면 9 못 찾고 7에서 자꾸 끝나버렸다.
"""

import sys
sys.stdin = open('190404_02_input.txt', 'r')

def gethoney(hcnt, maxh, cur_sum, cur_honey, x, y, N):
    global honey
    if cur_sum > C: # 벌꿀 채취 가능 개수를 넘어가면?
        return
    if hcnt == maxh: # 선택할 수 있는 만큼 다 선택했으면
        if honey < cur_honey:
            honey = cur_honey
        return
    if y >= N: # 더 이상 벌꿀 채취 못하면
        return

    # 그 개수로 만들 수 있는 최대 개수
    # used[hcnt] = True
    gethoney(hcnt+1, maxh, cur_sum + bh[x][y], cur_honey + bh[x][y]*bh[x][y], x, y+1, N)
    # used[hcnt] = False
    gethoney(hcnt, maxh, cur_sum, cur_honey, x, y+1, N)

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    bh = []
    for _ in range(N):
        bh.append(list(map(int, input().split())))
        
    # used = [False]*M # 일꾼들을 위한 순열
    maxvalue = 0 # 결과 변수 초기화

    # M개씩 찾아간다.
    for row in range(N):
        for col in range(N-M+1):
            honey1 = 0 # 일꾼1의 맥스값

            # 시작점을 정해줌
            start = [row, col]
            # 시작점부터 M개 벌통에서 꿀을 채취할 수 있는지 확인
            # 순열 구하기 4개가 다 가능하면 4개를 채취하고, 아니면 하나씩 줄여가면서 채취해야한다.
            for cnt in range(M, 0, -1): # 벌꿀 채취 개수를 줄여가면서
                honey = 0
                # 벌꿀 채취 개수가 최대이면?, 최대 개수 ex 4개로 먼저 조합을 만들어 볼 것
                gethoney(0, cnt, 0, 0, start[0], start[1], start[1]+M) # 만들 수 없으면 return 0
                if honey1 < honey: # 최대 수익 업데이트
                    honey1 = honey
                # if honey1 != 0: # 수익이 났으면 더 줄여서 채취할 필요 없음
                #     break
            # 여기서부터 다시 다른 벌꿀 찾아들어감

            for row2 in range(start[0], N):
                for col2 in range(N-M+1):
                    honey2 = 0
                    if row2 == start[0]: # 그 줄에 가능한 벌꿀 돌기
                        if N-1-start[1] < M: # 남은 벌꿀통 개수가 두 번째 일꾼이 돌 수 없을 정도로 작으면 패스
                            continue
                        if col2 < start[1]+M: # 첫번째 벌꿀 채취하는 곳이면 패스
                            continue
                    other = [row2, col2]
                    # 이걸 가지고 또 4개가 가능하면 4개를 채취하고, 아니면 하나씩 줄여가면서 채취하기
                    # 그리고 나서 두 개 합한게 최대 수익인지 확인
                    for cnt in range(M, 0, -1):
                        honey = 0
                        gethoney(0, cnt, 0, 0, other[0], other[1], other[1]+M)
                        if honey2 < honey:
                            honey2 = honey
                            # print(honey2)
                        # if honey2 != 0:
                        #     break

                    if honey1 + honey2 > maxvalue:
                        maxvalue = honey1 + honey2

    print("#%d %d" %(tc, maxvalue))