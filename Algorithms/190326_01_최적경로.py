def permutation(k, n, curpath):
    global minvalue
    if curpath > minvalue: # 가지치기
        return
    if k >= n: # 종료 조건
        # 거기서 집 가는 길도 저장하고 minvalue인지 업데이트
        curpath += abs(perm[-1][0]-coordi[1][0])+abs(perm[-1][1]-coordi[1][1])
        if minvalue > curpath:
            minvalue = curpath
        return
    for i in range(n):
        if used[i] == False:
            used[i] = True
            perm[k] = coordi[2+i]
            permutation(k+1, n, curpath+abs(perm[k][0]-perm[k-1][0])+abs(perm[k][1]-perm[k-1][1]))
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    nCustomer = int(input())
    total_coordi = list(map(int, input().split()))
    coordi = []
    for j in range(0, (nCustomer+2)*2, 2):
        coordi.append([total_coordi[j], total_coordi[j+1]]) 
    minvalue = 200*(nCustomer+2)
    used = [False]*nCustomer # 그 집에 방문했는지 표시
    perm = [0] * nCustomer # 매 순서마다 방문한 집 좌표 넣어두기
    # 고객 방문
    for i in range(nCustomer): # 누구 먼저 방문
        used[i] = True # 그 집에 방문했다고 표시하고
        perm[0] = coordi[2+i] # 고객의 좌표값이 들어감
        permutation(1, nCustomer, abs(perm[0][0]-coordi[0][0])+abs(perm[0][1]-coordi[0][1])) # 첫번째 고객까지 걸린 경로 포함해서 넘김
        used[i] = False
    print("#%d %d" %(tc, minvalue))

"""
회사의 좌표가 항상 0,0 이라고 착각해서
test case 1번만 맞길래 왜 그런가 한참 찾았다....
"""
