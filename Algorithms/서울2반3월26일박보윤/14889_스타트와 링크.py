"""
14889 스타트와 링크
순열 연습

2019.03.26 PBY 최초작성

"""

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
teamnum = N//2    
minvalue = 100 * N * N
A = []
# 재귀로 들어가서 선택하기, 무조건 오름차순으로 해서!!! 조합 효과 내기!!!
#  pop으로 두 팀 나누기
def findTeam(a):
    global teamnum, N, minvalue
    
    if len(A) == teamnum: # 팀을 결성했으면
        # 점수 계산
        # B도 점수 계산
        Apower = 0
        for idx in range(teamnum):
            std = A[idx]
            for idx2 in range(teamnum):
                if idx == idx2:
                    continue
                other = A[idx2]
                Apower += arr[std][other]

        # B찾기?
        B = []
        for i in range(N):
            if i not in A: # 오래 걸리지 않으려나
                B.append(i)

        Bpower = 0
        for idx in range(teamnum):
            std = B[idx]
            for idx2 in range(teamnum):
                if idx == idx2:
                    continue
                other = B[idx2]
                Bpower += arr[std][other]

        if minvalue > abs(Apower-Bpower):
            minvalue = abs(Apower-Bpower)
        return            
    # 지금 사람 선택하고,
    # 다음 사람 고르기
    for n in range(a+1, N):
        A.append(n)
         # pop을 여러번 한다....
        findTeam(n)
        A.pop() # 전역변수니까 나올 때 다시 빼주기

for i in range(teamnum+1): # 오름차순으로 할 거라서 제한이 있음
    A.append(i)
    findTeam(i)
    A = []
print(minvalue)


"""
# 또 시간 초과

import itertools
for i in itertools.permutations(list(range(N))):
    # 앞에서 절반이 한 팀, 뒤에서 절반이 나머지 한 팀
    Apower = 0
    A = i[:N//2]; B =i[N//2:]
    for idx in range(N//2):
        std = A[idx]
        for idx2 in range(N//2):
            if idx == idx2:
                continue
            other = A[idx2]
            Apower += arr[std][other]
            
    Bpower = 0
    for idx in range(N//2):
        std = B[idx]
        for idx2 in range(N//2):
            if idx == idx2:
                continue
            other = B[idx2]
            Bpower += arr[std][other]
                    
    # 최소의 차이 찾기
    if minvalue > abs(Apower-Bpower):
        minvalue = abs(Apower-Bpower)
        
print(minvalue)
"""

"""
# 시간초과

# 모든 순열 뽑기
import itertools
for i in itertools.permutations(list(range(N))):
    # 앞에서 절반이 한 팀, 뒤에서 절반이 나머지 한 팀
    Apower = 0
    A = i[:N//2]; B =i[N//2:] # N//2 + 1이라고 생각해서 B가 하나 덜 들어왔다... ㅠㅠ 
    for std in range(N):
        if std in A:
            for others in range(N):
                if others in A:
                    Apower += arr[std][others]

    Bpower = 0
    for std in range(N):
        if std in B:
            for others in range(N):
                if others in B:
                    Bpower += arr[std][others]
                    
    # 최소의 차이 찾기
    if minvalue > abs(Apower-Bpower):
        minvalue = abs(Apower-Bpower)
        
print(minvalue)
"""
