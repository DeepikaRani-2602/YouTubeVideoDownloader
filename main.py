from tkinter import *
from tkinter import filedialog
import pytube

import shutil
from moviepy import *
#pytube-->Youtube
#moviepy-->shutil



root=Tk()

def directory():#select button
    folder_path=filedialog.askdirectory()#c:\desktop\html
    select_label.config(text=folder_path)


def download():#download button
    destpath=select_label.cget("text")
    Youtubeurl = url_path.get()  # https://www.youtube.com/watch?v=jX3aHRNAkPs&list=PLZnxqowr6IKjAKo3wmBBgjUgfFejvqho_
    video = pytube.YouTube(Youtubeurl).streams.get_highest_resolution()
    video.download()
    updatedvideo=VideoFileClip(video)
    updatedvideo.close()
    shutil.move(updatedvideo,destpath)
    finalconfirm.config(text="Video is downloaded successfully!!")


canvas=Canvas(root,width=400,height=400)
canvas.pack()


title_label=Label(root,text="Video Downloader",fg="blue")
canvas.create_window(200,15,window=title_label)

url_path=Entry(root,width=30)
canvas.create_window(200,90,window=url_path)

url_label=Label(text="Enter the link here:",font="Arial")
canvas.create_window(200,50,window=url_label)



b=Button(root,text="select",fg="red",command=directory)

canvas.create_window(200,200,window=b)

select_label=Label(root,text="select the path where the video should get downloaded")
canvas.create_window(200,170,window=select_label)


download_button=Button(root,text="Download",fg="olive",command=download)
canvas.create_window(200,260,window=download_button)


finalconfirm=Label(root,text="Video is not yet downloaded!!")
canvas.create_window(200,300,window=finalconfirm)

root.mainloop()
