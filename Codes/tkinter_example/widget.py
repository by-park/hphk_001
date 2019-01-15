# import tkinter 쓰면 아래에서 부를 때마다 tkinter. 쓰기 귀찮으니까!
from tkinter import *
# 버튼 누르면 brower 켜지게 할 거임
import webbrowser

# 이 함수를 button의 세 번째 인자로 넣어줄 수 있다.
def browser():
    webbrowser.open("https://www.daum.net")

# root라는 윈도우를 만들었다.
root = Tk()

# Label(어떤 tkinter 윈도우/프로그램에 넣을지, text = "")
# label = Label이라는 클래스를 이니셜라이즈!
label = Label(root, text = "Hello", fg="red", bg="blue")
label2 = Label(root, text = "John Kang's widget")

# 버튼 만들기 (라벨 만드는 과정과 비슷하다)
# command에 버튼 눌렸을 때 작동할 함수 이름을 그대로 써준다.
btn = Button(root, text="This is a button", command = browser)

# 좌표값 지정 (.pack()이라는 메소드, 가장 위에서부터 쌓아나가준다.)
label.pack()
label2.pack()
btn.pack()

# 사람들의 클릭이 있을 때, 그걸 계속 확인하고 실행해주는 조그만 위젯
root.mainloop()

