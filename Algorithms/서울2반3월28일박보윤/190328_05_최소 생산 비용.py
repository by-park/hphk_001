def perm(people, N, cur_sum):
    global mincosts
    if cur_sum > mincosts: # 가지치기
        return
    if people >= N: # 종료 조건
        if cur_sum < mincosts:
            mincosts = cur_sum
        return

    for i in range(N):
        if used[i] == False: # 아직 사용 안한 일이면
            used[i] = True
            perm(people+1, N, cur_sum+costA[people][i])
            used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mincosts = 99*N*N
    costA = []
    for _ in range(N):
        costA.append(list(map(int, input().split())))
    used = [False] * N # 각 일이 선택되었는지
    # 순열 들어가기
    for i in range(N): # 첫 번째 사람한테 무슨 일을 맡길 건지
        used[i] = True
        perm(1, N, costA[0][i])
        used[i] = False
    print("#%d %d" %(tc, mincosts))


            
