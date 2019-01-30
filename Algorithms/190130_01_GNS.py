""" 
[S/W 문제해결 기본] 5일차 - GNS
문제 내용
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]
입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.

최초 작성 2019.01.30 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190130_01_input.txt", "r")

code = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
testcase = int(input())
for tc in range(1, testcase+1):
    nrow = input()
    s = input()
    print("#%d" %tc)
    ans = ''
    for i in range(len(code)):
        ans += (code[i] + ' ')*s.count(code[i])
    print(ans)

"""
code = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
testcase = int(input())
for tc in range(testcase):

    # input
    nrow = input() #1 7041
    s = input().split()

    # 각 문자가 등장한 개수 세기
    stoi = [0 for _ in range(10)]
    for word in s:
        for c in range(len(code)):
            if word == code[c]:
                stoi[c] += 1

    # 출력
    ans = ''
    for idx in range(len(stoi)):
        ans += (code[idx] + ' ')*stoi[idx]
    print('#{}'.format(tc+1))
    print(ans)
"""

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
