from tkinter import Tk, Label
from datetime import datetime 
window = Tk()
window.title("Digital Adarsh Clock")
window.geometry("600x300")
window.configure(bg="red")
label = Label(window,text="Adarsh Clock", font=("Arial Black", 78, "bold"), bg="steelblue")
label.pack(pady=100)


def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500, clock)
clock()
window.mainloop()
print("thank you ambuj ji")
