# 자동화할 기능들을 파이썬으로 구현
import webbrowser
import sys

#url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C+%EC%97%B0%EC%9A%B0"
#webbrowser.open(url)

# sys.arg 우리가 입력한 명령어들이 다 들어가 있음
# =>  hello john
# => ["hello 파일 전체 경로", "john"]

#print(sys.argv)
# hello 입력받은 사람의 이름을 출력해 보세요.
# => hello john 실행시
# => hello john 출력

print("Hello " + sys.argv[1])