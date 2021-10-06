from tkinter import *

window = Tk()
choice = IntVar()

Label(window, text="가장 선호하는 프로그램 언어를 선택하시오.", justify = LEFT, padx=20).pack()
Radiobutton(window, text="Python", padx=20, variable=choice, value=1).pack(anchor=W)
Radiobutton(window, text="C", padx=20, variable=choice, value=2).pack(anchor=W)
Radiobutton(window, text="Java", padx=20, variable=choice, value=3).pack(anchor=W)
Radiobutton(window, text="Swift", padx=20, variable=choice, value=4).pack(anchor=W)

window.mainloop()


from tkinter import *

window = Tk()

select = IntVar()
select.set(1)

list=[("Python",1), ("C",2), ("Java",3), ("Swift",4)]

def PrintChoice():
    print(select.get())

Label(window, text="가장 선호하는 프로그래밍 언어를 선택하시오", justify = LEFT, padx = 20).pack()

for txt, val in list:
    Radiobutton(window, text=txt, padx=20, variable=select, command=PrintChoice, value=val).pack(anchor=W)

window.mainloop()


from tkinter import *

window = Tk()
Label(window, text="선호하는 언어를 모두 선택하시오:").grid(row=0, sticky=W)

value1 = IntVar()
Checkbutton(window, text="Python", variable=value1).grid(row=1, sticky=W)
value2 = IntVar()
Checkbutton(window, text="C", variable=value2).grid(row=2, sticky=W)
value3 = IntVar()
Checkbutton(window, text="Java", variable=value3).grid(row=3, sticky=W)
value4 = IntVar()
Checkbutton(window, text="Swift", variable=value4).grid(row=4, sticky=W)

window=mainloop()


from tkinter import *

window = Tk()

lb = Listbox(window, height=4)
lb.pack()
lb.insert(END, "Python")
lb.insert(END, "C")
lb.insert(END, "Java")
lb.insert(END, "Swift")

window.mainloop()



from tkinter import *

window = Tk()

sb = Scrollbar(window, orient=VERTICAL)
sb.pack(side = RIGHT, fill = Y)

lb = Listbox(window, height=4)
lb.pack()
lb.insert(END, "Python")
lb.insert(END, "C")
lb.insert(END, "Java")
lb.insert(END, "스위프트")
lb.insert(END, "GO")
lb.insert(END, "C++")
lb.insert(END, "C#")

sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

window.mainloop()