"""
문제해결 응용 1일차 - 이진수2

최초작성 2019.03.21 PBY

입력)
3
0.625
0.1
0.125

출력)
#1 101
#2 overflow
#3 001
"""

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    arr = ''
    for i in range(2, 2+12+1):
        N *= 2
        arr += str(int(N))
        if N == 1:
            print("#%d %s" %(tc, arr))
            break
        N -= int(N)
    else: print("#%d overflow" %tc)
