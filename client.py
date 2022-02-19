import socket

import threading
from tkinter import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))

root = Tk()

root.title('client')
frame= Frame(root, width=300)

frame.pack()

def send_data():
    data = entry.get()
    chat = Label(root, text=data, fg='red', bg='black', anchor='e')
    chat.pack(side=TOP, fill=X)
    s.sendall(data.encode())
    entry.delete(0, END)

def get_data():
    while 1:
        data = s.recv(1024).decode()
        chat = Label(root,text = data,fg='green', bg='black', anchor='w')
        chat.pack(side= TOP,fill=X )
    s.close()

recp = threading.Thread(target=get_data)
recp.start()

send = Button(root, text = 'send', command = send_data)
send.pack(side =BOTTOM)
entry = Entry(root)
entry.pack(side=BOTTOM, fill=BOTH)
root.mainloop()


