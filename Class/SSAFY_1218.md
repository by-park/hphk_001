# 웹 크롤링

#### SSAFY 2주차 2018-12-18



1. 사용툴

   파이썬 챗봇



2. 작성 코드

오늘의 로또 번호를 지난 로또 당첨 번호와 비교하기

```python
import requests
import random
from bs4 import BeautifulSoup as bs

# url 에 요청 보내기
url = 'https://m.dhlottery.co.kr/common.do?method=main'
response = requests.get(url).text

# 필요한 데이터 뽑아내기
soup = bs(response, 'html.parser')
document = soup.select('.prizeresult')[0]
numbers = document.select('span')
ns = []
for number in numbers:
  ns.append(int(number.text))

# 랜덤 로또 번호 추출하기
lotto = sorted(random.sample(list(range(1,46)), 6))

count = 0
# 지난 주 당첨 숫자 배열을 한번씩 순회하면서
for num in ns:
# 내가 뽑아놓고 lotto 배열에서
  if num in lotto:
    count = count + 1
# 몇 개가 맞았는지 카운트 하기
print("이번주 추천 번호는 {} 입니다.".format(lotto))
print("지난주 번호와 비교했을 때 {}개가 일치합니다.".format(count))
```



네이버 웹툰 타이틀과 주소 크롤링해오기

```python
import requests
import time
from bs4 import BeautifulSoup as bs

# 오늘 요일
today = time.strftime("%a").lower()
# 1. 네이버 웹툰을 가져올 수 있는 주소 (url) 를 파악하고 url 변수에 저장한다.
url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today

# 2. 해당 주소로 요청을 보내 정보를 가져온다.
response = requests.get(url).text

# 3. 받은 정보를 bs를 이용해서 검색하기 좋게 만든다.
soup = bs(response, 'html.parser')

# 4. 네이버 웹툰 페이지로 가서 내가 원하는 정보가 어디에 있는지 파악한다.
toons = []
li = soup.select('.img_list li')
for item in li:
  toon = {
    "title": item.select('dt a')[0].text,
    "url": item.select('dt a')[0]["href"],
    "img_url": item.select('.thumb img')[0]["src"]
  }
  toons.append(toon)
    
# 5. 출력
print(toons)
```



