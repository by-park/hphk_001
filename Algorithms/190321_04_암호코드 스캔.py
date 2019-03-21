"""
암호코드 스캔

최초작성 2019.03.21 PBY

입력)
1
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000

56 배수여야하는데, 4개씩 코드로 변환됨. 그 개수가 56개
그러면 최소 len은 4개씩 코드로 56배수를 만들려면....14개...
=> 아님

가능한 암호 코드의 길이들
56 112 168 224 280 336 392 ...
"""
import sys
sys.stdin = open('190321_04_input.txt','r')
mapping = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

T = int(input())
for tc in range(1, T+1): # T+1
    N, M = map(int, input().split())
    codes = [] # 암호 코드 맞는 바코드들 넣기
    ans = 0 # 정답 출력을 위한 변수
    
    for _ in range(N):
        array = input()
        # input을 받으면, 끝에서부터 돌면서 다 이진수로 변환
        two = ''
        for i in range(M-1, -1, -1):
            if ord(array[i]) >= ord('A'):
                binary = bin(ord(array[i])-ord('A')+10)
                two = '0'*(6-len(binary)) + binary[2:] +two
            else:
                binary = bin(int(array[i]))
                two = '0'*(6-len(binary)) + binary[2:] +two
                
        # 이진수를 거꾸로 돌면서 들어온 숫자 배열이 어느 길이의 암호인지 찾기
        idx = len(two)-1
        while idx > -1:
            if two[idx] != '0': # 암호가 시작되는 위치를 찾았으면 (무조건 그건 암호일 수밖에 없음)
                
                # 가능한 암호의 길이
                amho = []
                for k in range(1, 36):
                    if 56*k <= idx:
                        amho.append(56*k)

                pre_idx = idx # 암호의 끝자리를 저장해둠
                check = 0
                fromback = -1 # 가장 긴 길이부터 암호가 가능한지 체크

                # 거꾸로 암호 시작 위치를 찾아간다
                while check == 0:
                    
                    # 가능한 제일 긴 암호 길이부터 체크
                    idx -= amho[fromback]
                    
                    # 제일 긴 거씩 확인하다가 out of range가 나면 더 짧은 길이로 줄여야함
                    if idx < -1: # 맨 앞 배열인 경우가 있을 수 있어서?
                        idx = pre_idx
                        fromback -= 1
                        continue

                    # 0을 만나면 그 길이까지 확인해보고, 아니면 idx를 더 줄여서 암호 길이를 더 길게 생각한다.
                    if idx == -1 or two[idx] == '0': # 0을 만나던지 배열 끝에 닿던지
                        c = two[idx+1:pre_idx+1]
                        if c not in codes: # 이미 정한 정답이 아니면,
                            am = [] # 암호 코드들을 저장
                            breakpoint = 0
                            for start in range(0, len(c), 7*amho[fromback]//56):
                                for mapp in range(10):
                                    if c[start:start+7*amho[fromback]//56] == '0'*mapping[mapp][0]*(amho[fromback]//56) + '1'*mapping[mapp][1]*(amho[fromback]//56) + '0'*mapping[mapp][2]*(amho[fromback]//56) + '1'*mapping[mapp][3]*(amho[fromback]//56):
                                        am.append(mapp)
                                        break
                                else: # 암호가 아닌데 모르고 넘어가면 안됨 => 이거 때문에 8번에 7000이 나왔나? 맞음!!!!!
                                    breakpoint = 1
                                    idx = pre_idx
                                    fromback -= 1

                                if breakpoint == 1: # 한 번이라도 7개 글자가 암호가 아니면 그냥 넘어가면 안 됨
                                    break
                            if breakpoint == 1:
                                continue # 암호 체크하다 나왔으면 아래는 못 돌림
                            
                            # 암호인지 확인
                            if len(am) == 8:
                                value = (am[0]+am[2]+am[4]+am[6])*3 + (am[1]+am[3]+am[5]+am[7])
                                if value % 10 == 0:
                                    # 정상적 암호코드
                                    ans += sum(am)
                                    codes.append(c)
                                check = 1
                                break
                            # 암호가 아니면 amho[-1]을 바꿔야함
                            else:
                                idx = pre_idx # 다시 복구시킨다음에
                                fromback -= 1 # 더 뒤로 가야함
                        else: # 이미 정답이면 한 번 더 체크할 필요 없음
                            check = 1
                            break
            else:
                idx -= 1

    print("#%d %d" %(tc, ans))


"""

T = int(input())
for tc in range(1, T+1): # T+1
    N, M = map(int, input().split())

    #가능한 모든 암호 길이
    amho = []
    for k in range(1, 36):
        if 56*k <= M*4:
            amho.append(56*k)

    codes = []
    ans = 0
    for _ in range(N):
        array = input()
        # 끝에서부터 돌면서 다 이진수로 변환
        two = ''
        for i in range(M-1, -1, -1):
            if ord(array[i]) >= ord('A'):
                binary = bin(ord(array[i])-ord('A')+10)
                two = '0'*(6-len(binary)) + binary[2:] +two
            else:
                binary = bin(int(array[i]))
                two = '0'*(6-len(binary)) + binary[2:] +two
        # 이진수를 거꾸로 돌면서 숫자의 길이를 센다
        idx = len(two)-1
        while idx > -1:
            if two[idx] != '0':
                pre_idx = idx
                print(idx)
                while idx > -1: # 무조건 암호 시작
                    idx -= (56) # 56 배수 #=> 디버깅:  56자리에서 암호 코드가 안 끝날 수 있다.
                    if two[idx] == '0' or idx == -1: # 0을 만나던지 배열 끝에 닿던지
                        #print(array)
                        if two[idx+1:pre_idx+1] not in codes:
                            #print(array[idx+1:pre_idx+1], idx, idx+1)
                            codes.append(two[idx+1: pre_idx+1])
                        break
            else:
                idx -= 1
    # 만든  codes 배열을 2진수로 변환
    #print(codes)
    for c in codes:
        value= 1
        # 2진수로 변환을 다 했으면, 돌면서 암호인지 확인
        am = []
        for start in range(0, len(c), 7*len(c)//56):
            for mapp in range(10):
                if c[start:start+7*len(c)//56] == '0'*mapping[mapp][0]*(len(c)//56) + '1'*mapping[mapp][1]*(len(c)//56) + '0'*mapping[mapp][2]*(len(c)//56) + '1'*mapping[mapp][3]*(len(c)//56):
                    am.append(mapp)
                    break
        # 암호를 변환
        value = (am[0]+am[2]+am[4]+am[6])*3 + (am[1]+am[3]+am[5]+am[7])
        if value % 10 == 0:
            # 정상적 암호코드
            ans += sum(am)
    print("#%d %d" %(tc, ans))
"""

"""
T = int(input())
for tc in range(1, T+1): # T+1
    N, M = map(int, input().split())
    codes = []
    ans = 0
    for _ in range(N):
        array = input()
        idx = M-1
        while idx > -1:
            if array[idx] != '0':
                pre_idx = idx
                idx -= 1 # 하나 전 부터 14씩 가면서
                while idx > -1: # 무조건 암호 시작
                    idx -= (14) # 앞에 충분한 공간을 두기 위함
                    if array[idx] == '0' or idx <= 0: # 0을 만나던지 배열 끝에 닿던지
                        if array[idx+1:pre_idx+1] not in codes:
                            #print(array[idx+1:pre_idx+1], idx, idx+1)
                            codes.append(array[idx+1: pre_idx+1])
                        break
            else:
                idx -= 1
    # 만든  codes 배열을 2진수로 변환
    print(codes)
    for c in codes: # 암호를 하나씩 확인하면서
        two = ''
        for letter in c: # 글자들을 다 2진수로 변환
            if ord(letter) >= ord('A'):
                binary = bin(ord(letter)-ord('A')+10)
                two += '0'*(6-len(binary)) + binary[2:]
            else:
                binary = bin(int(letter))
                two += '0'*(6-len(binary)) + binary[2:]
        # 2진수로 변환을 다 했으면, 돌면서 암호인지 확인
        am = []
        # 근데 앞 뒤로 0 붙은 거 잘라내야함
        # 뒤 시작 지점 알아야함
        for findtwoend in range(len(two)-1, -1, -1):
            if two[findtwoend] != '0':
                two = two[findtwoend-56*(len(c)//14)+1: findtwoend+1]
                break
        for start in range(0, len(two), 7*len(two)//56):
            for mapp in range(10):
                if two[start:start+7*len(two)//56] == '0'*mapping[mapp][0]*(len(two)//56) + '1'*mapping[mapp][1]*(len(two)//56) + '0'*mapping[mapp][2]*(len(two)//56) + '1'*mapping[mapp][3]*(len(two)//56):
                    am.append(mapp)
                    break
        # 암호를 변환
        value = (am[0]+am[2]+am[4]+am[6])*3 + (am[1]+am[3]+am[5]+am[7])
        if value % 10 == 0:
            # 정상적 암호코드
            ans += sum(am)
    print("#%d %d" %(tc, ans))
"""
    
"""        
    #array = []
    codes = []
    idx = M-1
    while idx > -1:
        if 
            
        temp = input().split('000')
        for i in temp:
            if len(i) >= 14: # 암호 코드만 들어가도록
                array += [i]
    array = set(array)
    for a in array:
        # a를 뒤집어서 확인하면서 //56 한 암호인지 확인
        length = len(a) //14 # 배수 확인
        # a를 뒤집어서 2진수로 변환
        two = ''
        for r in a[::-1]:
            if ord(r) >= ord('A'):
                binary = bin(ord(r)-ord('A')+10)
                two = '0'*(6-len(binary)) + binary[2:] + two
            else:
                binary = bin(int(r))
                two = '0'*(6-len(binary)) + binary[2:] + two
        # 2진수로 변환을 다 했으면, 돌면서 암호인지 확인
        for start in range(0, len(two), 7):
"""            
 

"""
timebird
def makebi(M):
    M = M.replace('0','0000')
    M = M.replace('1','0001')
    M = M.replace('2','0010')
    M = M.replace('3','0011')
    M = M.replace('4','0100')
    M = M.replace('5','0101')
    M = M.replace('6','0110')
    M = M.replace('7','0111')
    M = M.replace('8','1000')
    M = M.replace('9','1001')
    M = M.replace('A','1010')
    M = M.replace('B','1011')
    M = M.replace('C','1100')
    M = M.replace('D','1101')
    M = M.replace('E','1110')
    M = M.replace('F','1111')
    return M
 
def divcode(binum):
    binum = binum.lstrip('0')
    tmp = ''
    global codes
    flag = ['0']
    for b in binum:
        if b != flag[-1]:
            flag.append(b)
             
        if len(flag) > 32:
            flag = ['0']
            a = 56 - len(tmp)%56
            tmp = '0'*a + tmp
            codes.add(tmp)
            tmp = ''
        elif len(flag) > 1 and len(flag) <= 32:
            tmp += b
    return None
 
def convert(pwd, x):
    result = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if pwd[7*x*i:7*x*i+7*x] == '000'*x+'11'*x+'0'*x+'1'*x:
            result[i] = 0
            continue
        if pwd[7*x*i:7*x*i+7*x] == '00'*x + '11'*x + '00'*x + '1'*x:
            result[i] = 1
            continue
        if pwd[7*x*i:7*x*i+7*x] == '00'*x + '1'*x + '00'*x + '11'*x:
            result[i] = 2
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '1111'*x + '0'*x + '1'*x:
            result[i] = 3
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '1'*x + '000'*x + '11'*x:
            result[i] = 4
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '11'*x + '000'*x + '1'*x:
            result[i] = 5
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '1'*x + '0'*x + '1111'*x:
            result[i] = 6
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '111'*x + '0'*x + '11'*x:
            result[i] = 7
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '11'*x + '0'*x + '111'*x:
            result[i] = 8
            continue
        if pwd[7*x*i:7*x*i+7*x] == '000'*x + '1'*x + '0'*x + '11'*x:
            result[i] = 9
            continue
 
    return result
 
TC = int(input())
 
for tc in range(TC):
    N, M = list(map(int,input().split()))
    nums = []
    ans = 0
    codes = set()
 
    for n in range(N):
        tmp = input().lstrip('0')
        if tmp and tmp not in nums:
            nums.append(tmp)
     
    for n in nums:
        binum = makebi(n)
        divcode(binum)
 
    for code in codes:
        x = len(code)//56
        pwd = convert(code,x)
 
        result = (pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3 + (pwd[1] + pwd[3] + pwd[5]) + pwd[7]
 
        if result%10 == 0:
            ans += sum(pwd)
        else:
            result = 0
            continue
 
    print(f'#{tc+1} {ans}')
"""
