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

global bar_root
bar_root = tk.Tk()
app = bar_root


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
prc_lbl["bg"] = "black"
prc_lbl.place(x=250, y=120, width=100, height=40)

#
# def fill_bar(bar_prc):
#     bar["value"] = bar_prc
#     prc_lbl["text"] = str(bar_prc) + "%"
#     bar_root.update_idletasks()

# fill_bar(25)
