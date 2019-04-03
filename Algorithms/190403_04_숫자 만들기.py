"""Solving Club"""
"""
숫자 만들기

2019.04.03 PBY 최초작성

"""

import sys
sys.stdin = open('190403_04_input.txt', 'r')

def permutations(cur, cursum, depth):
    if cur == depth:
        anslist.append(cursum)
        return
    # 4개를 다 보면서 선택하고 선택하지 않고
    for i in range(4):
        if operands[i] > 0:
            operands[i] -= 1
            if i == 0:
                permutations(cur+1, cursum+numbers[cur+1], depth)
            elif i == 1:
                permutations(cur+1, cursum-numbers[cur+1], depth)
            elif i == 2:
                permutations(cur+1, cursum*numbers[cur+1], depth)
            else:
                permutations(cur+1, int(cursum/numbers[cur+1]), depth) # 이걸 cursum//numbers[cur+1] 하면 오답이 생긴다. 소숫점을 버리라는게 이런 의미인가 보다 - 종민님 감사....
            operands[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operands = list(map(int, input().split())) # 이걸 빼면서 used처럼 사용할 것
    numbers = list(map(int, input().split()))
    anslist = []
    permutations(0, numbers[0], N-1)

    print("#%d %d" %(tc, max(anslist) - min(anslist)))



# 메모리 초과....
# 연산자 4개를 가지고 순서를 구하기
"""
from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, multi, div = map(int, input().split())
    operands = [0]*plus + [1]*minus + [2]* multi + [3]*div
    numbers = list(map(int, input().split()))
    anslist = []
    for i in permutations(operands):
        # permutations으로 계산
        ans = numbers[0]
        for j in range(len(operands)):
            if i[j] == 0: # +면
                ans = ans+numbers[j+1]
            elif i[j] == 1: # -면
                ans = ans - numbers[j+1]
            elif i[j] == 2: # *면
                ans = ans * numbers[j+1]
            else:
                ans = ans // numbers[j+1]
        # 다 계산하고 난 값
        anslist.append(ans)
    print("#%d %d" %(tc, max(anslist) - min(anslist)))
"""