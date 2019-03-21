"""
정식이의 은행업무

최초작성 2019.03.21 PBY

입력)
1
1010
212
// Test Case 수
// Test Case 1, 2진수
// Test Case 1, 3진수

출력)
#1 14 #Test case 1의 정답
"""
twos = {'0':'1', '1':'0'}
threes = {'0': ['1', '2'], '1':['0','2'], '2':['1','0']}

def whatnumber(num, jin):
    ans = 0
    num = num[::-1]
    for i in range(len(num)):
        ans += int(num[i])*(jin**i)
    return ans

T = int(input())
for tc in range(1, T+1):
    two = input()
    three = input()
    for i in range(len(two)):
        twonumber = whatnumber(two[:i]+twos[two[i]]+two[i+1:], 2)
        for j in range(len(three)):
            threenumber = whatnumber(three[:j]+threes[three[j]][0]+three[j+1:], 3)
            if twonumber == threenumber:
                break
            threenumber = whatnumber(three[:j]+threes[three[j]][1]+three[j+1:], 3)
            if twonumber == threenumber:
                break
        if twonumber ==threenumber:
            print("#%d %d" %(tc, twonumber))
            break

