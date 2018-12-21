#  방탈출 까페 예약 시간 확인 챗봇 구현

##### SSAFY 2주차 2018-12-21

방탈출 예약 시간 확인하는 챗봇 만들기 (마스터키 & 서이룸)

```python
from flask import Flask, request
from bs4 import BeautifulSoup as bs
import requests
import json
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'

CAFE_LIST = {
    '전체': -1,
    '부천점': 15,
    '안양점': 13,
    '대구동성로2호점': 14,
    '대구동성로점': 9,
    '궁동직영점': 1,
    '은행직영점': 2,
    '부산서면점': 19,
    '홍대상수점': 20,
    '강남점': 16,
    '건대점': 10,
    '홍대점': 11,
    '신촌점': 6,
    '잠실점': 21,
    '부평점': 17,
    '익산점': 12,
    '전주고사점': 8,
    '천안신부점': 18,
    '천안점': 3,
    '천안두정점': 7,
    '청주점': 4
}


def get_total_info():
    url ="http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date' : '2018/12/21'
    }
    
    response = requests.get(url, params = params).text
    document = json.loads(response)
    cafe_code = {
        '강남1호점':3,
        '홍대1호점':1,
        '인천 부평점':4,
        '강남2호점':11,
        '홍대2호점':10,
        '부산 서면점':5
    }
    
    total = {}
    game_room_list = document["gameRoomList"]
    # 기본 틀 잡기
    for cafe in cafe_code:
        total[cafe] = []
        for room in game_room_list:
            if(cafe_code[cafe] == room["branch_id"]):
                total[cafe].append({"title": room["room_name"], "info":[]})
    
    # 앞에서 만든 틀에 데이터 집어넣기
    book_list = document["bookList"]
    
    for cafe in total:
        print(cafe)
        for book in book_list:
            if(cafe==book["branch"]):
                for theme in total[cafe]:
                    if (theme["title"] == book["room"]):
                        if (book["booked"]):
                            booked = "예약완료"
                        else:
                            booked = "예약가능"
                        theme["info"].append("{} - {}".format(book["hour"],booked))
    return total
    
def seoul_escape_list():
    total = get_total_info()
    return total.keys()
    
def seoul_escape_info(cd):
    total = get_total_info()
    cafe = total[cd]
    tmp = []
    for theme in cafe:
        tmp.append("{}\n {}".format(theme["title"], '\n'.join(theme["info"])))
    return tmp
    
def master_key_info(cd):
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    params = {
        'date': time.strftime("%Y-%m-%d"),
        'store': cd,
        'room': ''
    }
    response = requests.post(url, params).text
    document = bs(response,'html.parser')
    ul = document.select('.reserve .escape_view')
    theme_list = []
    for li in ul:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col'):
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        theme = {
            'title':title,
            'info':info
        }
    
        theme_list.append(theme)
    return theme_list

def master_key_list():
    url = 'http://www.master-key.co.kr/home/office'
    
    response = requests.get(url).text
    document = bs(response, 'html.parser')
    lis = document.select('.escape_list .escape_view')
    cafe_list = []
    for li in lis:
        title = li.select_one('p').text
        if (title.endswith('NEW')):
            title = title[:-3]
        address = li.select('dd')[0].text
        tel = li.select('dd')[1].text
        link = 'http://www.master-key.co.kr' + li.select_one('a')["href"]
        cafe = {
            'title':title,
            'tell': tel,
            'address': address,
            'link': link
        }
        cafe_list.append(cafe)
        print(cafe_list)
    
    return cafe_list

@app.route('/{}'.format(TELEGRAM_TOKEN), methods=['POST'])
def telegram():
    # 텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req = request.get_json()
    chat_id = req["message"]["from"]["id"]
    txt = req["message"]["text"]
    # 마스터키 전체
    # 마스터키 ****점
    if (txt.startswith('마스터키')):
        cafe_name = txt.split(' ')[1]
        cd = CAFE_LIST[cafe_name]
        if (cd > 0):
            data = master_key_info(cd)
        else:
            data = master_key_list()
        msg = []
        for d in data:
            msg.append('\n'.join(d.values()))
        msg = '\n'.join(msg)
        
    elif (txt.startswith('서이룸')):
        cafe_name = txt.split(' ')
        if (len(cafe_name)>2):
            # python howm to join middle of list
            cafe_name = ' '.join(cafe_name[1:3])
            if(cafe_name=="전체"):
                data= seoul_escape_list()
            else:
                data=seoul_escape_info(cafe_name)
        else:
            cafe_name = cafe_name[-1]
            if(cafe_name=="전체"):
                data= seoul_escape_list()
            else:
                data=seoul_escape_info(cafe_name)
        msg = '\n'.join(data)
    else:
        msg = '등록되지 않은 지점입니다.'
        
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

