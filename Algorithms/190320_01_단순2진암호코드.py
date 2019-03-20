T = int(input())
mapping = ['0001101','0011001','0010011','0111101', '0100011','0110001','0101111','0111011','0110111','0001011']

for tc in range(T):
    N, M = map(int, input().split())
    arr = ''
    for _ in range(N):
        arr += input() # 배열을 쭉 연결
    ans = 0
    check = 0
    # 8개 숫자를 점프하면서 홀수 자리는 x3으로 저장 짝수자리는 그대로 합
    cnt = 1
    for a in range(N*M-56):
        for start in range(a, a+56, 8):
            if cnt % 2 == 1: # 홀수 자리
                for num in range(10):
                    if arr[start:start+8] == mapping[num]:
                        ans += num
                        check+= num*3
                        cnt = 0
            else:
                for num in range(10):
                    if arr[start:start+8] == mapping[num]:
                        ans += num
                        check += num
                        cnt = 1
        if check >= 10 and check % 10 == 0:
            break
        else:
            ans = 0
            check = 0
    # ans
    print('#%d %d' %(tc+1, ans))

# 딕셔너리로 찾게 하면 빠를까?
