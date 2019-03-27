"""
11047 동전 0

문제에 배수라는 조건이 있기 때문에 그리디로 풀 수 있다.

2019.03.26 PBY 최초 작성

틀리는 경우 https://www.acmicpc.net/board/view/34962
2 100
1
100
"""

N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

cur_money = K
cnt = 0
# 가치의 합을 구하기
for item in coin[::-1]:
    if cur_money >= item: # 오마이갓 금액이 아예 같은 경우를 안 써줬다. > 로 해서 틀림
        temp = cur_money // item
        cur_money -= temp*item
        cnt += temp

    if cur_money == 0:
        break

print(cnt)
    
