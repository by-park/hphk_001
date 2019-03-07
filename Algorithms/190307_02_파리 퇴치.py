"""
파리 퇴치

2019.03.07 PBY 최초작성
"""

T = int(input())
for tc in range(T):
    arraysize, parisize = list(map(int, input().split()))
    array = []
    for _ in range(arraysize):
        array.append(list(map(int, input().split())))

    # 시작점 정하기
    maxvalue = 0
    for i in range(arraysize-parisize+1):
        for j in range(arraysize-parisize+1):
            squaresum = 0
            # 시작점 부터 M x M 구하기
            for i2 in range(parisize):
                for j2 in range(parisize):
                    squaresum += array[i+i2][j+j2]

            # max값 구해진 건지 확인
            if squaresum > maxvalue:
                maxvalue = squaresum

    print("#%d %d" %(tc+1, maxvalue))
