
# 가지 수가 너무 많은데, 그리디하게 짜도 되나?
# => 안됨 이 문제는 이분탐색 문제

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tks = []
    for _ in range(N):
        tks.append(int(input()))
    left = 0
    right = min(tks)*M # 최소의 시간으로 M명이 다 서는 경우
    people = 0
    # 이진 탐색
    while True:
        middle = (left+right)//2
        temppeople = people
        # tks를 돌면서 지금 시간 안에 몇 명이 들어오는지
        people = 0
        for tk in tks:
            people += middle // tk # 이 시간 안에 몇 명을 할 수 있는지
        if left > right: # 무한루프에 빠지면 left가 더 커지고, right와 middle이 계속 같다.
            ans = middle + 1
            break
#        if temppeople == people: # 계속 무한루프에 빠지면... => 틀렸습니다.
#            ans = middle + 1 # 좌우를 반복하는 중이니까 탈
#            break
        #if people == M: => 틀렸습니다.
        #    ans = middle
        #    break
        if people >= M:
            right = middle-1
        elif people < M:
            left = middle+1
    print("#%d %d" %(tc, ans))

# 입국심사
"""
# 시간초과
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tks = []
    for _ in range(N):
        tks.append(int(input()))
    left = 0
    right = min(tks)*M # 최소의 시간으로 M명이 다 서는 경우
    people = 0
    # 이진 탐색
    while True:
        middle = (left+right)//2
        temppeople = people
        # tks를 돌면서 지금 시간 안에 몇 명이 들어오는지
        people = 0
        for tk in tks:
            people += middle // tk # 이 시간 안에 몇 명을 할 수 있는지
        if temppeople == people: # 계속 무한루프에 빠지면...
            ans = middle + 1 # 좌우를 반복하는 중이니까 탈
            break
        # 완전히 내가 원하는 명수에 멈추지 않을 수도 있다! == 으로 체크하면 안 됨
        if people == M: # 내가 원하는 명수를 찾았으면
            while people == M:
                middle -= 1
                people = 0
                for tk in tks:
                    people += middle // tk
                # 새로 갱신된 people이 작으면 while을 나가게 된다.
            ans = middle+1
            break
        elif people >= M:
            right = middle-1 # 좌우를 잘못 생각해서 left, right식을 바꿔썼다...
        elif people < M:
            left = middle+1

    print("#%d %d" %(tc, ans))
"""

"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tks = []
    minvalue = 10**9*N
    for _ in range(N):
        tks.append(int(input()))
    remainingtime = [0] * M # 입국 심사대 기다릴 필요 없음
    for i in range(N): #각 사람 마다 매번 그리디하게
        # 최소값을 찾아서 가서 줄을 선다.
        # 기다려야하면, 몇 초나 기다릴 지, 기다린 후에 다른 애들 값 바꿔주기
        # 내가 기다리면 어차피 내 뒷사람도 못들어감
        
        tk, timedelay = findMintk()
        for t in range(M):
            if tks[t] <= timedelay:
                tks[t] = 0 # 빈 심사대
            else:
                tks[t] -= timedelay # 남은 시간
        # 나는 어디 서는거지
        tks[t] += tk # 내가 선 만큼 대기 시간 늘어남
        
    print("#%d %d" %(tc, 1))
"""
