"""
1931 회의실 배정

2019.03.26

2
2 2
1 2
답 2

3
7 7
7 8
8 8

답 3

https://www.acmicpc.net/board/view/6569
아래 예시가 신의 한수였다....
6 
1 3
3 100
4 5
6 6
5 6
7 7

답 5

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

답 4
"""

"""
# 선생님 코드
res = []
time = [[0]*2]*T
for i in range(T):
    time[i] = [inp[i*2+1], inp[i*2]]
time.sort() # 제일 앞 거 기준, 그 다음 기준으로 정렬이 된다!!!!!
cnt = 0
res.append([time[0][1], time[0][0]])
for i in range(1, T):
    if res[cnt][1] <= time[i][1]:
# 퀵소트
def sort_time(start, end):
    left = start
    # ...
"""

# 시간초과를 이기려면 sort 한 번에 끝내야할 것 같다.
# 두번째 기준으로 정렬해놓고, 지금 시간보다 다음 시간이면 바로 선택하도록 => 문제 있을 것
# 1 2
# 2 2 이거 찾으려면 첫 스타트 뿐 아니라 매번 두번째도 정렬을 해야한다.

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda meetings: (meetings[:][1], meetings[:][0]))

# 첫 회의
minvalue = meetings[0][1] # 무조건 이 회의 부터 시작함
cnt = 1
nextidx = 0

# 그 다음 회의를 찾음
while nextidx < N: # 이 방향 자꾸 실수함...
    
    for i in range(nextidx+1, N):
        # 시작 시간이 이전 회의보다 끝난 시간이 아니면 선택하면 안 됨
        if meetings[i][1] == meetings[i][0] == minvalue:
            cnt += 1
        elif meetings[i][1] >= minvalue and meetings[i][0] >= minvalue: # 겹치는 걸 한 번 더 구함 ㅠㅠㅠㅠㅠ 바보 ㅠㅠㅠㅠ
            nextidx = i
            break
    else:
        # 끝까지 다 봤다는 건 거기까지 같은 minvalue였다는 것
        break

    # 다음 minvalue는
    minvalue = meetings[nextidx][1]
    cnt += 1 # 다음 회의 찾아옴
        
print(cnt)

"""
arr = sorted(arr, key=lambda x: x[1], x[0])
idx = 0
cnt = 1
while True:
    a = arr[idx]
    for i in range(idx+1, N):
        if a[1] <= arr[i][0]:
            cnt += 1
            idx = i
            break
    else:
        print(cnt)
        break
"""

"""
# 시간초과
N = int(input())
meetings = []
minidx = 0
minvalue = 2**31
for _ in range(N):
    meeting = list(map(int, input().split()))
    meetings.append(meeting)
    if meeting[1] < minvalue:
        minvalue = meeting[1]
        minidx = _

# 그리디로 가장 일찍 끝나는 애를 찾는다.
#minidx
cnt = 1
meetings.pop(minidx)

i = 0
while meetings:
    preminvalue = minvalue
    minvalue = 2**31
    flag = 0
    for j in range(len(meetings)):
        if meetings[j][1] < minvalue and meetings[j][0] >= preminvalue:
            minvalue = meetings[j][1]
            minidx = j
            flag = 1
    if flag == 0:
        break # 배정할 수 있는 회의가 없어서 while문 탈출
    # minvalue를 찾았으면
    cnt += 1
    meetings.pop(minidx)
    # minvalue 다음 시간이면서 가장 빨리 끝나는 애

print(cnt)
"""
