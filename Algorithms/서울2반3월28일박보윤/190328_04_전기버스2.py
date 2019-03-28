def replaceBus(remain, cur, renum):
    global lenbattery, minvalue
    # 가지치기 추가 (for문 안에 넣지 말것 - break처럼 사용할 거 아니면)
    if renum >= minvalue:
        return
    
    # 현재 위치 중 갈 수 있는 곳을 간다.
    for i in range(cur+1, cur+remain+1):
        # 가봄
        if i >= lenbattery+1: # 배열크기는 1개 더 들어가 있다.
            if minvalue > renum:
                minvalue = renum
            return
        replaceBus(batteries[i], i, renum+1) 

T = int(input())
for tc in range(1, T+1):
    batteries = list(map(int, input().split())) # 첫번째는 정류장 수
    lenbattery = len(batteries)-1 # 배터리 수
    minvalue = lenbattery
    # 지금 충전기 양 & 현재 위치 & 교체횟수
    replaceBus(batteries[1], 1, 0)
    print("#%d %d" %(tc, minvalue))
    
"""
# 제한시간 초과
def replaceBus(remain, cur, renum):
    global lenbattery, minvalue
    # 현재 위치 중 갈 수 있는 곳을 간다.
    for i in range(cur+1, cur+remain+1):
        # 가봄
        if i >= lenbattery+1: # 배열크기는 1개 더 들어가 있다.
            if minvalue > renum:
                minvalue = renum
            return
            
        replaceBus(batteries[i], i, renum+1) 

T = int(input())
for tc in range(1, T+1):
    batteries = list(map(int, input().split())) # 첫번째는 정류장 수
    lenbattery = len(batteries)-1 # 배터리 수
    minvalue = lenbattery
    # 지금 충전기 양 & 현재 위치 & 교체횟수
    replaceBus(batteries[1], 1, 0)
    print("#%d %d" %(tc, minvalue))
"""

