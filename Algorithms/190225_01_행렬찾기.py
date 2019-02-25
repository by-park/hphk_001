"""
[S/W 문제해결 응용] 7일차 - 행렬찾기
문제 내용
유엔 화학 무기 조사단이 대량 살상 화학 무기를 만들기 위해 화학 물질들이 저장된 창고를 조사하게 되었다.
창고에는 화학 물질 용기 n2개가 n x n으로 배열되어 있었다.
유엔 조사단은 각 용기를 조사하여 2차원 배열에 그 정보를 저장하였다.
빈 용기에 해당하는 원소는 ‘0’으로 저장하고, 화학 물질이 들어 있는 용기에 해당하는 용기는 화학 물질의 종류에 따라 ‘1’에서 ‘9’사이의 정수를 저장하였다.
다음 그림은 창고의 화학 물질 현황을 9x9 배열에 저장한 예를 보여준다.카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는
유엔 조사단은 화학 물질이 담긴 용기들로부터 3가지 사항을 발견하였다.
1. 화학 물질이 담긴 용기들이 사각형을 이루고 있다. 또한, 사각형 내부에는 빈 용기가 없다.
예를 들어, 위의 그림에는 3개의 화학 물질이 담긴 용기들로 이루어진 사각형 A, B, C가 있다.
2. 화학 물질이 담긴 용기들로 이루어진 사각형들은 각각 차원(가로의 용기 수 x 세로의 용기 수)이 다르다.
예를 들어, 위의 그림에서 A는 3x4, B는 2x3, C는 4x5이다.
3. 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다.
예를 들어, 위의 그림에서 A와 B 사이와 B와 C 사이를 보면, 빈 용기를 나타내는 ‘0’ 원소들이 2개의 사각형 사이에 있는 것을 알 수 있다.
단, A와 C의 경우와 같이 대각선 상으로는 빈 용기가 없을 수도 있다.
유엔 조사단은 창고의 용기들에 대한 2차원 배열에서 행렬(화학 물질이 든 용기들로 이루어진 사각형)들을 찾아내고 정보를 수집하고자 한다.
찾아낸 행렬들의 정보를 출력하는 프로그램을 작성하시오.

[입력]
맨 첫 줄에는 테스트 케이스의 개수가 주어진다.
그리고 테스트 케이스가 각 라인에 주어진다.
각 테스트 케이스는 (n+1) 줄로 구성되며, 첫 줄에는 양의 정수인 n이 주어지고, 다음 n줄에는 n x n 행렬이 (각 행이 한 줄에) 주어진다.


[출력]
각 테스트 케이스 각각에 대한 답을 출력한다.
각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 행렬에서 추출된 부분 행렬들을 개수와 그 뒤를 이어 행렬들의 행과 열의 크기를 출력한다.
크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력한다.
예를 들어 3x4 행렬의 크기는 3*4 = 12 이다.
크기가 같을 경우 행이 작은 순으로 출력한다.
예를 들어 12x4, 8x6 두 개의 행렬은 같은 크기이고 행은 각각 12, 8 이므로 8 6 12 4 순으로 출력한다.

최초 작성 2019.02.25 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190225_01_input.txt", "r")

testcase = int(input())

for tc in range(testcase):
    # input
    n = int(input())
    array = [[] for _ in range(n)]
    for row in range(n):
        array[row] = list(map(int, input().split()))

    # 사각형들의 행과 열을 저장할 배열
    ans = []

    # 모든 셀이 0이 될 때까지 진행
    check = 0
    while check == 0:
        # 매번 새롭게 돌면서
        for i in range(n):
            for j in range(n):
                # 용기를 하나 만나면 오른쪽 끝과 아래 끝을 찾아감
                if array[i][j] > 0:
                    # 상하 방면
                    iindex = i
                    while iindex < n+1 and array[iindex][j]:
                        iindex += 1
                    # 좌우 방면
                    jindex = j
                    while jindex < n+1 and array[i][jindex]:
                        jindex += 1

                    # 찾은 영역을 다 0으로 바꾸기
                    for i2 in range(i, iindex):
                        for j2 in range(j, jindex):
                            array[i2][j2] = 0
                    # 사각형의 끝 좌표들을 저장함
                    ans.append([iindex-i, jindex-j])

                # 더 이상 찾을 수 있는 셀이 없으면 종료
                elif i == n-1 and j == n-1:
                    check = 1
                    break
        if check == 1:
            break

    print('#{} {}'.format(tc+1, len(ans)), end=" ")

    # 버블 정렬
    for i in range(len(ans)):
        for j in range(0, len(ans)-1-i):
            # 행과 열을 곱한 값이 작고,
            if (ans[j][0] * ans[j][1]) > (ans[j+1][0] * ans[j+1][1]):
                j1backup = ans[j+1][:]
                jbackup = ans[j][:]
                ans[j], ans[j+1] = j1backup, jbackup

            # 행이 작은 순서대로
            elif (ans[j][0] * ans[j][1]) == (ans[j+1][0] * ans[j+1][1]):
                if ans[j][0] > ans[j+1][0]:
                    j1backup = ans[j + 1][:]
                    jbackup = ans[j][:]
                    ans[j], ans[j + 1] = j1backup, jbackup

    # 정렬 결과대로 출력
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            print(ans[i][j], end=" ")
    print()


# 계속 틀렸던 이유는 break 조건을 잘못 설정해서
# for j in 여기서 설정하는 바람에 옆으로 더이상 탐색하지 않고 끝내서
# 일부 케이스를 찾지 못하는 경우가 발생했다.