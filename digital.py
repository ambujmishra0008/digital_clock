from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="red")
label = Label(window,text="Adarsh Clock", font=("Arial Black", 78, "bold"), bg="steelblue")
label.pack(pady=100)
window.mainloop()
