arr = list(map(int, input().split()))

n = len(arr)

cnt = 0
for i in range(1<<n):
    summation = 0
    for j in range(n):
        if i & (1<<j):
            summation += arr[j]
    if summation == 0: cnt += 1
    print(summation, bin(i))

print("0의 개수: {}".format(cnt))

# 선생님 코드
arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
sum = cnt = 0

# 공집합은 빼는 과정
for i in range(1, 1 << len(arr)):
    for j in range(len(arr)):
        if i & (1 <<j):
            sum += arr[j]
    if sum == 0:
        cnt += 1
        print("%d: ")