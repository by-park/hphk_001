"""
11399 ATM
"""

N = input(); sum_ = 0; total = 0
a = list(map(int, input().split())); a.sort()
for m in a:
    sum_ += m
    total += sum_
print(total)
