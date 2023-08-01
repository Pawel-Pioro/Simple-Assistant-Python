from playsound import playsound
from tkinter import *
import webbrowser
from threading import Thread

# windows
window = Tk()
window.title('Virtual Assistant')

websiteInputWindow = Toplevel()
URLInputWindow = Toplevel()

website = StringVar()
URL = StringVar()

def start():
    window.deiconify()
    websiteInputWindow.withdraw()
    URLInputWindow.withdraw()
    Thread(target=lambda : playsound('greeting.mp3')).start()

def openWebsite():
    websiteInputWindow.deiconify()

def searchWebsite():
    webbrowser.open(f"https://www.google.com/search?q={website.get()}")
    Thread(target=lambda : playsound('openingWebsite.mp3')).start()

def openURLInputWindow():
    URLInputWindow.deiconify()

def openURL():
    webbrowser.open(URL.get())
    Thread(target=lambda: playsound('openingURL.mp3')).start()

#labels
websiteInputEntry = Entry(websiteInputWindow, textvariable=website, font=('Bold')).pack()
URLInputEntry = Entry(URLInputWindow, textvariable=URL).pack()
#buttons
openWebsiteButton = Button(window, text='Search the Internet', font=('Bold 15'), command=openWebsite).pack()
openURLInputButton = Button(window, text='Open URL', font=('Bold 15'), command=openURLInputWindow).pack()

websiteInputButton = Button(websiteInputWindow, text='Search', command=searchWebsite).pack()
openURLButton = Button(URLInputWindow, text='Open', font=('Bold 15'), command=openURL).pack()

start()
websiteInputWindow.mainloop()
window.mainloop()
