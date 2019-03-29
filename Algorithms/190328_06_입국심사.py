
# 가지 수가 너무 많은데, 그리디하게 짜도 되나?
# => 안됨 이 문제는 이분탐색 문제

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
