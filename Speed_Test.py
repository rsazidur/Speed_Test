from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    down_label.config(text=down)
    up_label.config(text=up)


sp = Tk()
sp.title(" Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="White")

label = Label(sp, text="Internet Speed Test", font=("Time New Roman", 20, "bold"))
label.place(x=60, y=40, height=50, width=380)

label = Label(sp, text="Download Speed", font=("Time New Roman", 20))
label.place(x=60, y=130, height=50, width=380)

down_label = Label(sp, text="00", font=("Time New Roman", 20), bg="Gray", fg="White")
down_label.place(x=60, y=200, height=50, width=380)

label = Label(sp, text="Upload Speed", font=("Time New Roman", 20))
label.place(x=60, y=290, height=50, width=380)

up_label = Label(sp, text="00", font=("Time New Roman", 20), bg="Gray", fg="White")
up_label.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Time New Roman", 20), relief=RAISED, bg="Gray", command=speedcheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
