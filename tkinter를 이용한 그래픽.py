from tkinter import *
window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()

w.create_line(0, 0, 300, 200)  # (0, 0)에서 (300, 200)까지의 직선
w.create_line(0, 0, 300, 100, fill="red")  # (0, 0)에서 (300, 100)까지의 직선
w.create_rectangle(50, 25, 200, 100, fill="blue")  # (50, 25)에서 (200, 100)까지의 대각선을 채우는 사각형, 왼쪽 상단과 오른쪽 하단

window.mainloop()


from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

i = w.create_line(0, 0, 300, 200, fill="red")
w.coords(i, 0, 0, 300, 100)  # 좌표를 변경한다.  # 괄호 내 첫 번째 항목은 '변경하려는 대상' 을 의미, 나머지는 '변경하려는 좌표' 를 의미
w.itemconfig(i, fill="blue")   # 색상을 변경한다.

# w.delete(i): i를 삭제한다.
# w.delete(All): 모든 항목을 삭제한다.

window.mainloop()


from tkinter import *

window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()

w.create_rectangle(50, 25, 200, 100, outline="blue")
window.mainloop()


from tkinter import *

window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()

w.create_rectangle(50, 25, 200, 100, fill="#FA88AB")  # '#'기호는 16진수를 의미, #FA88AB는 15 10 8 8 10 11를 뜻함
window.mainloop()


# from tkinter import *

# window = Tk()
# w = Canvas(window, width=300, height=200)
# w.pack()
# color = colorchooser.askcolor()

# w.create_rectangle(50, 25, 200, 100, fill=color[1])
# window.mainloop()


from tkinter import *
window = Tk()
button = Button(window, text="버튼을 클릭하세요.")
button.pack()
button["fg"] = "#ff0000"
button["bg"] = "#00ff00"

window.mainloop()


