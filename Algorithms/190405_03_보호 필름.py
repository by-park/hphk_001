"""Solving Club"""
"""
보호 필름

2019.04.05 PBY 최초작성
"""

import sys
sys.stdin = open('190405_03_input.txt', 'r')


from itertools import combinations
import copy

def testFilm(films):
    global W, D, K
    for col in range(W):
        testList[col] = 0 # 초기값
        for row in range(D-K+1): # 행을 돌면서
            sum_ = 0
            for k in range(K):
                sum_ += films[row+k][col]
            if sum_ == 0 or sum_ == K: # 다 같은 개수면
                testList[col] = 1
        if testList[col] == 0: # 하나라도 안 되면 다 검사할 필요 없음 -> 홈페이지에서 댓글보고 힌트 얻음
            return False

            # if films[row][col] == films[row+1][col] == films[row+2][col]: # 실수의 흔적!
            #     testList[col] = 1
    # 모든 col을 다 돌고 나왔는데 1이 아니면?
    if sum(testList) == W: return True
    else: return False

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = []
    for _ in range(D):
        films.append(list(map(int, input().split())))
    testList = [0] * W # 테스트 전에는 0으로 들어가있다.

    # 처음에 통과할 수 있는지 체크
    result = testFilm(films)
    drug = 0
    while not result:
        # 약품 주입
        drug += 1
        # 약품 개수에 따라 어떤 줄을 약품 주입할 건지
        for selected_lines in combinations(range(D), drug):
            # 선택된 줄은 drug 개수
            # 바이너리 카운팅으로 그 약을 넣고 안 넣고
            injection = []
            for i in range(1<<drug):
                temp = [0] * drug
                for j in range(drug):
                    if i & (1<<j):
                        temp[j] = 1
                injection.append(temp)
            # 돌고 나면 바이너리 카운팅이 생겨남
            # 바이너리 카운팅을 돌면서 injection을 시켜줌
            # copied_films = copy.deepcopy(films)
            for case in range(len(injection)): # i를 돌고 나왔을 때, 그 만큼 injection이 생겨남 (이걸 그냥 생각하기 귀찮다고 i로 했다가 예제 케이스도 틀렸다...)
                # print(drug, injection[case])
                # copied_films = copy.deepcopy(films)
                selected = []  # 선택된 라인들 나중에 되돌리기 위해 저장하기
                for idx in range(drug): # 선택된 줄에다가 injection을 해준다.
                    # print(films[selected_lines[idx]][:])
                    selected.append(films[selected_lines[idx]][:]) # 이게 shallow copy가 되어서 자꾸 바뀌나 보다!
                    for idx2 in range(W):
                        films[selected_lines[idx]][idx2] = injection[case][idx] # 시간을 줄여주기 위해서 *W를 넣는 것 대신에 돌면서 인덱스 값을 바꾸도록
                        # copied_films[selected_lines[idx]][idx2] = injection[case][idx] # 시간을 줄여주기 위해서 *W를 넣는 것 대신에 돌면서 인덱스 값을 바꾸도록
                # injection을 다 했으면 체크하기
                # result = testFilm(copied_films)
                result = testFilm(films)
                # 체크하고 나왔으면 원상복귀
                for idx in range(drug):
                    # print(films[selected_lines[idx]])
                    for idx2 in range(W):
                        films[selected_lines[idx]][idx2] = selected[idx][idx2]

                # print("원상복귀 되었나?")
                if result:
                    break
            if result:
                break

    print("#%d %d" %(tc, drug))


