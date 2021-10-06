
from tkinter import *

window = Tk()

b1 = Button(window, text="이것이 파이썬 버튼입니다.")
b1.pack()

window.mainloop()

from tkinter import *

window = Tk()
b1 = Button(window, text="첫 번째 버튼")
b2 = Button(window, text="두 번째 버튼")
b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b1["text"] = "One"
b2["text"] = "Two"


window.mainloop()

from tkinter import *

def callback():
    button["text"] = "버튼이 클릭되었음!"

window = Tk()
button = Button(window, text="클릭", command=callback)
button.pack(side=LEFT)

window.mainloop()


from tkinter import *

window = Tk()

label = Label(window, text="안녕하세요!")
label.pack()

button = Button(window, text="tkinter로 버튼을 쉽게 만들 수 있습니다.")
button.pack()

window.mainloop()
