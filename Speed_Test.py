from tkinter import *
import speedtest

sp = Tk()
sp.title(" Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="White")

label = Label(sp, text="Internet Speed Test", font=("serif", 20))
label.place(x=60, y=40, height=50, width=380)

label = Label(sp, text="Download Speed", font=("serif", 20))
label.place(x=60, y=130, height=50, width=380)

label = Label(sp, text="00", font=("serif", 20))
label.place(x=60, y=200, height=50, width=380)

label = Label(sp, text="Upload Speed", font=("serif", 20))
label.place(x=60, y=290, height=50, width=380)

label = Label(sp, text="00", font=("serif", 20))
label.place(x=60, y=360, height=50, width=380)


sp.mainloop()