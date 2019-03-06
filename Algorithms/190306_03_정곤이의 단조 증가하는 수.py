"""
정곤이의 단조 증가하는 수

정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


[출력]
각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.
만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

2019.03.06 PBY 최초작성
"""
# 1번과 2번 곱하는 것과 2번과 1번 곱하는 것이 같아서 조합 문제이다.
# n C 2 역으로 갈 필요는 없다!

T = int(input())

# 단조 증가하는 수 체크
# c스타일로 짜려면 t = x % 10, x // = 10 으로 if x % 10 > t: return False 로 할 수 있다. 뒤에서부터 오니까 부등호가 반대가 된다.

def checkNum(num):
    strnum = str(num)
    for idx in range(len(strnum)-1):
        if int(strnum[idx]) > int(strnum[idx+1]): # int 비교를 해야하는 걸 str 비교를 했네...
            return False
    return True

for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))  # 바보같이 이걸 맨 앞에다 두고 있었다!!!!!
    maxlist = []
    # Ai x Aj 의 조합들을 다 뱉음
    for i in range(N):
        for j in range(i+1, N):
            if checkNum(A[i]*A[j]):
                maxlist.append(A[i]*A[j])

    if len(maxlist) < 1:
        print("#%d -1" %(tc+1)) # -1 처리 안 해줬더니 런타임 에러
    else:
        print("#%d %d" %(tc+1, max(maxlist)))
