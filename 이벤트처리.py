# 마우스 이벤트 // 파이썬 쉘

from tkinter import *

window = Tk()

def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()


# focus_set() 메소드 이용하여 위젯으로 포커스 이동

from tkinter import *

window = Tk()

def key(event):
    print(repr(event.char), "가 눌렸습니다.")   # repr()은 문자코드를 문자열로 변환시키는 함수

def callback(event):
    frame.focus_set()
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()

# 마우스 단일클릭, 더블클릭 처리

from tkinter import *

def sleft(event):
    print("단일 클릭, 왼쪽 클릭")

def dleft(event):
    print("더블 크릭, 왼쪽 클릭")

widget = Button(None, text='마우스 클릭')

widget.pack()

widget.bind('<Button-1>', sleft)
widget.bind('<Double-1>', dleft)

widget.mainloop()


# 마우스 모션 이벤트

from tkinter import *

def motion(event):
    print("마우스 위치: (%s %s)" % (event.x, event.y))
    return

window = Tk()
message = """당신 스스로 하지 않으면 아무도 당신의 운명을 개선시켜주지 않을 것이다."""

msg = Message(window, text = message)
msg.config(bg='yellow', fg='blue', font="times 20 italic")
msg.bind('<Motion>', motion)   # motion은 마우스 모션 이벤트 처리 함수이다.
msg.pack()

window.mainloop()

