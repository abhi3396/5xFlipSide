from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import encrypt_window
import decrypt_window

def encrypt_menu():
    box.destroy()
    encrypt_window.encrypt_menu()

def decrypt_menu():
    box.destroy()
    decrypt_window.decrypt_menu()

box=Tk()
box.title('ENCRYPT IT')
box.geometry("500x250")
frame=Frame(box, width=500, height=300)
frame.pack()
frame.place(x=-60,y=0)
img=ImageTk.PhotoImage(Image.open("1.jpg"))
label=Label(frame,image=img)
label1=Label(box,text="Select one of the Choices")
label1.config(font=("Elephant", 20))
label1.pack()
label.pack()

b1=Button(box, text="ENCRYPT FILES", command=encrypt_menu)
b2=Button(box, text="DECRYPT FILES", command=decrypt_menu)
b3=Button(box, text="EXIT", command=box.destroy)
b1.place(x=211, y=100)
b2.place(x=211, y=150)
b3.place(x=241, y=200)
box.mainloop()
