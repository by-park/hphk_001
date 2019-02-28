"""
5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기
문제 내용
여러 개의 수열을 정해진 규칙에 따라 합치려고 한다. 다음은 3개의 수열이 주어진 경우의 예이다.
수열 2의 첫 숫자 보다 큰 수자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.
합쳐진 수열에 대해, 수열 3의 첫 숫자보다 큰 숫자를 찾아 그 앞에 수열 3을 끼워 넣는다. 큰 숫자가 없는 경우 맨 뒤에 붙인다.
마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.

최초 작성 2019.02.27 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190228_02_input.txt", "r")

# version 1 (원래 코드 시간 단축 버전)
T = int(input())

for tc in range(T):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split())) # 처음 거는 인풋 받아서 만들고
    for _ in range(M-1): # 그 다음부터는 이전 거랑 비교
        temp_numbers = list(map(int, input().split()))
        for idx in range(len(numbers)):
            if numbers[idx] > temp_numbers[0]:
                numbers[idx:idx] = temp_numbers
                break
        else: # break에 걸리지 않은 경우
            numbers += temp_numbers
    print("#%d %s" %(tc+1, ' '.join(list(map(str,numbers[::-1][:10])))))

"""
=> [idx:idx] 만 했는데 시간 초과 통과!
"""

# version 2 (연결리스트 버전)
# 마지막 노드로 삽입
"""
def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)


# 노드 삭제
def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link


# 가운데 노드로 삽입
def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)


# 첫번째 노드 삽입
def addtoFirst(data):
    global Head
    Head = Node(data, Head)


class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n


import sys

if __name__ == "__main__":
    sys.stdin = open('C:/Users/BY/Desktop/sample_input.txt', 'r')
    T = int(input())
    for tc in range(T):
        # input
        N, M = list(map(int, input().split()))
        numbers = list(map(int, input().split()))  # 처음 거는 인풋 받아서 만들고

        # 노드로 삽입
        Head = None
        addtoFirst(numbers[0])

        # 나머지도 노드로 이어 붙이기
        for node in numbers[1:]:
            addtoLast(node)

        # 다음 수열 돌면서
        for _ in range(M - 1):
            temp_numbers = list(map(int, input().split()))
            pre = Head  # 수열의 맨 앞부터 다 돌면서 내가 필요한 지점 찾기
            while pre.link != None:
                if pre.link.item > temp_numbers[0]:  # 다음 거의 아이템이 나보다 크면
                    break
                pre = pre.link
            # 아이템들을 거기에 넣어줌
            if pre == Head:  # 맨 앞에 들어가는 경우 Head를 업데이트
                addtoFirst(temp_numbers[0])
                pre = Head  # 이걸 안 써서 덮어씌워졌다. pre = pre.link말고 Head값을 가지고 돌도록 해야함
                for item in temp_numbers[1:]:
                    add(pre, item)
                    pre = pre.link
            else:
                for item in temp_numbers:
                    add(pre, item)
                    pre = pre.link  # 연결 잊지 말기

        # 최종 결과는 뒤집어서 출력
        pre = Head
        ans = [0] * N * M
        ind = 0
        while pre.link != None:
            ans[ind] = pre.item
            pre = pre.link
            ind += 1
        ans[ind] = pre.item  # while문 나오면서 마지막 거리를 안 넣어줬다....
        # 출력
        print("#{} {}".format(tc + 1, ' '.join(list(map(str, ans[::-1][:10])))))
"""

"""
연결 리스트로 구현한 코드 실패한 내용들

pre = pre.link를 항상 이어서 써줘야 다음 link로 이어질 수 있는데, 그것을 업데이트 해주는 줄을 써주지 않아서
계속 덮어씌워졌다. 결과가 [0, 15, 9 ..] 이런 식으로 0부터 시작하는 현상을 발견하고 수정하였다.

pre = Head를 안 해주면 그 다음 for 문 들어갈 때, 맨 앞을 pre 기준으로 삼을 수가 없었다.
pre = pre.link 이렇게 써줘서 한칸 밀려서 들어갔다!! pre.link는 다음 칸을 가리키는 거니까.

=> 결국 시간 안에 성공!
"""

# 또 제한시간 초과....
"""
T = int(input())

for tc in range(T):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split())) # 처음 거는 인풋 받아서 만들고

    # max index 찾기
    max_value = [0, 0]
    for num in range(N):
        if numbers[num] > max_value[1]:
            max_value = [num, numbers[num]]

    # 그리고 max_index를 업데이트하면서 거기에 덧붙이기
    for _ in range(M-2): # 그 다음부터는 이전 거랑 비교
        temp_numbers = list(map(int, input().split()))

        # 내 첫 숫자가 max 값과 얼마나 차이나는지 확인 (이걸로 시간 단축을 노리자!)
        if temp_numbers[0] > max_value[1]:
            numbers.extend(temp_numbers) # 내가 더 크면 그냥 뒤에 이어붙임
            max_value[0] += 1 # 나 때문에 max 위치가 뒤로 밀림
        else:
            numbers = numbers[:max_value[0]] + temp_numbers + numbers[max_value[0]:]

        # 지금 범위에서 max를 확인
        for num in range(len(temp_numbers)):
            if temp_numbers[num] > max_value[1]:
                max_value = [max_value[0]+num, temp_numbers[num]] # 이전 max 위치를 더해서 업데이트 (내가 중간에 insert 되었으니까)

    # 마지막 수열은 앞에다가 붙임 - 이거 반대로 해놓고 한참 찾음...
    numbers = list(map(int, input().split())) + numbers

    print("#%d" %(tc+1), end=" ")
    for i in range(len(numbers)-1, len(numbers)-1-10, -1):
        print(numbers[i], end=" ")
    print()
#    print("#%d %s" %(tc+1, ' '.join(list(map(str,numbers[::-1][:10])))))
"""

"""
제한 시간 초과
for문 돌지 말고 max index값을 가지고 있다가 바로 넣자
어차피 문제를 보면 이전 수열에 합친다는 건 나보다 큰 애가 하나밖에 없다는 것이다.
=> 왜 안 틀렸지? 시간 초과 때문에 답이 틀렸을 것 같아도 검증이 안 되었다.
"""

"""
제한시간 초과 코드

T = int(input())

for tc in range(T):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split())) # 처음 거는 인풋 받아서 만들고
    for _ in range(M-2): # 그 다음부터는 이전 거랑 비교
        temp_numbers = list(map(int, input().split()))
        for idx in range(len(numbers)):
            if numbers[idx] > temp_numbers[0]:
                numbers = numbers[:idx] + temp_numbers + numbers[idx:]
                break
                # for temp_idx in range(N):
                #     numbers.insert(idx+temp_idx, temp_numbers[temp_idx])
                # break # 삽입하면 나가기
        else: # break에 걸리지 않은 경우
            numbers.extend(temp_numbers)
    numbers = list(map(int, input().split())) + numbers
    print("#%d" %(tc+1), end=" ")
    for i in range(len(numbers)-1, len(numbers)-1-10, -1):
        print(numbers[i], end=" ")
    print()
#    print("#%d %s" %(tc+1, ' '.join(list(map(str,numbers[::-1][:10])))))
"""