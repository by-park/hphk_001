"""
그룹 나누기
"""
def make_set(x):
    joe[x] = x
def find_set(x):
    if x == joe[x]:
        return x
    else:
        return find_set(joe[x])
def union(x, y):
    joe[find_set(y)] = find_set(x)
    
for test_case in range(int(input())):
    N, M = map(int, input().split())
    team_request = list(map(int, input().split()))
    joe = [0] * N
    for i in range(N):
        make_set(i)
    # 팀 신청서를 돌면서 union 시키기
    for i in range(M):
        union(team_request[i*2]-1, team_request[i*2+1]-1)
    # 한번에 모든 신청서가 다 union되지 않는다.
    for i in range(N):
        joe[i] = find_set(i)

    print("#%d %d" %(test_case+1, len(set(joe))))
