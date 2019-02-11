# Homework 14 - Django

2019-02-11



1. Django는 요청에 대한 응답을 해줄 때 허용하는 도메인에게만 응답을 해주도록 설정한다. Settings.py 파일에서 도메인을 허용하기 위해 수정해줘야하는 변수 이름을 찾아서 적어주세요.

> INSTALLED_APPS



2. https://`<your-server-url>`/ssafy로 요청이 들어왔을 때 응답을 해주기 위해 urls.py에 추가해주어야할 코드를 작성하세요. (실행하는 함수는 views.py 안에 있는 ssafy 함수라고 가정한다.)

> path('ssafy/', views.ssafy)



3. Django 서버를 실행시키는 명령어를 작성해주세요. (c9환경에서)

> python manage.py runserver $IP:$PORT



4. django는 MTV로 이루어진 web framework이다. MTV가 무엇의 약자인지 작성하세요.

> Model, Template, View

