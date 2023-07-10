
import tkinter 
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils
import tkinter as tk
import tkinter.ttk as ttk

stream = cv2.VideoCapture("video.mp4")
flag = True

def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

   
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def pending(decision):
    
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
  
    time.sleep(1.5)

   
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


SET_WIDTH = 650
SET_HEIGHT = 368


window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit")


frame = tkinter.Frame(window)
frame.pack()

cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(frame, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.grid(row=0, column=0, columnspan=4)




style = ttk.Style()
style.configure(
    "Custom.TButton",
    border=0,
    relief=tk.SOLID,
    padding=10,
    background="yellow",
    foreground="black",
)




frame = tk.Frame(window)
frame.pack(padx=10, pady=10)


btn = ttk.Button(
    frame,
    text="<< Previous (fast)",
    width=20,
    command=partial(play, -25),
    style="Custom.TButton",
)
btn.grid(row=1, column=0, padx=5, pady=5)

btn = ttk.Button(
    frame,
    text="<< Previous (slow)",
    width=20,
    command=partial(play, -2),
    style="Custom.TButton",
)
btn.grid(row=1, column=1, padx=5, pady=5)

btn = ttk.Button(
    frame,
    text="Next (slow) >>",
    width=20,
    command=partial(play, 2),
    style="Custom.TButton",
)
btn.grid(row=1, column=2, padx=5, pady=5)

btn = ttk.Button(
    frame,
    text="Next (fast) >>",
    width=20,
    command=partial(play, 25),
    style="Custom.TButton",
)
btn.grid(row=1, column=3, padx=5, pady=5)


button_frame = tk.Frame(window)
button_frame.pack(padx=10, pady=10)

btn = ttk.Button(
    button_frame,
    text="Give Out",
    width=20,
    command=out,
    style="Custom.TButton",
)
btn.grid(row=0, column=0, padx=5, pady=5)

btn = ttk.Button(
    button_frame,
    text="Give Not Out",
    width=20,
    command=not_out,
    style="Custom.TButton",
)
btn.grid(row=0, column=1, padx=5, pady=5)


window.mainloop()
