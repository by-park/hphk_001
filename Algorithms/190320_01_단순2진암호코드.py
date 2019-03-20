T = int(input())
mapping = ['0001101','0011001','0010011','0111101', '0100011','0110001',
           '0101111','0111011','0110111','0001011']
"""
for tc in range(T):
    flag = 0
    N, M = map(int, input().split())
    for _ in range(N):
        arr = input() # 배열을 쭉 연결
        ans = 0
        check = 0
        # 8개 숫자를 점프하면서 홀수 자리는 x3으로 저장 짝수자리는 그대로 합
        cnt = 1
        if flag == 1:
            continue
        for a in range(N*M-56+1):
            cnt = 1
            for start in range(a, a+56, 7):
                #print("실행")
                if cnt % 2 == 1: # 홀수 자리
                    cnt = 0
                    for num in range(10):
                        #print(arr[start:start+7], mapping[num])
                        if arr[start:start+7] == mapping[num]:
#                           print(arr[start:start+7], mapping[num])
                            ans += num
                            check+= num*3                        
                            break
                else:
                    cnt = 1
                    for num in range(10):
                        if arr[start:start+7] == mapping[num]:
                            ans += num
                            check += num
                            break
            if check >= 10 and check % 10 == 0:
                flag= 1
                break
            else:
                ans = 0
                check = 0
        # ans
    print('#%d %d' %(tc+1, ans))
"""    


for tc in range(T):
    N, M = map(int, input().split())
    arr = ''
    for _ in range(N):
        arr += input() # 배열을 쭉 연결
    ans = 0
    check = 0
    # 8개 숫자를 점프하면서 홀수 자리는 x3으로 저장 짝수자리는 그대로 합
    cnt = 1
    for a in range(N*M-56+1):
        cnt = 1
        for start in range(a, a+56, 7):
            #print("실행")
            if cnt % 2 == 1: # 홀수 자리
                cnt = 0
                for num in range(10):
                    #print(arr[start:start+7], mapping[num])
                    if arr[start:start+7] == mapping[num]:
#                        print(arr[start:start+7], mapping[num])
                        ans += num
                        check+= num*3                        
                        break
                else: # 이 부분 안 넣으면 암호 숫자처럼 보이는 애를 넣어버린다!!!!
                    check = 0
                    break # 여기가 암호 숫자가 아니면 for문을 포기
            else:
                cnt = 1
                for num in range(10):
                    if arr[start:start+7] == mapping[num]:
                        ans += num
                        check += num
                        break
                else:
                    check = 0
                    break # 여기가 암호 숫자가 아니면 for문을 포기
        if check >= 10 and check % 10 == 0:
            break
        else:
            ans = 0
            check = 0
    # ans
    print('#%d %d' %(tc+1, ans))


# 딕셔너리로 찾게 하면 빠를까?
"""
1
1 56
00100110111101010001101100010101111011101101101110001011
"""
