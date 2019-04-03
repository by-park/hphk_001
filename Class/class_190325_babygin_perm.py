def perm(n, k):
    global ans
    if k == n:
        # 순열이 생성되면 baby-gin 검사
        # 처음 3 자리가 런인지, 트리플렛인지
        if (arr[0] == arr[1] == arr[2]) or ((arr[0] + 1 == arr[1]) and (arr[1]+1 == arr[2])):
            if (arr[3] == arr[4] == arr[5]) or ((arr[3]+1 == arr[4]) and (arr[4]+1 == arr[5])):
                ans = 1
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = list(map(int, input().split()))
ans = 0
perm(len(arr), 0)
if ans == 1:
    print("Baby-gin!")
else:
    print("No...")
    
"""
1 2 4 7 8 3
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
"""

"""
라이브러리 사용
"""
    
import itertools
for i in itertools.permutations(map(int, input().split())):
    if (i[0] == i[1] == i[2]) or ((i[0] + 1 == i[1]) and (i[1]+1 == i[2])):
            if (i[3] == i[4] == i[5]) or ((i[3]+1 == i[4]) and (i[4]+1 == i[5])):
                ans = 1
if ans == 1:
    print("Baby-gin!")
else:
    print("No...")
