"""
부분 집합의 합 문제

{1...10} 집합의 부분집합의 합이 10인 경우를 출력하라
"""

def backtrack(a, k, input_):
    for i in range(k, input_-k):
        # 이진 트리에서 다음 자리를 하나씩 1로 표시하거나 표시하지 않음
        c = a[:]
        c[i] = 1
        k += 1 # 뎁스 증가

        # 부분집합의 합 구하기
        ans = 0
        current_list = []
        for j in range(10):
            if c[j] == 1:
                current_list.append(j+1)
                ans += j + 1
        if ans == 10:
            print(current_list) # print(c)를 하게 되면 [1,1,1,1,0,0,0,0..] 이런 식으로 출력됨

        # 다음 뎁스의 백트래킹 계속 진행
        backtrack(c, k, input_)

# 함수 메인 동작 부분
a = [0] * 10
backtrack(a, 0, 10)