import tkinter as tk

def startTimer():
    if (running):
        global timer  # 전역변수 timer 사용
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10, startTimer)  # 10ms 후 startTimer() 호출

def start():
    global running
    running = True

def stop():
    global running
    running = False

running = False

window = tk.Tk()

timer = 0

timeText = tk.Label(window, text="0", font=("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text="시작", bg="yellow", command=start)
startButton.pack(fill=tk.BOTH)

stopButton = tk.Button(window, text="중지", bg="yellow", command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
window.mainloop()

