# Typora 사용법

##### 2 주차 2018-12-17

#을 쓰고 엔터를 치면 큰 글씨가 나온다. ##후 엔터를 치면 조금 더 작은 큰 글씨가 나온다.

-를 쓰고 엔터를 치면 검은 점이 나온다. 탭으로 들여쓰면 흰색 동그라미가 되며 들여쓰기가 된다.

1.2.3.으로 하면 ordered list도 가능하다.

`를 3번 이어 쓰고 python이라고 쓰고 엔터를 치면 코드 블록이 생긴다.

*를 글자 앞 뒤에 붙여주면 이탤릭체가 되면서 파일이름을 알려주는 용도로 쓸 수 있다. (코드블럭 안에 #app.py 도 가능하다)

*2개씩을 붙여서 감싸면 bold처리가 된다.

링크는 [쓰고 싶은 내용]를 열고 닫은 후 바로 붙여서 ()

위와 같은 형식에 맨 앞에 !를 붙이면 이미지가 들어간다.



# Git 사용법

##### 2 주차 2018-12-17

1. [깃 설치 페이지 접속](https://git-scm.com/download/win)
2. git bash 켜기
3. git 파일을 관리할 폴더 만들기

```git
$ cd Documents/
$ mkdir week2
$ cd week2
$ mkdir day1
$ cd day1
```

4. readme.md 파일 만들어보기

```git bash
$ touch readme.md
```

5. [github 가입하기](https://github.com/)
6. 내가 만든 파일 업로드하기

``` git bash
$ pwd 현재 위치가 잘못되었다면 $ cd Documents/week2/day1
$ git init
$ git add .
$ git commit -m "first commit" 을 치면 오류가 난다. 다음의 두 줄을 작성한다.

$ git config --global user.email "you@example.com"
$ git config --global user.name "name"
이메일과 이름은 모두 깃헙에 들어간 이름으로 지정한다.

$ git remote ~ create respository를 했을 때 메인 화면에 나온 이 부분을 복사한다.
$ git push ~ 마찬가지로 이 부분도 복사한다. 그리고 로그인 화면이 뜨면 로그인한다.

$ git add .
$ git commit -m "second commit"
$ git push
```

cf. 달라진 git 내용을 보기 위해서는 git status나 git diff를 쳐보면 된다.



# 파이썬 기초

##### 2 주차 2018-12-17

변수

```python
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+key

data = requests.get(url).json()
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15
wind = float(data['wind']['speed'])
visibility = float(data['visibility'])

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다. 
현재 풍속은 {:.1f}m/s이고, 가시거리는 {}m 입니다.
""".format(weather, temp, temp_min, temp_max, wind, visibility)
)
```



조건문

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%84%9C%EC%9A%B8&ServiceKey={}&ver=1.3&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
print(soup('item'))

gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

# 조건문
condition = ""
if (dust > 150):
  condition = "매우 나쁨"
elif (80 < dust <= 150):
  condition = "나쁨"
elif (30 < dust <= 80):
  condition = "보통"
else:
  condition = "좋음"
print("오늘의 미세먼지 농도는 " + condition + "입니다.")
```



반복문

```python
dish = ["삼겹살","꽃등심","파스타","뚝배기 불고기","폭찹"]

# 1. for문을 이용해서 dish에 담겨있는 모든 음식을 먹는 코드를 작성
for food in dish:
  print("배가 고프니 {}을(를) 먹어야겠다.".format(food))
  
# 2. for문과 while문을 이용해서 dish에 담겨있는 모든 음식을 두번씩 먹는 코드를 작성
for food in dish:
  eating_count = 0
  while eating_count < 2:
    print("배가 고프니 {}을(를) 먹어야겠다.".format(food))
    eating_count = eating_count + 1
```



내장함수

```python
import random

# 리스트
menu = ["순남시레기","멀티캠퍼스 20층","양자강","강남목장", "시골집"]
# 딕셔너리
menu_detail = {"순남시레기":"시레기국, 보쌈","멀티캠퍼스 20층":"오늘의 메뉴",
               "양자강":"차돌짬뽕","강남목장":"뚝배기 불고기","시골집":"쌈밥정식"}

lunch = random.choice(menu)

# 문자열에 +는 문자열을 합친다는 의미
print(lunch + "에서는 " + menu_detail[lunch] + "이(가) 먹을만 합니다.")
```



