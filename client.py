import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from requests import get


def GetIP():
    ip = get('https://api.ipify.org').text
    return ip

HOST = GetIP()
PORT = 9090

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent = msg)
        self.gui_done = False

        self.running = True

        gui_thread = threading.Thread(target=gui_loop)
        receive_thread = threading.Thread(target=recive)

        gui_thread.start()
        receive_thread.start()