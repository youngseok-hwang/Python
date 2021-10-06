from tkinter import *

w = 500
h = 300

def drawDot(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="gray")

window = Tk()
canvas = Canvas(window, width=w, height=h)
canvas.pack(expand=YES, fill=BOTH)
canvas.bind("<B1-Motion>", drawDot)   # canvas에 bind 함수를 실행하면
                                      # 적용할 이벤트 하나를 정하고 정의된 이벤트의 함수를 옆에 써 넣으면 진행된다.

message = Label(window, text="마우스를 드래그하면 점들이 그려집니다.")
message.pack(side=BOTTOM)

window.mainloop()
