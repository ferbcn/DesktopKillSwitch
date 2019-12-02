# TKDesktopKiller
# Kill Switch for Desktop Icons (hide all icons on Desktop)
# Works on: osX
# Dependencies: None (tkinter)

import os
from tkinter import *
from tkinter import PhotoImage

class Application(Frame):

    def __init__(self, master=None):
        self.icons_hidden = False
        self.img = PhotoImage(file="button.gif")
        Frame.__init__(self)
        self.createWidgets ()
        self.pack()


    def hide (self):
        if not self.icons_hidden:
            print ('Hiding Desktop Icons')
            os.system('defaults write com.apple.finder CreateDesktop false')
            self.icons_hidden = True
            self.button["text"] = "UNHIDE"
            self.button.config(bg="blue")
        else:
            print ('Showing Desktop Icons')
            os.system ('defaults write com.apple.finder CreateDesktop true')
            self.icons_hidden = False
            self.button["text"] = "HIDE"
            self.button.config(bg="grey")
        os.system('killall Finder')

    def createWidgets(self):
        self.button = Button(self)
        self.button.config(image=self.img)
        self.button["text"] = "HIDE"
        self.button["command"] =  self.hide
        #self.button.pack({"side": "top"})
        self.button.pack()


if __name__ == "__main__":
    root = Tk()
    root.geometry("150x145")
    root.title("Desktop Icons Kill Switch")
    app = Application(master=root)
    app.mainloop()
