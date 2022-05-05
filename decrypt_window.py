from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import encrypt_image
import document_encrypt
import text_encrypt

def image():
    def img_enc():
        encrypt_image.decrypter(passphrase,box1)                              
        
    box1=Tk()
    box1.title('DECRYPT IT')
    box1.geometry("600x400")
    label1=Label(box1,text="Enter 10 digit numeric pass-phrase")
    label1.config(font=("Elephant", 10))
    label1.pack()

    enb=Button(box1,text="Choose File To Decrypt", command=img_enc)
    enb.place(x=200, y=300)

    passphrase=Text(box1,height=1, width=63)
    passphrase.place(x=30, y=200)
    box1.mainloop()

def document():
    def doc_enc():
        document_encrypt.decrypter(passphrase,box1)
    box1=Tk()
    box1.title('DECRYPT IT')
    box1.geometry("600x400")
    label1=Label(box1,text="Enter 10 digit numeric pass-phrase")
    label1.config(font=("Elephant", 10))
    label1.pack()

    enb=Button(box1,text="Choose File To Decrypt", command=doc_enc)
    enb.place(x=200, y=300)

    passphrase=Text(box1,height=1, width=63)
    passphrase.place(x=30, y=200)
    box1.mainloop()

def text():
    def text_enc():
        text_encrypt.decrypter(passphrase,box1)
    box1=Tk()
    box1.title('DECRYPT IT')
    box1.geometry("600x400")
    label1=Label(box1,text="Enter 10 digit numeric pass-phrase")
    label1.config(font=("Elephant", 10))
    label1.pack()

    enb=Button(box1,text="Choose File To Decrypt", command=text_enc)
    enb.place(x=200, y=300)

    passphrase=Text(box1,height=1, width=63)
    passphrase.place(x=30, y=200)
    box1.mainloop()

def decrypt_menu():
    box=Tk()
    box.title('DECRYPT IT')
    box.geometry("600x400")
    frame=Frame(box, width=500, height=300)
    frame.pack()
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("1.jpg"))
    label=Label(frame,image=img)
    label1=Label(box,text="What Do YOU Want To Decrypt")
    label1.config(font=("Elephant", 20))
    label1.pack()
    label.pack()

    b1=Button(box, text="IMAGE", command=image)
    b2=Button(box, text="DOCUMENT", command=document)
    b3=Button(box, text="TEXT", command=text)
  

    b1.place(x=282, y=150)
    b2.place(x=270, y=200)
    b3.place(x=288, y=250)
    box.mainloop()
