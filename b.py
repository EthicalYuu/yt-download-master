import tkinter as tk
from tkinter import font as tkfont
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from pytube import YouTube
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image
import os
import urllib.request
import io
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.title("ddd")

        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        # def get_title(link):
        #     yt = YouTube(link)
        #     return yt.title
        #
        # def get_streams(link):
        #     yt = YouTube(link)
        #     return yt.streams
        #
        # def thumb_url(link):
        #     yt = YouTube(link)
        #     return yt.thumbnail_url
        #
        # def get_res(link):
        #     res = []
        #     streams = get_streams(link).filter(progressive=True)
        #     for st in streams:
        #         res.append(st.resolution)
        #     return res
        #
        # def choose_folder():
        #     folder = filedialog.askdirectory()
        #     if folder:
        #         filepath = os.path.abspath(folder)
        #     if filepath:
        #         return filepath
        #
        # #setting title
        #
        #
        # link_ent = tk.Label(root)
        # link_ent["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times', size=14)
        # link_ent["font"] = ft
        # link_ent["fg"] = "#333333"
        # link_ent["justify"] = "center"
        #
        # if len(get_title(link)) > 45:
        #     link_ent["text"] = 9 * '.' + get_title(link)[0:40]
        # else:
        #     link_ent["text"] = get_title(link)
        #
        # link_ent.place(x=80,y=35,width=320,height=34)
        #
        # def dl_btn_command():
        #     dl_res = res_choice.get()
        #     fpath = fpath_lbl["text"]
        #     if not dl_res:
        #         tk.messagebox.showerror(title="", message="No Resolution Chosen")
        #     elif fpath_lbl["text"] == "Choose Filepath":
        #         tk.messagebox.showerror(title="", message="No File Path Chosen")
        #     else:
        #         try:
        #             streams = get_streams(link)
        #             chosen_stream = streams.get_by_resolution(dl_res)
        #             chosen_stream.download(fpath)
        #         except PermissionError:
        #             tk.messagebox.showerror(title="Permission Denied", message="Choose a different filepath and try again")
        #
        #
        # def loc_btn_command():
        #     fpath = choose_folder()
        #     fpath_lbl["text"] = fpath
        #
        # def loc_command():
        #     fpath = choose_folder()
        #     fpath_lbl["text"] = fpath
        #
        #     fpath = choose_folder()
        #     fpath_lbl["text"] = fpath
        #
        # dl_btn = tk.Button(self)
        # ft = tkFont.Font(family='Sans-serif', size=11)
        # dl_btn["font"] = ft
        # dl_btn["fg"] = "#fff"
        # dl_btn["bg"] = "#5cb85c"
        # dl_btn["justify"] = "center"
        # dl_btn["text"] = "Downlaod Video"
        # dl_btn.place(x=570, y=240, width=166, height=53)
        # dl_btn["command"] = dl_btn_command
        #
        # global res_choice
        # res_choice = ttk.Combobox(root)
        # ft = tkFont.Font(family='Times', size=10)
        # res_choice["font"] = ft
        # res_choice["justify"] = "center"
        # res_choice["values"] = get_res(link)
        # res_choice.place(x=540,y=160,width=160,height=30)
        #
        # GLabel_533 = tk.Label(root)
        # ft = tkFont.Font(family='Times', size=12)
        # GLabel_533["font"] = ft
        # GLabel_533["fg"] = "#333333"
        # GLabel_533["justify"] = "center"
        # GLabel_533["text"] = "Resolution"
        # GLabel_533.place(x=460, y=160, width=70, height=25)
        #
        # loc_btn = tk.Button(root)
        # ft = tkFont.Font(family='Sans-serif', size=11)
        # loc_btn["font"] = ft
        # loc_btn["fg"] = "#fff"
        # loc_btn["bg"] = "grey"
        # loc_btn["justify"] = "center"
        # loc_btn["text"] = "Location"
        # loc_btn.place(x=440, y=100, width=70, height=25)
        # loc_btn["command"] = loc_command
        #
        # fpath_lbl = tk.Label(root)
        # ft = tkFont.Font(family='Times', size=11)
        # fpath_lbl["font"] = ft
        # fpath_lbl["fg"] = "#333333"
        # fpath_lbl["bg"] = "#fff"
        # fpath_lbl["justify"] = "center"
        # fpath_lbl["text"] = "Choose Filepath"
        # fpath_lbl.place(x=510, y=100, width=210, height=25)
        #
        # with urllib.request.urlopen(thumb_url(link)) as u:
        #     raw_data = u.read()
        # image = Image.open(io.BytesIO(raw_data))
        # image = image.resize((320, 180), Image.ANTIALIAS)
        # image = ImageTk.PhotoImage(image)
        # logo = tk.Label(root, image=image, anchor='center')
        # logo.photo = image
        # logo.place(x=80, y=80, width=320, height=180)
        #
