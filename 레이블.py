
from tkinter import *

window = Tk()
photo = PhotoImage(file="빌리.png")  # 해당 파이썬 파일과 같은 폴더 내에 있어야 불러오기 가능
w = Label(window, image=photo)
w.photo = photo
w.pack()
window.mainloop()

from tkinter import *

window = Tk()
photo = PhotoImage(file="빌리.png")
w = Label(window, image=photo).pack(side="right")  # Label()은 제목 설정, .pack()은 적절하게 크기조절, side="right"는 오른쪽 정렬
message="""삶이 그대를 속일지라도 슬퍼하거나 노하지말라 !
우울한 날들을 견디면 : 믿으라,
기쁨의 날이 오리니.
마음은 미래에 사는 것
현재는 슬픈 것:
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.
"""
w2 = Label(window, justify=LEFT, padx=10, text=message).pack(side="left")  # side="left"는 레이블 왼쪽 정렬
window.mainloop()

from tkinter import *

window = Tk()

Label(window, text="Times Font 폰트와 빨강색을 사용합니다.", fg="red", font="Times 32 bold italic").pack()
Label(window, text="Helvetica 폰트와 녹색을 사용합니다.", fg="blue", bg="yellow", font="Helvetica 32 bold italic").pack()

window.mainloop()


