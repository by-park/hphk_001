""" 
4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


최초 작성 2019.01.24 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190124_02_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    N, K = list(map(int, input().split()))

    # 모든 부분집합의 합을 다 저장하기 - 비트 연산
    arr = list(range(1, 13))  # 1~12
    n = len(arr)
    tlist = []
    for i in range(1 << n):  # 2의 12승
        sum_, cnt = 0, 0
        for j in range(n):  # 전체 원소의 수 12만큼 비트를 비교한다.
            if i & (1<<j):
                sum_ += arr[j]
                cnt += 1
        tlist.append([cnt, sum_])

    # 부분집합의 n과 k를 검사
    ans = 0
    for i in range(len(tlist)):
        if tlist[i][0] == N and tlist[i][1] == K:
            ans += 1

    print("#%d %d" % (tc+1, ans))

# 선생님 코드
TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1<<12):
        bitCnt = sum = 0
        for j in range(12):
            if i & (1<<j):
                sum += (j+1) # j+1 은 1부터 12가 된다.
                bitCnt += 1 # 어떤 놈이 선택이 되면 선택 되었다고 표시
        if sum == K and bitCnt == N: #합이 K, 선택된 원소 개수가 N개면
            cnt += 1 # 카운팅 추가

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
