# Github 페이지 구축

##### SSAFY 2 주차 2018-12-19

- Github에서 새 Repository를 만들고 아이디.github.io를 이름으로 설정한다.
- free Bootstrap templates을 다운받고 그것을 내가 원하는 폴더에 압축 푼 내용 전체를 복사해둔다. [템플릿 다운받기](https://startbootstrap.com/template-categories/all/)
- templates이 저장된 폴더와 github을 연결한다. (commit 방법은 2018-12-18 수업 참조)
- html 파일을 vscode로 열어서 편집한다.
- [구축된 깃헙 페이지 바로가기](https://by1994.github.io/)



# Cloud9 서버 환경 구축

##### SSAFY 2주차 2018-12-19

- 초대장을 받아 가입하지 않으면 유료로 서버를 만들어야 한다.
- 새  workspace 만들기: project name, public, blank template 선택

- 다음의 코드를 작성하여 파이썬을 설치한다. [코드 참고](<https://github.com/sspy2/install_python> )

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ source ~/.bashrc
```

- 위를 따라 python environment를 설치한 후에는 pyenv -v로 정상적으로 설치가 되었는지 확인한다.

```bash
$ pyenv install 3.6.7 # pyenv를 통해서 python 3.6.7을 설치 
$ pyenv global 3.6.7 # 전역으로 버전 설정
$ python -V # 파이썬 버전 확인
$ pyenv versions # 사용가능한 파이썬 버전 리스트 출력
```

- 코드 동작에 필요한 라이브러리도 설치한다.

```bash
$ pip install bs4
$ pip install requests
$ pip install flask
```



# FLASK를 이용한 서버 만들기

##### SSAFY 2주차 2018-12-19

- app.py 파일에 다음과 같이 작성한다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("Nice to meet you")
    return "Hello World"
    
```

- bash 에 다음을 작성하여 서버를 올린다.

```bash
$ flask run --host 0.0.0.0 --port 8080
```

- 위 주소에 접속하려면 shell에 뜬 주소 /index를 붙여주면 된다.
- 파일을 저장한 후에 서버를 껐다 키지않고 저장할 때마다 자동으로 서버가 꺼졌다가 업데이트 되도록 하기 위해서는 다음을 작성한다.

```bash
$ echo 'export FLASK_ENV=development' >> ~/.bashrc
$ source ~/.bashrc 
```

- 웹툰의 썸네일, 주소, 웹툰 링크를 정리해서 보여주는 페이지를 만든다.

*app.py*

```python
from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("Nice to meet you")
    return """
    <h1>index 타이틀</h1>
    <img src="http://newsimg.hankookilbo.com/2015/06/04/201506041864618664_1.jpg">
    <h3>SSAFY 화이팅 ㅎㅎ</h3>
    """
    
@app.route('/naver_toon')
def naver_toon():
    today = time.strftime("%a").lower()
    # 1. 네이버 웹툰을 가져올 수 있는 주소 (url) 를 파악하고 url 변수에 저장한다.
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' +  today
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
    return render_template('naver_toon.html', t = toons)

```

*naver_toon.html*

```html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1>Naver Webtoon 모아보기</h1>
        <table>
            <thead>
                <tr>
                    <th>썸네일</th>
                    <th>웹툰 제목</th>
                    <th>웹툰 링크</th>
                </tr>
            </thead>
            <tbody> 
                {% for toon in t: %}
                <tr>
                    <td><img src="{{toon["img_url"]}}"></td>
                    <td>{{toon["title"]}}</td>
                    <td><a href="{{toon["url"]}}">웹툰 보러가기</a></td>
                </tr>
                {% endfor %}
                </tbody>
        </table>
    </body>
</html>
```

