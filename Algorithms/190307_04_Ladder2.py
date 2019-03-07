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