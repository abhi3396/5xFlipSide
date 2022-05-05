from tkinter import *
from tkinter import filedialog, messagebox

def encrypter(passphrase,box):
    image=filedialog.askopenfile(mode='r', filetype=[('jpg file','*.jpg'),('png file','*.png'),('jpeg file','*.jpeg'),('gif file','*.gif')])
    if image is not None:
        name=image.name
        key=passphrase.get(1.0,END)
        print(key)
        if len(str(key)) != 11:
            messagebox.showerror('Input Error', '10 Digit Key Required')
        else:
            file=open(name,'rb')
            image1=file.read()
            file.close()
            key_str=str(key)
            image1=bytearray(image1)
            j=0
            k=2
            for x in range(5):
                key=key_str[j:k]
                j=j+2
                k=k+2
                for index,values in enumerate(image1):
                    image1[index]=values^int(key)
            file=open(name,'wb')
            file.write(image1)
            file.close()
            box.destroy()
            messagebox.showinfo("SUCCESS", "File Encrypted Successfully")
    else:
        messagebox.showerror('Input Error','DOCUMENT REQUIRED')
            
def decrypter(passphrase,box):
    image=filedialog.askopenfile(mode='r', filetype=[('jpg file','*.jpg'),('png file','*.png'),('jpeg file','*.jpeg'),('gif file','*.gif')])
    if image is not None:
        name=image.name
        key=passphrase.get(1.0,END)
        print(key)
        if len(str(key)) != 11:
            messagebox.showerror('Input Error', '10 Digit Key Required')
        else:
            file=open(name,'rb')
            image1=file.read()
            file.close()
            key_str=str(key)
            image1=bytearray(image1)
            j=8
            k=10
            for x in range(5):
                key=key_str[j:k]
                j=j-2
                k=k-2
                for index,values in enumerate(image1):
                    image1[index]=values^int(key)
            file=open(name,'wb')
            file.write(image1)
            file.close()
            box.destroy()
            messagebox.showinfo("SUCCESS", "File Decrypted Successfully")
    else:
        messagebox.showerror('Input Error','DOCUMENT REQUIRED')
