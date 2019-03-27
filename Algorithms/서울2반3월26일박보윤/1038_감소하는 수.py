"""
1038 감소하는 수

2019.03.26 PBY 최초작성

이거보다 큰 감소하는 수는 있을 수 없다.
9876543210
"""

# 모든 경우를 안 찾고 재귀로 하나씩 찾아 들어 가려고 하면
# 3 다음에 3 0 을 찾아왔을 때 이게 몇 번째인지 모른다.

def nextnum(depth, length):
    if depth == length:
        ans.append(arr[:]) # 복사해서 넘긴게 아니라 주소값이 바뀌었나? => 정답!
        return
    
    for j in range(10):
        if j < arr[depth-1]:
            arr[depth] = j
            nextnum(depth+1, length)
        else:
            return # 필요 없음
        

N = int(input())
ans = []
for length in range(1, 11): # 전체 range로
    arr = [0] * length
    for start in range(10):
        arr[0] = start
        nextnum(1, length)

if N > len(ans)-1: # -1을 안 넣었더니 런타임 에러가 나왔다!!!!!
    print(-1)
else:
    print(''.join(map(str, ans[N])))
    
"""
시간초과

N = int(input())
if N < 11:
    print(N)
else:
    n = 10 # 몇 번째냐고
    
    for i in range(11, 9876543211):
        # 감소하는 수면 n을 증가시킴
        stri = str(i)
        for j in range(len(stri)-1):
            if stri[j] <= stri[j+1]:
                break
        else:
            n += 1
            
        if n == N:
            print(stri)
            break
    else:
        print(-1)
"""
