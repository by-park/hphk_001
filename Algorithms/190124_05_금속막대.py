""" 
[S/W 문제해결 응용] 7일차 - 금속막대
원형 금속 막대를 가장 길게 연결하고자 한다. 원형 금속 막대는 한 쪽 면에 수나사와 다른 쪽에 암나사로 이루어져 있다.
수나사와 암나사는 굵기가 서로 다르다. 아래 그림에서 수나사의 굵기는 3을 암나사의 굵기는 4를 나타내고 있다.
이후 나사의 굵기를 수나사의 굵기 x 암나사의 굵기로 표현한다. 연결은 +로 표현한다.
이와 같은 원형 금속 막대를 연결하기 위해서는 수나사의 굵기와 암나사의 굵기가 서로 일치해야 한다.
예를 들어 두 개의 원형 금속 막대 3x4와 4x5가 있을 때 3x4+4x5로 연결해야 연결되며 4x5+3x4로 연결하면 연결되지 않는다.

[입력]
맨 첫 줄에는 테스트 케이스의 개수가 주어진다.
그리고 테스트 케이스가 각 라인에 주어진다. 각 테스트 케이스는 2줄로 구성되며, 첫 줄에는 원형 금속 막대의 개수 n이 주어지고, 다음 줄에는 2n개의 수가 주어진다.
숫자는 공백으로 구분한다. 앞에서부터 2개씩 하나의 원형 금속 막대의 수나사 굵기와 암나사 굵기를 의미한다.

[출력]
각 테스트 케이스 각각에 대한 답을 출력한다.
각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 수열로부터 가장 많이 연결하기 위한 원형 금속 막대의 수나사 굵기와 암나사 굵기를 순서대로 출력한다.

최초 작성 2019.01.24 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190124_05_input.txt", "r")
"""
testcase = int(input())
for tc in range(testcase):
    num = int(input())
    ary = list(map(int, input().split()))
    a, s = [], []

    # 암수 리스트 업데이트
    for i in range(0, len(ary), 2):
        a.append(ary[i])
        s.append(ary[i+1])

    # 진행 방향 1 앞으로 2 뒤로
    stat = 1
    cur = a[0]
    ans = []
    fcheck = 0
    while len(ans) != len(ary):
        for j in range(len(a)):
            if stat == 1:
                # 앞으로 갈 때는 암에서 찾아서 수에 있는 수를
                if cur == a[j]:
                    ans.extend([a[j], s[j]])
                    cur = s[j]
                # for문 다 돌았는데, 뒤에 수가 없으면 방향 전환
                if fcheck > len(a):
                    stat = 2
                    cur = ans[0]
            elif stat == 2 and cur == s[j]:
                # 뒤에서 갈 때는 수에서 찾아서 암에 있는 수를
                ans = [a[j], s[j]] + ans
                cur = a[j]
        fcheck += 1

    print("#%d" % (tc+1), ' '.join(map(str, ans)))
"""
# 선생님 코드
TC = int(input())
for tc in range (1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        found = False
        for j in range(N):
            if arr[i * 2] == arr[j * 2 + 1] :
                found = True
                break
        if found == False:
            start_position = i
            break

    arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]
    arr[1], arr[start_position * 2 + 1] = arr[start_position * 2 + 1], arr[1]

    for i in range(1, N - 1):
        for j in range(i, N):
            if arr[i * 2 - 1] == arr[j * 2]:
                arr[i * 2], arr[j * 2] = arr[j * 2], arr[i * 2]
                arr[i * 2 + 1], arr[j * 2 + 1] = arr[j * 2 + 1], arr[i * 2 + 1]
                break

    print("#%d "%tc, end=' ')
    for i in range(N*2):
        print("%d "%arr[i], end=' ')
    print()

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
