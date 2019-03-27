# 일차원 배열로 만들려면 딕셔너리로 할 수 있을 것 같다....!!!!!
# => 딕셔너리도 아닌 듯. 그냥 이전에 들어온 인풋값이랑 비교해서 넣어야할 것 같다.

def pretraversal(t): # t 노드
        print(t) # 이거 위치만 바꾸면 모든 순회 다 가능!
        if trees[t][0]:
            pretraversal(trees[t][0])
        
        if trees[t][1]:
            pretraversal(trees[t][1])

N = 12
lines = list(map(int, '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split()))

# 높이가 4가 되니까 2의 5승 -1 만큼 잡으면 된다.
#trees = [0] * (2**5+1) # -1을 안 해주는 것은 내 함수의 끝이 0에서 끝나기 때문에.... 거기에다가 1번 노드부터 시작하니까 +1도 해줬다.
trees = [[0 for _ in range(2)] for __ in range(13+1)]

for i in range(12): # 길이가 24개이고, 인덱스로는 *2를 한게 23에 접근해야한다....
    if trees[lines[i*2]][0] == 0:
        trees[lines[i*2]][0] = lines[i*2+1]
    else:
        trees[lines[i*2]][1] = lines[i*2+1]

print(trees)    
pretraversal(1)

