"""
의석이의 세로로 말해요

2019.03.07 PBY 최초작성
"""

T = int(input())

for tc in range(1, T+1):
    array = []
    for _ in range(5):
        cur_input = input()
        array.append(cur_input + '-'*(15-len(cur_input)))

    # input 채운 후에 세로로 읽기
    ans = ''
    for j in range(15):
        for i in range(5):
            if array[i][j] != '-':
                ans += array[i][j]

    print("#%d %s" %(tc, ans))