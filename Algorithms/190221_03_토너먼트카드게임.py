"""
4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
문제 내용
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.
두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.
다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.
#1 3
#2 5
#3 1

최초 작성 2019.02.21 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190221_03_input.txt", "r")


# 분할 정복 함수
def DC(array_students):

    # 가장 아래로 내려가서 올라올 때마다 학생이 2명씩 묶인다.
    if len(array_students) == 2:

        # 가위 바위로 로직 구현 (return = 이긴 카드, 학생 넘버)
        if array_students[0][0] == "1":
            if array_students[1][0] == "1" or array_students[1][0] == "3":
                return ("1", array_students[0][1])
            else:
                return ("2", array_students[1][1])
        elif array_students[0][0] == "2":
            if array_students[1][0] == "2" or array_students[1][0] == "1":
                return ("2", array_students[0][1])
            else:
                return("3", array_students[1][1])
        else:
            if array_students[1][0] == "3" or array_students[1][0] == "2":
                return ("3", array_students[0][1])
            else:
                return ("1", array_students[1][1])

    # 그룹에 한 명밖에 없는 경우 자기 자신을 출력
    elif len(array_students) == 1:
        return (array_students[0][0], array_students[0][1])

    # 2명 이상인 경우 2명씩 다시 쪼개줘야한다.
    else:
        # index = 전체 배열을 절반으로 나눌 기준
        index = len(array_students)
        # 절반으로 나뉜 배열의 답이 오면 그걸 기준으로 또 2명으로 묶어서 다시 분할 정복을 시킴)
        return DC([DC(array_students[:index//2 + index%2]), DC(array_students[index//2+index%2:])])


if __name__ == "__main__":
    testcase = int(input())
    for tc in range(testcase):
        # input
        N = int(input())
        cards = input().split()

        # student number 생성
        students = [i + 1 for i in range(N)]

        # 주어진 데이터를 분할 정복 함수에 넣음
        ans = DC(list(zip(cards, students)))

        # output
        print("#{} {}".format(tc+1, ans[1]))


# 계속 오류났던 이유
# (2,1) 이런 식으로 안 묶고 (1, 2) 이런 식으로 묶이는 경우가 있었다!
# 함수 내에서 student_array를 print해보면 그것을 확인할 수 있고,
# //2 뿐만 아니라 %2를 추가함으로써 내가 원하는 인덱스로 잘리도록 할 수 있었다.

"""
max_depth를 활용하려고 했는데, 리턴하면서 올라오게 할 방법을 찾아서 필요가 없어졌다.

    # max_depth
    #for i in range(N):
    #    if 2**i > N:
    #        max_depth = i-1
    #k = 1
"""

"""
# 왜 그냥 토너먼트로 가면 안 되지? => //2 이렇게 나눠가야 하는데 나는 무조건 전체의 마지막을 부전승으로 올렸다.

testcase = int(input())
for tc in range(testcase):
    N = int(input())
    cards = input().split()
    student_list = [i+1 for i in range(N)]
    student_n = N

    # 처음 2 명씩 비교해서 넣는다.
    while len(student_list) > 1: # 마지막 한 명이 남으면 나오도록
        newstudent_list = []
        for idx in range(1,student_n, 2):
            # 두 개씩 비교
            if cards[student_list[idx]-1] == "1": # student 이름을 +1해서 넣어서 -1해야함
                if cards[student_list[idx-1]-1] == "1" or cards[student_list[idx-1]-1] == "2":
                    # 같으면 숫자가 적은 애가 이김 혹은 바위로 이김
                    newstudent_list.append(student_list[idx-1])
                else:
                    # 보로 짐
                    newstudent_list.append(student_list[idx])
            elif cards[student_list[idx]-1] == "2":
                if cards[student_list[idx-1]-1] == "2" or cards[student_list[idx-1]-1] == "3":
                    newstudent_list.append(student_list[idx-1])
                else:
                    newstudent_list.append(student_list[idx])
            else:
                if cards[student_list[idx-1]-1] == "3" or cards[student_list[idx-1]-1] == "1":
                    newstudent_list.append(student_list[idx-1])
                else:
                    newstudent_list.append(student_list[idx])

        # 홀수면 마지막에 추가해줌
        if student_n % 2 != 0:
            newstudent_list.append(student_list[-1])

        # student list 업데이트
        student_list = newstudent_list[:]
        student_n = len(student_list)

    print("#{} {}".format(tc+1,student_list[0]))
"""
