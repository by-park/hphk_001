"""
트리 전위 순회
"""

# input
nodes = 13
lines = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13' # 왼쪽 노드, 오른쪽 노드 순서로 들어옴
lines = list(map(int, lines.split()))

# static 배열 만들기
array = [[0 for _ in range(2)] for __ in range(nodes+1)]
for idx in range(0, len(lines), 2):
    if array[lines[idx]][0] == 0:
        array[lines[idx]][0] = lines[idx+1] # 번호 그대로 인덱스 바로 접근
    else:
        array[lines[idx]][1] = lines[idx+1]
    
# pre-order: 상위 노드, 왼쪽 노드, 오른쪽 노드
def preorder(start):
    if start: # 0이 아닌 경우에만 다음 자식 노드를 계속 찾아감
        print(start) # 상위 노드
        preorder(array[start][0]) # 왼쪽 노드
        preorder(array[start][1]) # 오른쪽 노드

# 부모 노드가 1인 것도 인풋이 순서대로 들어오기 때문
preorder(1)
