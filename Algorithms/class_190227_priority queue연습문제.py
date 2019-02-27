# 우선순위 큐 구현
inputlist = [1, 5, 2, 4, 3]

# 새로운 게 들어올 때마다 가장 뒤에 있는 애를 확인함
new = inputlist.pop(0)
priorityque = []
priorityque.append(new)

while len(inputlist)>0:
    new = inputlist.pop(0)
    for idx in range(len(priorityque)-1, -1, -1):
        if priorityque[idx] <= new:
            priorityque.insert(idx+1, new) # 뒤에서부터 보면서 그 위치에 내가 들어감
            break

print(priorityque)

# break 를 안 넣으면?
# [1, 2, 5] 까지는 제대로 가고 3이 되는 순간 insert가 두 번 돌면서 3이 두번 들어간다.
# 잘못된 답 [1, 3, 4, 2, 3, 4, 5] 가 출력되어버림 ㅠㅠ!!

