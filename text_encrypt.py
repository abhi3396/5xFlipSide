from tkinter import *
from tkinter import filedialog, messagebox

def encrypter(passphrase,box):
    doc=filedialog.askopenfile(mode='r', filetype=[('text file','*.txt'),('c file','*.c')])
    if doc is not None:
        name=doc.name
        key=passphrase.get(1.0, END)
        print(key)
        if len(str(key)) != 11:
            messagebox.showerror('Input Error','10 Digit Key Required')
        else:
            file=open(name,'rb')
            document=file.read()
            file.close()
            document=bytearray(document)
            key_str=str(key)
            j=0
            k=2
            for x in range(5):
                key=key_str[j:k]
                j=j+2
                k=k+2
                for index,values in enumerate(document):
                    document[index]=values^int(key)
            file=open(name,'wb')
            file.write(document)
            file.close()
            box.destroy()
            messagebox.showinfo("SUCCESS","File Encrypted Successfully")
    else:
        messagebox.showerror('Input Error','DOCUMENT REQUIRED')
                
def decrypter(passphrase,box):
    doc=filedialog.askopenfile(mode='r', filetype=[('text file','*.txt'),('c file','*.c')])
    if doc is not None:
        name=doc.name
        key=passphrase.get(1.0, END)
        print(key)
        if len(str(key)) != 11:
            messagebox.showerror('Input Error','10 Digit Key Required')
        else:
            file=open(name,'rb')
            document=file.read()
            file.close()
            document=bytearray(document)
            key_str=str(key)
            j=8
            k=10
            for x in range(5):
                key=key_str[j:k]
                j=j-2
                k=k-2
                for index,values in enumerate(document):
                    document[index]=values^int(key)
            file=open(name,'wb')
            file.write(document)
            file.close()
            box.destroy()
            messagebox.showinfo("SUCCESS","File Decrypted Successfully")
    else:
        messagebox.showerror('Input Error','DOCUMENT REQUIRED')
