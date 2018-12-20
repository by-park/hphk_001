# 텔레그램 봇 만들기

##### SSAFY 2주차 2018-12-20

- 핸드폰으로 Telegram에 가입한다.
- Telegram Web에서 로그인한다. [Telegram](https://web.telegram.org/)
- 봇을 생성한다.
  1. Telegram 친구 검색에서 @botFather 검색
  2. 채팅으로 bot name과 username을 설정해서 토큰을 발급받는다.
- 토큰을 외부에 노출되지 않도록 환경변수로 설정한다.

```bash
$ vi ~/.bashrc
$ shift + g 맨 뒤로 가는 명령어
$ o 작성 가능(insert)
$ export TELEGRAM_TOKEN = 발급받은 키
$ esc 여러번 누르기
$ :wq 저장 종료
$ source ~/.bashrc
$ echo $TELEGRAM_TOKEN
```

- 텔레그램 챗봇 코드를 작성한다.

```bash
from flask import Flask, request
import requests
import json
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'

@app.route('/{}'.format(TELEGRAM_TOKEN), methods=['POST'])
def telegram():
    # 텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req = request.get_json()
    chat_id = req["message"]["from"]["id"]
    if (req["message"]["text"]=="안녕"):
        msg = "첫만남에는 존댓말을 써야죠!"
    elif (req["message"]["text"]=="안녕하세요"):
        msg = "인사 잘하신다 ㅋㅋㅋ"
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    requests.get(url, params = {"chat_id": chat_id, "text": msg})
    return '', 200

@app.route('/set_webhook')
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url' : 'https://computer-choco-bypark.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    response = requests.get(url, params = params).text
    return response

```

