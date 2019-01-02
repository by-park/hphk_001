# Jupyter notebook 설치

#### SSAFY 2019-01-02

- pip --version을 확인한다.

- pip (python package installer 를 뜻한다.) 가 잘 설치되어 있으면  pip install jupyter를 통해 쉽게 설치할 수 있다.

- 주피터 노트북을 열어보기 위해 clone or download 로 초록 색 버튼을 눌러서 주소를 복사한다.

- `cd ~`로 이동하고, `code . `을 열고 다음의 내용을 _.bashrc_로 저장한다. (.은 리눅스 시스템에서 숨김 파일을 의미한다.)

_.bashrc_

```bash
alias jn="jupyter notebook"
```

- 그리고 `source .bashrc`를 입력한다.

- 그러면 이제 jn 만 써도 jupyter notebook이 열린다!



# swexpertacademy 문제 풀기

#### SSAFY 2019-01-02

- code - problem - difficulty level 1을 누르고 두 번째 페이지에 있는 대각선 출력하기 문제를 선택한다.
- 언어를 pypy 5.9로 선택한 다음 원하는 코드를 써서 제출을 누른다.



# 백준 Online Judge 문제 풀기

#### SSAFY 2019-01-02

- 문제 - 단계별로 풀어보기 - 입/출력 받아보기 - Hello World 문제를 풀어본다.
- `print("Hello World!")`를 쓰고 제출한다.
- 문제 - 단계별로 풀어보기 - 입/출력 받아보기 - A+B 문제를 풀어본다.
- 다음과 같이 작성하고 제출한다.

```python
a, b = list(map(int, input().split()))
print(a + b)
```

- 문제 - 단계별로 풀어보기 - 입/출력 받아보기 - 개 문제를 풀어본다.
- 이스케이프 문자와 관련된 문제이다.

```python
# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

print("""|\_/|
|q p|   /}
( 0 )\"""\\
|"^"`    |
||_/=\\\__|""")
```

