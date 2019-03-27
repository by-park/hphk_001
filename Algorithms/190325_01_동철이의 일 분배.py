"""
03/25 Solving Club 문제 동철이의 일 분배

2019.03.27 PBY 최초작성
"""

def findProb(curprob, n): # n번째 사람
    global N, maxvalue
    if curprob == 0:
        return # 그런 경우는 버려도 될 듯
    if n == N: # 0, 1, 2면 3이 되는 순간 출력하기
        if maxvalue < curprob:
            maxvalue = curprob
        return
    for i in range(N):
        if used[i]: continue
        arr[n] = i # 그 사람이 이 일을 선택하고
        used[i] = True
        if curprob*0.01*(jobs[n][i]) >= maxvalue: # 이미 작으면 다음에는 더 작아질 수 밖에 없다.
            findProb(curprob*0.01*(jobs[n][i]), n+1) # 내 다음 사람을 넘겨줌...
        used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))
    arr = [0]*N # 각각 몇 번째 일 하는지 저장
    used = [False]*N # 순열이 사용되었는지 알아야함
    maxvalue = 0
    for start in range(N): # 몇 번째 일인지 돌면서
        arr[0] = start
        used[start]=True
        findProb(jobs[0][start]*0.01, 1) # 0번째 사람부터 시작
        used[start]=False

    print("#%d %.6f" %(tc, round(maxvalue*100, 6)))
       

"""
# 15개 permutation 뽑는게 이미 너무 오래 걸린다....
from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))

    # 각 순열 별로 성공할 확률
    maxvalue = 0 # 0%로 초기화
    for i in permutations(range(N)): # 이걸 3이라고 잘못 써서 ㅠㅠ 3번째 케이스 1개 짜리 바로 틀렸다 
        p = 0
        pro = 1 # 확률 곱해야하니까 1로 초기화
        for j in i: # 순열을 돌면서 첫 번째 사람은 j 번째 일, 두번째 사람은 다음 j+1번째 일...
            pro *= (jobs[p][j]*0.01)
            p += 1
        if pro > maxvalue:
            maxvalue = pro
    print("#%d %f" %(tc, round(maxvalue*100, 6)))
"""
