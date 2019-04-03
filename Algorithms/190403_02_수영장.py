"""Solving Club"""
"""
수영장

2019.04.03 PBY 최초작성

"""

def usePool(cur, cursum, depth):
    global minvalue
    if cur >= depth: # 11월이나 12월에 사면 넘어갈 수도 있다.
        if cursum < minvalue:
            minvalue = cursum
        return
    # 1일짜리를 사면
    usePool(cur+1, cursum+months[cur]*tickets[0], depth)
    # 1달짜리를 사면
    usePool(cur+1, cursum+tickets[1], depth)
    # 3달짜리를 사면
    usePool(cur+3, cursum+tickets[2], depth)

T = int(input())
for tc in range(1, T+1):
    tickets = list(map(int, input().split()))
    months = list(map(int, input().split()))

    minvalue = tickets[-1]
    # 1일 이용 계획, 1달 이용 계획, 3달 이용 계획을 사는 경우
    usePool(0, 0, 12)
    print("#%d %d" %(tc, minvalue))
