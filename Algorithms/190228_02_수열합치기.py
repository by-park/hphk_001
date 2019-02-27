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

# 또 제한시간 초과....
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
제한 시간 초과
for문 돌지 말고 max index값을 가지고 있다가 바로 넣자
어차피 문제를 보면 이전 수열에 합친다는 건 나보다 큰 애가 하나밖에 없다는 것이다.
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