"""
03/27 Solving Club 장훈이의 높은 선반

2019.03.27 PBY 최초작성
"""

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    workers = list(map(int, input().split()))
    minvalue = sum(workers)
    # 점원들로 탑 만들기 => 뽑고 안 뽑고를 선택
    for i in range(1<<N):
        ans = 0
        for j in range(N):
            if i & (1<<j):
                ans += workers[j] # 지금 점원들로 탑을 만들 었을 때
        if ans == B: # 꽃몬님 방법. 이미 더 탑을 쌓을 필요가 없음. 10번 케이스 빨라짐.
            minvalue = ans
            break
        elif ans < B:
            continue
        elif ans > B:
            if minvalue > ans:
                minvalue = ans
        
        
    print("#%d %d" %(tc, minvalue-B))
