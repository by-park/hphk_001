T = int(input())
for tc in range(T):
    N = int(input())
    tree = [[1],[1,1]]
    for n in range(N-1): # 매 줄을 돌면서
        newtree = []
        for i in range(n): # 그 줄에 출력해야 하는 애를 출력
            newtree.append(tree[-1][i] + tree[-1][i+1])
        if newtree:
            tree.append([1]+newtree+[1])
    #출력
    print("#%d" %(tc+1))
    for n in range(N):
        print(' '.join(list(map(str, tree[n]))))
