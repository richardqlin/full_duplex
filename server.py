import socket

import threading
from tkinter import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)

root =Tk()

root.title('sever')

frame = Frame(root, width =300)
frame.pack()


conn, addr = s.accept()
print(addr)

def send_data():
    data = entry.get()
    chat = Label(root, text=data, fg='green',bg='black', anchor='e')
    chat.pack(side=TOP, fill=X)
    conn.sendall(data.encode())
    entry.delete(0, END)

def get_data():
    while 1:
        data = conn.recv(1024).decode()
        print(data)
        chat = Label(root, text=data, fg='red',bg='black', anchor='w')
        chat.pack(side=TOP, fill=X)
    conn.close()
recp = threading.Thread(target=get_data)
recp.start()

send = Button(root,text = 'Send', command = send_data)
send.pack(side =BOTTOM)
entry = Entry(root)
entry.pack(side =BOTTOM, fill=BOTH)
root.mainloop()








