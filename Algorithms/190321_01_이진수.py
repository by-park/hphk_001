"""
문제해결 응용 1일차 - 이진수

최초작성 2019.03.21 PBY

입력)
3
4 47FE
5 79E12
8 41DA16CD

출력)
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101
"""

T = int(input())
for tc in range(1, T+1):
    N, numbers = input().split()
    arr = ''
    for i in range(int(N)):
        if ord(numbers[i]) >= ord('A'):
            binary = bin(ord(numbers[i])-ord('A')+10)
            arr += '0'*(6-len(binary)) + binary[2:]
        else:
            binary = bin(int(numbers[i]))
            arr += '0'*(6-len(binary)) + binary[2:]
    print("#%d %s" %(tc, arr))
