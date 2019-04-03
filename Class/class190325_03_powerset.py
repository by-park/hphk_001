arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

for i in range(1, (1<<n)):
    sum_ = 0
    ans = []
    for j in range(0, n):
        if i & (1<<j):
            sum_ += arr[j]
            ans.append(arr[j])
    if sum_ == 0:
        print(ans)

"""
조합생성 알고리즘
"""
print("=========")
an = [1, 2, 3, 4]
tr = [0, 0, 0]
def comb(n, r):
    if r == 0:
        print(tr)
        return
    if n < r: return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
comb(4, 3)
