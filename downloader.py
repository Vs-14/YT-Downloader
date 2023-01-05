from tkinter import *
from pytube import YouTube
from tkinter import messagebox

main = Tk() #main screen
main.title("YT Downloader")
main.geometry("300x100")
main.resizable(0,0)

choice = Label(main,text="Choose type of data to download",font=('Arial 10'),padx=50)
choice.grid(row=0,column=1)

v = StringVar()
v.set("Audio")

quality = [("Audio: Has only audio","Audio"),("Video: Has both audio and video","Video")]
c = 1
for text,val in quality:
    Radiobutton(main,text=text,value=val,variable=v).grid(row=c,column=1)
    c += 1

def next_btn(): #after choosing from audio/video
    ch = v.get()
    if(ch == "Video"):
        main.destroy() #destroys main screen and creates new for video
        video = Tk()
        video.title("YT Downloader")
        video.geometry("300x150")
        video.resizable(0,0)

        Label(video,text="Video Downloader",font=('Arial 14'),foreground="blue").grid(row=0,column=1)

        def click(event): #clears the link box when clicked
            if link_bar.get() == "Enter the link":
                link_bar.delete(0,END)

        global link_bar
        link_bar = Entry(video,width=20,borderwidth=5,font=('Arial 14'))
        link_bar.insert(0,"Enter the link")
        link_bar.bind("<FocusIn>", click)
        link_bar.grid(row=1,column=0,columnspan=3,padx=35)

        def vid_download():
            global link_bar
            link = link_bar.get()
            try:
                yt = YouTube(link)
                vid = yt.streams.get_highest_resolution() #720p
                vid.download()
                res = messagebox.showinfo("Downloaded","Video downloaded successfully") #closes after download
                if(res=="ok"):
                    video.destroy()
            except:
                res = messagebox.showerror("Invalid link","Invalid link please try again") #throws error when link does not work and ends
                if(res=="ok"):
                    video.destroy()

        download_btn = Button(video,text="Download",command=vid_download)
        download_btn.grid(row=2,column=1)
    else: #when audio is chosen
        main.destroy()
        audio = Tk()
        audio.title("YT Downloader")
        audio.geometry("300x150")
        audio.resizable(0,0)

        Label(audio,text="Audio Downloader",font=('Arial 14'),foreground="blue").grid(row=0,column=1)
        
        def click(event):
            if link_bar.get() == "Enter the link":
                link_bar.delete(0,END)
        
        link_bar = Entry(audio,width=20,borderwidth=5,font=('Arial 14'))
        link_bar.insert(0,"Enter the link")
        link_bar.bind("<FocusIn>", click)
        link_bar.grid(row=1,column=0,columnspan=3,padx=35,pady=(0,5))
        
        def music():
            link = link_bar.get()
            try:
                yt = YouTube(link)
                Label(audio,text="Downloading please wait").grid(row=3,column=1)
                aud = yt.streams.filter(mime_type="audio/mp4").first() #gets the first stream with mp4 and audio
                aud.download()
                res = messagebox.showinfo("Downloaded","Audio downloaded successfully") #closes after download
                if(res=="ok"):
                    audio.destroy()
            except:
                res = messagebox.showerror("Invalid link","Invalid link please try again") #throws error when link does not work and ends
                if(res == "ok"):
                    audio.destroy()
        
        d_btn = Button(audio,text="Download",command=music)
        d_btn.grid(row=2,column=1)

n_btn = Button(main,text="Next",command=next_btn)
n_btn.grid(row=3,column=1)

main.mainloop()