""" 
4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

[문제 내용]
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

최초 작성 2019.01.17 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190117_02_input.txt", "r")

TC = int(input())

for i in range(TC):
    K, N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))

    # 모든 정류장
    stops = [0] * (N+1)
    # 버스스탑 채우기
    for stop in S:
        stops[stop] = 1

    pre_index = -K
    cur_index = 0
    stopnum = 0
    while True:
        if pre_index == cur_index:
            print("#{} {}".format(i+1, 0))
            break
        if cur_index + K >= N:
            print("#{} {}".format(i+1, stopnum))
            break
        if stops[cur_index + K] == 1:
            pre_index = cur_index
            cur_index += K
            stopnum += 1            
        else:
            cur_index -= 1 

        
    


# visual studio는 실행시 ctrl + f5

# 1차 시도
# 처음에 0을 넣을 뿐 아니라, 마지막에 마지막 정류소도 넣어야
# 마지막까지 무사히 충전이 되었는지 확인할 수 있는데
# 그걸 안 넣어서 한 번 틀렸다.

# 2차 시도
# 시간 초과
# 함수를 없애고, for 문을 최소한으로 줄이려고 시도하였다.

# 그리디 알고리즘
# 1 2 1 
# 1 답이 1이어야 하는 경우
# 3 2 1 
# 1 답이 0이어야 하는 경우 - 한 번에 가는 경우 실패
# 1 3 1 
# 1 답이 0이어야 하는 경우

# 
# pre_index = -2를 pre_index = -K로 변경함


# 모든 경우의 수 만들기 - 실패!
"""
def combinations(current_list, target_list, result=[]):
    if current_list == target_list:
        return result
    for item in range(len(target_list)):
        current_list2 = current_list[:] + [target_list[item]]
        target_list2 = target_list[item+1:]
        result += [current_list2]
        print(current_list2, target_list2)
        return combinations(current_list2, target_list2, result)
"""

# 시간 초과 전 코드
"""
from itertools import combinations
TC = int(input())

# 조합 함수
def all_comb(lst):
    result = []
    for num in range(1, len(lst)+1):
        result += list(map(list, combinations(lst, num)))
    return result

for i in range(TC):
    K, N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))

    # 완전 탐색
    all_list = all_comb(S)
    result_list = all_list[:]
    for case in all_list:
        new_case = [0] + case + [N] # 시작점을 넣어줌. 충전하고 시작하니까
        for item in range(1, len(new_case)):
            if new_case[item] > K + new_case[item-1]: # 이전 위치에서 4칸 더 갈 수 있는가
                result_list.remove(case) # 해당 경우는 삭제
                break # 한 지점이라도 충전 못하면 바로 나가기

    if len(result_list) < 1:
        print("#{} {}".format(i+1, 0))
    else:
        min_len = min([len(x) for x in result_list])
        print("#{} {}".format(i+1, min_len))
"""

# 시간 초과 함수 줄인 거로 조금 나아진 코드 7개 맞음
"""
from itertools import combinations
TC = int(input())

for i in range(TC):
    K, N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))

    # 완전 탐색
    result = []
    for num in range(1, len(S)+1): # N//K은 아마 K=0인 경우에 런타임 에러,  1부터 하면 제한 시간 초과 모든 가지수 다 보지 말고, 충전기가 있어야 하는 범위...
        case = list(map(list, combinations(S, num)))
        for one_case in case:
            current_case = [0] + one_case + [N]
            check = 1 # 일단 가능하다고 가정
            for stop in range(1, len(current_case)):
                if current_case[stop] > K + current_case[stop-1]:
                    check = 0 # 불가능한 상황을 만나면 나가기
                    break
            if check == 1:
                result.append(len(current_case)-2) # 0 이랑 N 더한 거 빼기

    if len(result) < 1:
        print("#{} {}".format(i+1, 0))
    else:
        min_len = min(result)
        print("#{} {}".format(i+1, min_len))
"""

# 그리디 시도 2개 틀렸다고 나옴
"""
TC = int(input())

for i in range(TC):
    K, N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))

    # 예외 케이스 처리
    if N <= K:
        print("#{} {}".format(i+1, 0))
        continue

    candidates = list(filter(lambda x: x <= K, S)) # 시작 트리
    min_deep = len(S) # 전체 깊이


    for j in candidates:
        end_point = j
        result = [] # 가지를 쭉 담아내려갈 것
        while end_point + K < N: # endpoint >= 10 마지막 정류소에 닿는 순간 종료
            next_candidates = list(filter(lambda x: end_point < x <= K + end_point, S))
            # 충전기가 부족해서 가지 못하는 경우 처리            
            if len(next_candidates) < 1:
                if len(result) < 1: # 아예 더 이상 가능한 트리가 없을 때
                    break # 다음 경우 탐색
                end_point = result[-1][0] # 이전 트리로 돌아가기
                result[-1].remove(result[-1][0])
                break # 다음 경우 탐색
            end_point = next_candidates[-1]
            result.append(next_candidates)

        if end_point + K >= N and min_deep > (len(result) + 1):
            min_deep = len(result) + 1

    if end_point + K < N and len(result) < 1: # 이렇게 하면 마지막 정류소 부터 시작한 게 답이 아닌 애들이 틀리게 된다. 
        print("#{} {}".format(i+1, 0))
    else:
        print("#{} {}".format(i+1, min_deep))
"""