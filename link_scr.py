import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from dl_scr import DownloadScr
from pytube import YouTube
import urllib.request


class App:

    def __init__(self, root):

        #setting title
        root.title("Video Downloader")
        #setting window size
        width=615
        height=307
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        global link_ent
        link_ent = tk.Entry(root)
        link_ent["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        link_ent["font"] = ft
        link_ent["fg"] = "#808080"
        link_ent["justify"] = "center"
        link_ent["text"] = ""
        link_ent.place(x=50,y=100,width=509,height=46)
        link_ent.insert(0, 'URL of youtube video')


        def on_click(event):                    # Deletes placeholder when mouse click
            link_ent.configure(state=NORMAL)
            link_ent.delete(0, END)
            link_ent["fg"] = "black"
            # make the callback only work once
            link_ent.unbind('<Button-1>', on_click_id)

        on_click_id = link_ent.bind('<Button-1>', on_click)

        dl_btn = tk.Button(root)
        ft = tkFont.Font(family='Sans-serif',size=11)
        dl_btn["font"] = ft
        dl_btn["fg"] = "#fff"
        dl_btn["bg"] = "#5cb85c"
        dl_btn["justify"] = "center"
        dl_btn["text"] = "Downlaod Video"
        dl_btn.place(x=410,y=160,width=150,height=42)
        dl_btn["command"] = self.dl_btn_command

        root.mainloop()

    def dl_btn_command(self):

        def check4vid(link):
            try:
                yt = YouTube(link)
                return True
            except:
                return False

        def connection(host='http://youtube.com'):  # Check internet connection
            try:
                urllib.request.urlopen(host)  # Python 3.x
                return True
            except:
                return False

        if connection():
            link = link_ent.get()
            # link = 'https://www.youtube.com/watch?v=v-KNbMt0Dms'

            is_valid = check4vid(link)
            if is_valid:
                dl_window = Toplevel()
                link_ent.delete(0, tk.END)
                root.withdraw()
                app = DownloadScr(dl_window, link, root)
            else:
                tk.messagebox.showerror(title="Invalid Link", message="Try a different link")
        else:
            tk.messagebox.showerror(title="Network Error", message="Check your internet connection")

global root
root = tk.Tk()
app = App(root)


