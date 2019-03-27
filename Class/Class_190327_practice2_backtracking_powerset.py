def backtrack(k, end): # 현재 depth, 마지막 depth
    c = [False] * 2
    ncands = 2

    if k == end: process_solution(k)
    else:
        k += 1
        make_candidates(k, end, c)
        for i in range(ncands):
            a[k] = c[i]
            # 가지치기
            ans = 0
            ansA = []
            for j in range(k+1):
                if a[j] == True: ans += j; ansA.append(j)
            if ans > 10:
                return
            elif ans == 10:
                print(ansA)
                return
            backtrack(k, end)

def make_candidates(k, end, c):
    c[0] = True
    c[1] = False

def process_solution(k):
    ans = 0
    ansA = []
    for i in range(1, k+1):
        if a[i] == True: ans += i; ansA.append(i) #print(i, end=' ')
    #print()
    if ans == 10:
        print(ansA)

if __name__=="__main__":
    a = [False] * 11
    backtrack(0, 10)
