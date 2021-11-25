from tkinter import *
from requests import get
import threading
import socket

ShowConfig = True
port = 9090

def GetIP():
    ip = get('https://api.ipify.org').text
    return ip

def Connect():
    print("test")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", port))


def OpenChat():
    window = Tk()
    window.title("ChatApp - connected")
    # window.geometry("400x600")

    name = Label(window, text="Username: ")
    ipname = Label(window, text="Your IP address: ")
    UserIP = Label(window, text=GetIP())
    NameInput = Entry(window)
    EnterIPText = Label(window, text="Enter IP address you want to connect: ")
    IPInput = Entry(window)

    ipname.grid(row=1, column=1)
    UserIP.grid(row=1, column=2)
    name.grid(row=2, column=1)
    NameInput.grid(row=2, column=2)
    EnterIPText.grid(row=3, column=1)
    IPInput.grid(row=3, column=2)

    SendBTN = Button(window, text="Connect")
    SendBTN.grid(row=5, column=2)

    window.mainloop()


WindowThread = threading.Thread(target=OpenChat)
SendThread = threading.Thread(target=Connect)


def OpenConfigWindow():
    window = Tk()
    window.title("ChatApp - config")
    # window.geometry("400x600")

    name = Label(window, text="Username: ")
    ipname = Label(window, text="Your IP address: ")
    UserIP = Label(window, text=GetIP())
    NameInput = Entry(window)
    EnterIPText = Label(window, text="Enter IP address you want to connect: ")
    IPInput = Entry(window)

    ipname.grid(row=1, column=1)
    UserIP.grid(row=1, column=2)
    name.grid(row=2, column=1)
    NameInput.grid(row=2, column=2)
    EnterIPText.grid(row=3, column=1)
    IPInput.grid(row=3, column=2)

    SendBTN = Button(window, text="Connect", command = lambda : [WindowThread.start(), SendThread.start()])
    SendBTN.grid(row=5, column=2)

    window.mainloop()




if ShowConfig:
    OpenConfigWindow()