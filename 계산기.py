
from tkinter import *
from math import *
def calculate(evnet):
    label.configure(text="결과: " + str(eval(entry.get())))

window = Tk()
Label(window, text="파이썬 수식 입력:").pack()
entry = Entry(window)
entry.bind("<Return>", calculate)  # 엔트리 위젯에서 엔터키를 치면 calculate()가 호출된다.
entry.pack()
label = Label(window, text="결과:")
label.pack()

window.mainloop()







