# Github 작업 환경 구축하기

#### SSAFY 2019-01-03

외부 컴퓨터와  홈 컴퓨터에서 동시에 작업을 할 때는, 반드시 pull 로 동기화를 해야한다. 

<img src="https://github.com/BY1994/hphk_001/tree/master/Images/image001.png">

처음에 이미 있는 내용을 받을 때는 git clone을 활용한다.

```bash
$ git init
$ git clone 깃헙 주소
```



> <b>github에 선별적으로 커밋하는 방법</b>
>
> 추가로 _.gitignore_  이라는 이름의 파일을 만들어서 무시하고 싶은 파일 이름들을 작성하면 github 가 먼저 돌면서 무시할 파일들은 push를 해주지 않는다.



# Github branch 만들기

#### SSAFY 2019-01-03

Github branch는 원래 작업하는 기준 선인 master말고, 가상 환경처럼 가지를 뻗어나온 것이다. 가상 환경처럼 따로 테스트를 해본 후에 괜찮으면 그때서야 정식 코드로, master 로 넣어주는 것이다.

<img src="https://github.com/BY1994/hphk_001/tree/master/Images/image002.png">

- `git branch`: 현재 있는 branch 목록을 확인할 수 있다.

- `git branch [새로운 브랜치 이름]`: 새 branch를 만들 수 있다.

- `git checkout [브랜치 이름]`: 해당 branch 로 이동해서 작업을 하게 된다.

```bash
$ git branch
$ git branch 새로 만들 브랜치 이름
$ git checkout 브랜치 이름
```



# 네이버 번역 API 연결하기

#### SSAFY 2019-01-03

API 서비스를 신청하고 다음과 같은 코드를 짠다.

```python
# 네이버 (파파고)야 내가 단어 하나 전달할테니, 번역해줘

# 사용자에게 단어를 입력 받는다.
text = input("단어를 입력해 주세요: ")
# 1. papago API 요청 주소에 요청을 보낸다.
# 2. 응답을 받아 번역된 단어를 출력한다.

import requests
naver_id = "" # 여기에 네이버에서 API 용으로 발급된 아이디와
naver_secret = "" # 발급된 비밀 키를 가져온다

url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

data = {
    'source': 'en',
    'target': 'ko',
    'text': text
}

# res.json()
res = requests.post(url, headers=headers, data=data)
res_json = res.json()
print(res_json['message']['result']['translatedText'])
```

