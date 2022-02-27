import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from pytube import YouTube
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image
import os
import urllib.request
import io
import time


class DownloadScr:
    def __init__(self, root, link, old_root):

        def progress_Check(stream=None, chunk=None, bytes_remaining=None):
            # Gets the percentage of the file that has been downloaded.
            percent = (100 * (file_size - bytes_remaining)) / file_size
            fill_bar(percent, bytes_remaining)

        def create_bar():
            global bar_root
            bar_root = tk.Tk()

            # setting title
            bar_root.title("Video Downloader")
            # setting window size
            width = 615
            height = 200
            screenwidth = bar_root.winfo_screenwidth()
            screenheight = bar_root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            bar_root.geometry(alignstr)
            bar_root.resizable(width=False, height=False)

            global bar
            bar = ttk.Progressbar(bar_root, orient=HORIZONTAL, length=300)
            bar.place(x=0, y=80, width=615, height=40)
            global prc_lbl
            ft = tkFont.Font(family='Consolas', size=11)
            prc_lbl = tk.Label(bar_root)
            prc_lbl["font"] = ft
            prc_lbl.place(x=157, y=120, width=300, height=40)

        def fill_bar(bar_prc, bytes_remaining):
            bar["value"] = bar_prc
            prc_lbl["text"] = str("{:.2f}".format((file_size - bytes_remaining)/convert_rat)) + "/"\
                              + str("{:.2f}".format(file_size/convert_rat)) + size_name
            bar_root.update_idletasks()

        def is_exist():
            if os.path.exists(fpath_lbl["text"] + "/" + file_name):
                return True
            else:
                return False

        def get_convert_rat():

            global convert_rat, size_name
            if file_size >= 1073741824:
                convert_rat = 1024 * 1024 * 1024
                size_name = "GB"
            elif 1073741824 > file_size > 1000000:
                convert_rat = 1024 * 1024
                size_name = "MB"
            else:
                convert_rat = 1024
                size_name = "KB"

        def get_title(link):
            yt = YouTube(link)
            return yt.title

        def get_streams(link):
            yt = YouTube(link, on_progress_callback=progress_Check)
            return yt.streams

        def thumb_url(link):
            yt = YouTube(link)
            return yt.thumbnail_url

        def get_res(link):
            res_audio = []
            vid_streams = get_streams(link).filter(progressive=True)
            aud_streams = get_streams(link).filter(type="audio")
            print(len(aud_streams))
            for st in vid_streams:
                res_audio.append(st.resolution)
            for st in aud_streams:
                res_audio.append(int(st.abr[:-4]))
            res_audio[-1*(len(aud_streams)):] =  sorted(res_audio[-1*(len(aud_streams)):])  # Sorting MP3 values
            res_audio[-1*(len(aud_streams)):] = ["mp3-" + str(val) + "kbps" for val in res_audio[-1*(len(aud_streams)):]] # Concatenate "kbps" and "mp3" to MP3 values

            return res_audio

        def choose_folder():
            folder = filedialog.askdirectory()
            if folder:
                filepath = os.path.abspath(folder)
            if filepath:
                return filepath

        #setting title)

        root.title("Video Downloader")
        #setting window size
        width = 765
        height = 326
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        link_ent = tk.Label(root)
        link_ent["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        link_ent["font"] = ft
        link_ent["fg"] = "#333333"
        link_ent["justify"] = "center"
        global vid_title
        vid_title = get_title(link)
        if len(vid_title) > 45:
            link_ent["text"] = 9 * '.' + vid_title[0:40]
        else:
            link_ent["text"] = vid_title

        link_ent.place(x=80,y=35,width=320,height=34)

        def dl_btn_command():
            dl_res = res_choice.get()
            if dl_res[:4] == "mp3-":
                dl_res = dl_res[4:]
                print(dl_res)
            fpath = fpath_lbl["text"]
            if not dl_res or dl_res[-1] != "p":
                tk.messagebox.showerror(title="", message="Wrong Resolution Chosen")
            elif fpath_lbl["text"] == "Choose Filepath":
                tk.messagebox.showerror(title="", message="No File Path Chosen")
            else:
                try:
                    global ext
                    create_bar()
                    streams = get_streams(link)
                    if dl_res[len(dl_res)-1] == "p":
                        chosen_stream = streams.get_by_resolution(dl_res)
                        global file_name
                        file_name = streams.get_by_resolution(dl_res).default_filename
                        ext = ".mp4"
                    else:
                        chosen_stream = streams.filter(abr=dl_res).first()
                        ext = ".mp3"
                    if is_exist():
                        if tk.messagebox.askokcancel(title='Duplicate Files', message="Same file already exists would you like to overwrite it?"):
                            os.remove(fpath_lbl["text"]+ "/" + file_name)
                        else:
                            return None
                    global file_size
                    file_size = chosen_stream.filesize
                    get_convert_rat()
                    chosen_stream.download(fpath)
                except PermissionError:
                    tk.messagebox.showerror(title="Permission Denied", message="Choose a different filepath and try again")


        def loc_btn_command():
            fpath = choose_folder()
            fpath_lbl["text"] = fpath

        def back_btn_command():
            root.destroy()
            old_root.deiconify()

        dl_btn = tk.Button(root)
        ft = tkFont.Font(family='Sans-serif', size=11)
        dl_btn["font"] = ft
        dl_btn["fg"] = "#fff"
        dl_btn["bg"] = "#5cb85c"
        dl_btn["justify"] = "center"
        dl_btn["text"] = "Downlaod Video"
        dl_btn.place(x=570, y=240, width=166, height=40)
        dl_btn["command"] = dl_btn_command

        back_btn = tk.Button(root)
        ft = tkFont.Font(family='Sans-serif', size=11)
        back_btn["font"] = ft
        back_btn["fg"] = "#fff"
        back_btn["bg"] = "Grey"
        back_btn["justify"] = "center"
        back_btn["text"] = "Go Back"
        back_btn.place(x=445, y=240, width=120, height=40)
        back_btn["command"] = back_btn_command

        global res_choice
        res_choice = ttk.Combobox(root)
        ft = tkFont.Font(family='Times', size=10)
        res_choice["font"] = ft
        res_choice["justify"] = "center"
        res_choice["values"] = get_res(link)
        res_choice.place(x=540,y=160,width=160,height=30)

        GLabel_533 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_533["font"] = ft
        GLabel_533["fg"] = "#333333"
        GLabel_533["justify"] = "center"
        GLabel_533["text"] = "Resolution/MP3"
        GLabel_533.place(x=435, y=160, width=100, height=25)

        loc_btn = tk.Button(root)
        ft = tkFont.Font(family='Sans-serif', size=11)
        loc_btn["font"] = ft
        loc_btn["fg"] = "#fff"
        loc_btn["bg"] = "grey"
        loc_btn["justify"] = "center"
        loc_btn["text"] = "Location"
        loc_btn.place(x=440, y=100, width=70, height=25)
        loc_btn["command"] = loc_btn_command

        fpath_lbl = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        fpath_lbl["font"] = ft
        fpath_lbl["fg"] = "#333333"
        fpath_lbl["bg"] = "#fff"
        fpath_lbl["justify"] = "center"
        fpath_lbl["text"] = "Choose Filepath"
        fpath_lbl.place(x=510, y=100, width=210, height=25)

        with urllib.request.urlopen(thumb_url(link)) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        image = image.resize((320, 180), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        logo = tk.Label(root, image=image, anchor='center')
        logo.photo = image
        logo.place(x=80, y=80, width=320, height=180)

if __name__ == "__main__":
    dl = tk.Tk()
    app2 = DownloadScr(dl)
    dl.mainloop()
