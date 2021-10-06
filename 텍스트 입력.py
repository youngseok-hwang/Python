
from tkinter import *

window = Tk()
Label(window, text="이름").grid(row=0)  # 테이블 0번째 행, 0번째 열
Label(window, text="나이").grid(row=1)  # 테이블 1번째 행, 0번째 열

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)  # 테이블 0번째 행, 1번째 열
e2.grid(row=1, column=1)  # 테이블 1번째 행, 1번째 열

window.mainloop()


from tkinter import *

def show():
    print("이름: %s\n나이: %s" % (e1.get(), e2.get()))

parent = Tk()
Label(parent, text="이름").grid(row=0)
Label(parent, text="나이").grid(row=1)

e1 = Entry(parent)
e2 = Entry(parent)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(parent, text="보이기", command=show).grid(row=3, column=1, sticky=W, pady=4)
Button(parent, text="종료", command=parent.quit).grid(row=3, column=0, sticky=W, pady=4)

mainloop()


from tkinter import *
window = Tk()
T = Text(window, height=5, width=60)
T.pack()
T.insert(END, "테스트 위젯은 여러 줄의 \n텍스트를 표시할 수 있습니다.")  # END: 텍스트 끝부분에 추가한다는 의미
window.mainloop()





