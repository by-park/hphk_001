""" 
4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

최초 작성 2019.01.24 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190124_04_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    num = int(input())
    ary = list(map(int, input().split()))

    for sortnum in range(0, 5):

        if ary[2*sortnum] >= ary[2*sortnum+1]:
            maxI, minI = 2*sortnum, 2*sortnum+1
        else:
            maxI, minI = 2*sortnum+1, 2*sortnum

        # sort 정렬된 거 이후로 다시 돌면서
        for j in range(2*sortnum + 2, len(ary)):
            # 최댓값 비교
            if ary[j] > ary[maxI]:
                maxI = j
        ary[2 * sortnum], ary[maxI] = ary[maxI], ary[2 * sortnum]

        for j in range(2*sortnum + 2, len(ary)):
            # 최소값 비교
            if ary[j] < ary[minI]:
                minI = j
        if 2*sortnum+1 == len(ary)-1: continue # max 업데이트 후 min 업데이트를 한 번 더 하면 max, min자리가 바뀜
        ary[2 * sortnum + 1], ary[minI] = ary[minI], ary[2 * sortnum + 1]

    print("#%d" % (tc+1), ' '.join(map(str, ary[:10])))

# 10 개 중 9개 맞음 - max, min 업데이트가 두 번 일어나면서 자리 바뀜 현상
# - 해결 완료

# 선생님 코드
# 10 1 9 2 8 3 7 4 6 5
# 정렬 시킨 후에 앞에서 하나 뒤에서 하나 꺼냄

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(10):
        minI = maxI = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if nums[maxI] < nums[j] : maxI = j
            nums[i], nums[maxI] = nums[maxI], nums[i]
        else:
            for j in range(i + 1, N):
                if nums[minI] > nums[j] : minI = j
            nums[i], nums[minI] = nums[minI], nums[i]

    print("#%d"%tc, end=' ')
    for i in range(10) : print(nums[i], end=' ')
    print()

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
