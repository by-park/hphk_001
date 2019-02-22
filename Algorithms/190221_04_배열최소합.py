"""
4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
문제 내용
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.
이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

최초 작성 2019.02.21 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190221_04_input.txt", "r")

# 재귀 버전 코드 - return 값은 없으나 전역변수 minvalue를 건드린다.
def nextsum(rows, array_index, acc):
    global minvalue
    global table

    # array_index 가 마지막 줄에 도달하면 더이상 재귀를 호출하지 않음
    if array_index == N:
        # 마지막 줄에 도달하면 minvalue 보다 큰지 확인한다.
        if acc < minvalue:
            minvalue = acc
        return True

    # 다음 갈 수 있는 경로를 확인한다 - (1) 가지치기를 위해 acc가 miinvalue보다 작은 경우만 들어갔다.
    if acc < minvalue:
        # (2) 또 다른 가지치기 방법으로 이전에 간 경로를 가지 않게 하기 위해 확인했다.
        for row in range(N):
            if rows[row] == 0: # 이전에 안 간 경로인 경우만
                candidates = rows[:] # rows[row]로 바꾸면 이전 단계가 항상 선택되어버리니까 임시 변수 활용
                candidates[row] = 1
                nextsum(candidates, array_index+1, acc+table[array_index][row])


if __name__ == "__main__":
    testcase = int(input())
    for tc in range(testcase):
        # input
        N = int(input())
        table = []
        for _ in range(N):
            table.append(list(map(int, input().split())))

        # 이전에 이미 잡힌 column을 표시하기 위한 배열 - 가지치기용
        rows = [0] * N

        # minvalue 최초 값 - 대각선의 합
        minvalue = 0
        for n in range(N):
                minvalue += table[n][n]

        # minvalue 업데이트를 위한 재귀 함수 호출
        nextsum(rows, 0, 0)

        # output
        print("#{} {}".format(tc+1, minvalue))


"""
다음 코드도 아직 안 돌아감 마지막 줄에서 이전 줄로 돌아가서 백트래킹 하는 부분 로직이 약함

testcase = int(input())
for tc in range(testcase):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))

    # 매 상태를 저장할 스택을 가지고 있음
    stack = [0] * N * N
    top = -1
    visited = [[0 for _ in range(N)] for __ in range(N)]


    # minvalue 최초 값 - 대각선의 합
    minvalue = 0
    for n in range(N):
            minvalue += table[n][n]

    for col in range(N):
        rows = [0] * N
        top = 0
        stack[top] = (col, 0)
        visited[stack[top][0]][stack[top][1]] = 1 # 방문 체크!
        rows[col] = 1

        while top > -1:
            if check == 0 and stack[top][1] < N-1: # 마지막 줄이 아니면
                for row in range(N): # 다음 가능한 경로를 탐색
                    if visited[row][stack[top][1] + 1] == 0 and not rows[row]:  # 방문 안 했으면
                        visited[row][stack[top][1] + 1] = 1  # 체크하고
                        rows[row] += 1
                        # stack에 넣고
                        top += 1
                        stack[top] = (row, stack[top - 1][1] + 1)
                        break
                else: # 가능한 모든 경로 탐색했으면 # break 못했으면 이전으로 돌아가야한다.
                    for row in range(N):
                        visited[row][stack[top][1] + 1] = 0
                        rows[row] -= 1
                    top -= 1
            else: # 내가 마지막 줄이면 이전으로 돌아가야한다. 더 이상 갈 곳이 없음
                temp = 0
                for stackid in range(top + 1):
                    temp += table[stack[stackid][0]][stack[stackid][1]]
                if temp < minvalue:
                    minvalue = temp
                for row in range(1, N):
                    visited[row][stack[top][1]] = 0
                    rows[row] -= 1
                top -= 2
    print(minvalue)
"""

# 그냥 2칸 전으로 가게 만드는게 아니라
# 바로 직전칸의 다음 길로 가게 만들어야한다.

"""
이게 돌아가는 코드가 아니긴 한데,
한줄에서 하나, 세로에서 하나 이거를 못 봤다.
N Queen 문제라고 생각하고 다시 풀어야한다.

testcase = int(input())
for tc in range(testcase):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))

    # 매 상태를 저장할 스택을 가지고 있음
    stack = [0] * N * N
    top = -1
    visited = [[0 for _ in range(N)] for __ in range(N)]

    # minvalue initialize
    minvalue = sum(table[0][:])

    # 첫 스택 넣어줌 - 시작점들 지정
    for firstcolumn in range(N):
        top += 1
        stack[top] = (firstcolumn, 0) # (0,0)
        visited[firstcolumn][0] = 1

        # 다음 자식 노드를 생성
        while top > -1:
            if stack[top][1] < N-1: # 마지막 단계까지 오기 전까지 N-1이면 딱 마지막 열
                for row in range(N):
                    if visited[row][stack[top][1]+1] == 0: # 방문 안 했으면
                        visited[row][stack[top][1]+1] = 1 #체크하고
                        # stack에 넣고
                        top += 1
                        stack[top] = (row, stack[top-1][1]+1)
                        break
                else: # 다 방문해서 갈 곳이 없으면
                    for row in range(N):
                        visited[row][stack[top][1]] = 0
                    top -= 2  # pop 구현 두 칸 뒤로 가는 이유는 자식 노드를 뱉은 애 말 고 다른 애를 골라야하니까
            else: # 마지막 단계면
                temp = 0
                for stackid in range(top+1):
                    temp += table[stack[stackid][0]][stack[stackid][1]]
                if temp < minvalue:
                    minvalue = temp
                # 마지막 단계니까 이전 노드로 다시 이동
                top -= 1

        print(minvalue)
"""

