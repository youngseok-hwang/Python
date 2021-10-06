# 격자 배치 관리자

from tkinter import *
window = Tk()
b1 = Button(window, text="One")
b2 = Button(window, text="Two")

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

l = Label(window, text="이것은 레이블입니다.")
l.grid(row=1, column=0)

window.mainloop()


# 압축 배치 관리자(박스 배치 가로)

from tkinter import *

window = Tk()

Label(window, text="박스 #1", bg="red", fg="white").pack()
Label(window, text="박스 #2", bg="green", fg="black").pack()
Label(window, text="박스 #3", bg="blue", fg="white").pack()

window.mainloop()

from tkinter import *

window = Tk()

w = Label(window, text="박스 #1", bg="red", fg="white")
w.pack(fill=X)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.pack(fill=X)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.pack(fill=X)

window.mainloop()


# 압축 배치 관리자(박스 배치 세로)

from tkinter import *

window = Tk()
w = Label(window, text="박스 #1", bg="red", fg="white")
w.pack(padx=5, pady=0, side=LEFT)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.pack(padx=5, pady=0, side=LEFT)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.pack(padx=5, pady=0, side=LEFT)

window.mainloop()


from tkinter import *

window = Tk()

w = Label(window, text="박스 #1", bg="red", fg="white")
w.place(x=0, y=0)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.place(x=20, y=20)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.place(x=40, y=40)

window.mainloop()


from tkinter import *

window = Tk()
f = Frame(window)  # 윈도우 안에 프레임 만들기

b1 = Button(f, text="One")  # 프레임 안에 버튼 만들기
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")

b1.pack(side=LEFT)  # 프레임은 압축 배치 관리자를 사용
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(window, text="이 레이블은 버튼들 위에 배치된다.")

l.pack()  # 레이블은 위도우 상단에 배치
f.pack()  # 프레임이 수직으로 쌓이게 됨

window.mainloop()





