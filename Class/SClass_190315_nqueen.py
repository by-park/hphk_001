#N-Queen
row = [0] * 14 # 행값은 순서대로 가니까 열값을 저장
def isPossible(k, c): # k번째 퀸의 위치 (k, c)
    # 그 이전에 결정한 퀸들의 위치, row[0 ~ k-1]
    for i in range(k):
        if k - i == abs(c - row[i]): return False
    return True

def nQueen(k, n, used):
    if k==n:
        global cnt
        cnt += 1
        return

    for i in range(n): # 순열 만들기
        if used & (1<<i): continue
       	# 답이 되는 선택인지 조사해서 거른다.
        # 0 ~ k-1 번째 퀸
        if not isPossible(k, i): continue
        row[k] = i # 0부터 3까지 하나씩 각 퀸의 열 값을 순서대로 나열한 것을 만든다.
        nQueen(k+1, n, used | (1<<i))
cnt = 0
nQueen(0, 14, 0)
print(cnt)
