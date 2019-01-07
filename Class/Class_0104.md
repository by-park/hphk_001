# 네이버 번역 API 사용하기

#### 2019-01-04

_papago.py_

```python
# 네이버 (파파고)야 내가 단어 하나 전달할테니, 번역해줘

# 사용자에게 단어를 입력 받는다.
# 1. papago API 요청 주소에 요청을 보낸다.
# 2. 응답을 받아 번역된 단어를 출력한다.

import requests
from pprint import pprint as pp

naver_id = ""
naver_secret = ""

keyword = input("Please type any english word or phrase: ")

url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

data = {
    'source': 'en',
    'target': 'ko',
    'text': keyword
}

# res.json()
res = requests.post(url, headers=headers, data=data)
result = res.json()

pp(result['message']['result']['translatedText'])
# pp(result.get('message').get('result').get('translatedText'))

```



# 네이버 유명인 얼굴인식 API 사용하기

#### 2019-01-04

_face.py_

```python
# 번역할 단어를 clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req (파일)

# 1. requests를 통해 clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다.

import requests
from pprint import pprint as pp

naver_id = ""
naver_secret = ""

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

# 1. 해당하는 image_url에 요청을 보내서,
image_url = "https://pbs.twimg.com/profile_images/890240220242759680/D-rnLqu__400x400.jpg"
# 2. 파일데이터를 받아 저장해 둔다.
image_res = requests.get(image_url, stream=True)

files = {'image': image_res.raw.read()}

url = "https://openapi.naver.com/v1/vision/celebrity"

res = requests.post(url, headers=headers, files=files)
result = res.json() # json => dictionary

face = result.get('faces')[0].get('celebrity').get('value')
confidence = result.get('faces')[0].get('celebrity').get('confidence')

# xxx입니다. xx% 확신할 수 있습니다.
# str -> float -> round

print("{}입니다. {}% 확신할 수 있습니다.".format(face, round(float(confidence*100))))

```



# Flask로 페이크 궁합 사이트 만들기

#### 2019-01-04

pip를 이용하여 flask를 설치한 후에 다음과 같은 코드를 짠다.



_app.py_

```python
from flask import Flask, render_template, send_file, request
app = Flask(__name__)

from datetime import datetime as dt
import random

hogu = []

@app.route("/")  # 주문 받는 방법 (요청을 받는 방법)
def index():
#    return str(random.sample(range(1, 46), 6))
#    return send_file('home.html')
    lotto = random.sample(range(1, 46), 6)
    return render_template('index.html', lucky = lotto) # 서비스 주는 방법 (응답을 보내는 방법)

# /goonghap => 나와 상대방의 이름 + 페이크 궁합값(60-99)
@app.route("/goonghap")
def goonghap():
    # request: 사용자의 요청정보
    me = request.args.get('me')
    you = request.args.get('you')
    hogu.append([me, you])
    # [[강동주, 김지수], [강동주, 설현]]
    rating = random.randint(60, 99)
    return render_template('goonghap.html', me=me, you=you, rating=rating)

@app.route("/god")
def god():
    return str(hogu)
```



_templates/goonghap.html_

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>궁합</title>
</head>
<body>
    <h1> {{me}} 님과 {{you}}님의 궁합은 {{rating}}%입니다.</h1>
</body>
</html>
```



git bash에서 flask run을 치면 크롬에서 localhost:5000/으로 작성된 코드가 돌아가는 것을 확인할 수 있다. 