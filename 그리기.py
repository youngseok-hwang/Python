
# 타원형을 그리기 전에 사각형을 그리는 좌표 2개를 먼저 설정한다.
# 그 후에 사각형의 각 변에 접하는 타원형을 그린다.

# 타원 그리기

from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_oval(10, 10, 200, 150)
window.mainloop()

# 호 그리기

from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_arc(10, 10, 200, 150, extent=45, style=ARC)
window.mainloop()

# 반복문을 사용하여 각도를 증가시키면서 호 그리는 프로그램

from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
for degree in range(0, 360, 30):
    canvas.create_arc(10, 10+degree//5, 200, 150+degree//5, extent=degree, style=ARC)
window.mainloop()

# 다각형 그리기

from tkinter import *
window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")
window.mainloop()

from tkinter import *

w = 300
h = 200
window = Tk()

w = Canvas(window, width=w, height=h)
w.pack()

points = [0, 0, 80, 150, 250, 20]
w.create_polygon(points, outline="red", fill="yellow", width=5)

window.mainloop()

# 텍스트 그리기

from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_text(100, 100, text='싱 스트리트(Sing Street)', fill='blue')
window.mainloop()

# 폰트 설정

from tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=200)
canvas.pack()
canvas.create_text(250, 10, text='Sing Street(싱 스트리트)', fill='blue', font=('Courier', 20))
canvas.create_text(250, 100, text='Sing street', fill="red", font=('Hevetica', 30))
canvas.create_text(250, 150, text='Sing Street', font=('Times', 40), fill='green')
window.mainloop()


from tkinter import *
window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

img = PhotoImage(file="C:\\Users\yaung\Desktop\빌리.png")
canvas.create_image(20, 20, anchor=NW, image=img)

window.mainloop()


import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
id=canvas.create_oval(10, 100, 50, 150, fill="green")

for i in range(100):
    canvas.move(id, 3, 2)
    window.update()
    time.sleep(0.05)

def call_back(event):
    canvas.move(id, -10, 0)

from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

id = canvas.create_oval(10, 100, 50, 150, fill="green")

def move_right(event):
    canvas.move(id, 5, 0)
canvas.bind_all('<KeyPress-Right>', move_right)



