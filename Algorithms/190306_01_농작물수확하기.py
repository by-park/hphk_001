"""
농작물 수확하기

[문제]
N X N크기의 농장이 있다.
이 농장에는 이상한 규칙이 있다.
규칙은 다음과 같다.
   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.
3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.
5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.
농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.

[제약 사항]
농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
농작물의 가치는 0~5이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

2019.03.06 PBY 최초작성
"""
import sys
sys.stdin = open('C:/Users/student/Documents/week2/day1/Algorithms/190306_01_input.txt','r')
T = int(input())
for tc in range(T):
    N = int(input())
    bat = []
    for _ in range(N):
        bat.append(input())

    income = 0
    for i in range(N//2):
        # 인덱스 있는 값 숫자로 바꿔서 더해야함
        for j in range(N//2 - i, N//2-i + (i+1)*2-1):
            income += int(bat[i][j])
#        income += sum(bat[i][N//2 - i:N//2-i + (i+1)*2-1])

    # 가운데 거 더해주고
    for j in range(N):
        income += int(bat[N//2][j])
#    income += sum(bat[N//2])

    # 끝에까지 더해주기
    for i in range(N//2+1,N):
        for j in range(i-N//2, i-N//2 + (N-i)*2-1):
            income += int(bat[i][j])
#        income += sum(bat[i][i-N//2 : i-N//2 + (N-i)*2-1])

    print('#%d %d' %(tc+1,income))