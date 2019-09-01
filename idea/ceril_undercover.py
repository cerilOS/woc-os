import tkinter as tk, os, sys
from PIL import Image, ImageTk

if getattr(sys, 'frozen', False):
    # running in pyinstaller
    basedir = sys._MEIPASS
else:
    basedir = os.path.abspath(__file__)

class Application(tk.Frame):

    def __init__(self,master=None):

        self.current_path = os.path.abspath(os.path.dirname(basedir) + os.path.sep + '.')
        self.img_path = self.current_path + '\\data\\img\\'
        self.files = os.listdir(self.img_path)
        self.index = 0
        
        self.img = Image.open(self.img_path + self.files[self.index])
        self.converted_img = ImageTk.PhotoImage(self.img)

        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):

        self.lblImage = tk.Label(self, width=700, height=700)
        self.lblImage['image'] = self.converted_img
        self.lblImage.pack()

        self.f=tk.Frame()
        self.f.pack()

        self.indexDisplay = tk.Label(self.f, text = '1/20')
        self.indexDisplay.pack(side = tk.TOP)
        
        self.btnPrev = tk.Button(self.f, text='上一张', command=self.prev)
        self.btnPrev.pack(side = tk.LEFT)
        
        self.btnNext = tk.Button(self.f, text='下一张', command=self.next)
        self.btnNext.pack(side = tk.LEFT)


    def prev(self):
        self.showfile(-1)

    def next(self):
        self.showfile(1)


    def showfile(self,n):

        self.index += n
        
        if self.index < 0:
            self.index = len(self.files)-1
        if self.index > (len(self.files)-1):
            self.index = 0

        self.indexDisplay['text'] = '%d/%d' %(self.index + 1, len(self.files))

        self.img = Image.open(self.img_path + self.files[self.index])
        self.converted_img = ImageTk.PhotoImage(self.img)
        self.lblImage['image'] = self.converted_img
        
        
root=tk.Tk()
root.title('woc!')
app=Application(master=root)
app.mainloop()