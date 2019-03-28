def binarysearch(array, std, direction):
    global cnt
    if len(array) < 1: # 빈 리스트가 들어오면
        # M에 속한 어떤 수가 A에 들어있으면서!
        return
    middle = (len(array)-1)//2 # 예제를 보면 (0+9)//2 이런 식
    if array[middle] < std:
        if direction == 2: return
        binarysearch(array[middle+1:], std, 2)
    elif array[middle] > std:
        if direction == 1: return
        binarysearch(array[:middle], std, 1)
    elif array[middle] == std:
        # middle이면서 left면 left로 치는 것 같다....
        #if  len(array) == 2 and direction == 1: return # 이전에 왼쪽 방향으로 왔으면 찾았어도 안 됨
        cnt += 1
        return
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Na = list(map(int, input().split()))
    Na.sort()
    Ma = list(map(int, input().split()))
    cnt = 0 # 양쪽 구간 번갈아 찾는 수의 개수
    middle = (N-1)//2 
    for m in Ma: # 원소를 하나 선택해서 그거를 찾아 들어감
        # 방향이 달라지면 바로 끝내기
        # 처음에 방향 선택
        if   Na[middle] < m:
            binarysearch(Na[middle+1:], m, 2) # 오른쪽 탐색
        elif Na[middle] > m :
            binarysearch(Na[:middle], m, 1)
        elif Na[middle] == m:
            cnt += 1
            
    print("#%d %d" %(tc, cnt))

