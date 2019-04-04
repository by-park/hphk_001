"""Solving Club"""
"""
최대상금

2019.04.03 PBY 최초작성

그냥 Selection Sort처럼 진행하고 마지막에 의미없는 마지막 숫자만 반복하게 하면 수학적으로 안 되는 경우가 생기는지?
교환을 잘 하게 하는 것은 최소 교환 횟수를 찾는데 도움이 되는 거 아닌가?

엄밀히 Selection Sort는 아니다. 32888이 88823 이런 식으로 자꾸 나와서 보니까 제일 작은 수가 끝으로 오게 하지 않았다.
나한테 주어진 기회 안에 제일 작은 수가 끝으로, 제일 큰 수가 맨 앞으로 오게 해야할 것 같다.

=> 메모리 초과

# 두 개만 자리 바꾸기 위한 것
itertools.combinations(range(len(numbs)), 2))
# 한성님 방법으로 2개 자리 바꾸고, 계속 다 바꿔가면서 최대값을 찾아내는 것이 정답인 것 같다. (가짓수가 엄청 많아지겠지만)
"""
import sys
sys.stdin = open('190403_01_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    numlist = [0] * len(numbers)
    for i in range(len(numbers)):
        numlist[i] = int(numbers[i])
    # 이것을 배열로 바꾸고... selection sort
    fixed = 0 # 교환이 끝난 자리수
    c = 0 # 교환 횟수
    while c < int(change): # 교환 횟수동안 바꿔야함
        # print(numlist, c)
        # 만약에 fixed가 더 늘어날 수 없으면 그냥 끝 두 수만 계속 자리 바꾸기
        if fixed == len(numbers): # 끝까지 정렬이 끝났으면
            # 근데 똑같은 수가 2개 이상이면 그냥 끝내면 된다. 그냥 그거만 자리 바꾸면 되니까
            if len(set(numbers)) < len(numbers):
                break
            numlist[-1], numlist[-2] = numlist[-2], numlist[-1]
            c += 1 # 그냥 횟수 채우기
            continue
        maxvalue = numlist[fixed]
        maxindex = fixed
        check = 0
        # 나보다 작은 애가 몇 개인지 찾아서
        # 최대 수가 여러개일 때 몇 번 지나칠지!
        maxcount = 0
        mincount = 0

        for j in range(fixed+1, len(numbers)): # 아직 sort되지 않은 곳을 돌면서
            if numlist[j] < numlist[fixed]:
                mincount += 1 # 나보다 작은 수가 몇 개인지 확인

        maxindexlist= []
        for j in range(fixed+1, len(numbers)):
            if numlist[j] > maxvalue:
                check = 1
                maxcount = 1
                maxvalue = numlist[j]
                maxindexlist = [j]
#                maxindex = j
#                 if maxcount == mincount: # 나보다 작은 수 만큼 max 찾았으면 끝
#                     break
            elif numlist[j] == maxvalue: # 최고 값이 여러개인 경우
                maxcount += 1
                maxindexlist.append(j)
        if check == 1: # 나보다 큰 수가 있어야만 자리 교환이 일어남
            # print(maxindexlist)
            if mincount >= maxcount:
                numlist[fixed], numlist[maxindexlist[0]] = numlist[maxindexlist[0]], numlist[fixed]
            else:
                numlist[fixed], numlist[maxindexlist[-1-mincount]] = numlist[maxindexlist[-1-mincount]], numlist[fixed]
            fixed += 1
            c += 1
        else:
            fixed += 1 # 나보다 큰 수 없으면 그냥 지나치면 됨
    print("#{}".format(tc), ''.join(map(str, numlist)))

# 나랑 똑같은 수가 여러 개 일 때 fixed에 있는 수보다 작은 수가 있으면, 그만큼을 더 진행함
# 77770 을 틀린다....
"""
T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    numlist = [0] * len(numbers)
    for i in range(len(numbers)):
        numlist[i] = int(numbers[i])
    # 이것을 배열로 바꾸고... selection sort
    fixed = 0 # 교환이 끝난 자리수
    c = 0 # 교환 횟수
    while c < int(change): # 교환 횟수동안 바꿔야함
        print(numlist, c)
        # 만약에 fixed가 더 늘어날 수 없으면 그냥 끝 두 수만 계속 자리 바꾸기
        if fixed == len(numbers): # 끝까지 정렬이 끝났으면
            numlist[-1], numlist[-2] = numlist[-2], numlist[-1]
            c += 1 # 그냥 횟수 채우기
            continue
        maxvalue = numlist[fixed]
        maxindex = fixed
        check = 0
        # 나보다 작은 애가 몇 개인지 찾아서
        # 최대 수가 여러개일 때 몇 번 지나칠지!
        maxcount = 0
        mincount = 0

        for j in range(fixed+1, len(numbers)): # 아직 sort되지 않은 곳을 돌면서
            if numlist[j] < numlist[fixed]:
                mincount += 1 # 나보다 작은 수가 몇 개인지 확인

        maxindexlist= []
        for j in range(fixed+1, len(numbers)):
            if numlist[j] > maxvalue:
                check = 1
                maxcount = 1
                maxvalue = numlist[j]
                maxindexlist = [j]
#                maxindex = j
#                 if maxcount == mincount: # 나보다 작은 수 만큼 max 찾았으면 끝
#                     break
            elif numlist[j] == maxvalue: # 최고 값이 여러개인 경우
                maxcount += 1
                maxindexlist.append(j)
        if check == 1: # 나보다 큰 수가 있어야만 자리 교환이 일어남
            # print(maxindexlist)
            if mincount >= maxcount:
                numlist[fixed], numlist[maxindexlist[0]] = numlist[maxindexlist[0]], numlist[fixed]
            else:
                numlist[fixed], numlist[maxindexlist[-1-mincount]] = numlist[maxindexlist[-1-mincount]], numlist[fixed]
            fixed += 1
            c += 1
        else:
            fixed += 1 # 나보다 큰 수 없으면 그냥 지나치면 됨
    print("#{}".format(tc), ''.join(map(str, numlist)))
"""

# 3번째 케이스를 못 잡음
"""
T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    numlist = [0] * len(numbers)
    for i in range(len(numbers)):
        numlist[i] = int(numbers[i])
    # 이것을 배열로 바꾸고... selection sort
    fixed = 0 # 교환이 끝난 자리수
    for c in range(int(change)): # 교환 횟수동안 바꿔야함
        print(numlist, fixed)
        maxvalue = numlist[fixed]
        check = 0
        for j in range(fixed+1, len(numbers)): # 아직 sort되지 않은 곳을 돌면서
            if numlist[j] >= maxvalue:
                check = 1
                maxvalue = numlist[j]
                maxindex = j
        # 돌고 나면 max가 찾아지니까 그거를 넣는다.
        numlist[fixed], numlist[maxindex] = numlist[maxindex], numlist[fixed]
        fixed += 1

    print(''.join(map(str, numlist)))
"""