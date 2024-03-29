""" 
[S/W 문제해결 기본] 1일차 - Flatten

[문제 내용]
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.
A’부분의 상자를 옮겨서, C부분에 덤프하였다. 이때 C 대신 C’부분에 덤프해도 무방하다.
2회의 덤프 후, 최고점과 최저점의 차이는 8 – 2 = 6 이 되었다 (최초덤프 이전에는 9 – 1 = 8 이었다).
덤프 횟수가 2회로 제한된다면, 이 예시 문제의 정답은 6이 된다.

[제약사항]
가로 길이는 항상 100으로 주어진다.
모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
덤프 횟수는 1이상 1000이하로 주어진다.
주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

[입력]
총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.
최초 작성 2019.01.17 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190117_05_input.txt", "r")

# 먼저 min, max를 사용해서 풀이

for i in range(1, 11):
    
    # input
    dump = int(input())
    blocks = list(map(int, input().split()))

    for j in range(dump):
        maxindex = blocks.index(max(blocks))
        minindex = blocks.index(min(blocks))
        if blocks[maxindex] - blocks[minindex] <= 1:
            print("#{} {}".format(i, blocks[maxindex] - blocks[minindex]))
            break
        blocks[maxindex] -= 1
        blocks[minindex] += 1

    maxindex = blocks.index(max(blocks))
    minindex = blocks.index(min(blocks))    
    print("#{} {}".format(i, blocks[maxindex] - blocks[minindex]))

# 한동훈님 코드 일부
for test in range(testcase):
    n = int(input())
    li = list(map(int, input().split()))
    N = 0
    while N!=n:
        N+=1
        li[li.index(my_max[li])] = my_max(li) -1
        li[li.index(my_min[li])] = my_min(li) +1
    print(f'#{test+1} {my_max(li) - my_min(li)}')

# 선생님 코드
    for i in range(dump_cnt):
        maxI, minI = find_minmax()
        box_height[maxI] -= 1
        box_height[minI] += 1

    # 덤프 끝난 후에 바로 차이를 빼면 테스트 케이스 중 반만 맞는다.
    maxI, minI = find_minmax()

    print("#%d" % tc, box_heights[maxI] - box_heights[minI])
# 1차 시도 실패 이유
# 마지막에 min +1이 되었기 때문에 더이상 아까의 min이 최솟값이 아닐 수 있다.
# max도 마찬가지 그래서 마지막에 한 번 더 찾아줘야 한다.
    
# max 인덱스를 뽑는 방법
# https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
# 외부 라이브러리
# values.index라는 방법
# for 문으로 찾는 방법
# max index 뽑을 때 enumerate로 했는데 안 됐다 ㅠㅠㅠㅠ


# visual studio는 실행시 ctrl + f5
