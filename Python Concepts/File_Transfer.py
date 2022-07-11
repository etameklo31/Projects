import shutil
import os
import tkinter
from tkinter import messagebox
from tkinter import filedialog
import datetime
from datetime import timedelta
from datetime import datetime
from datetime import *

m = tkinter.Tk()
m.geometry("900x370")
m.title('File Transfer Module')

def chooseSource():
    #allows the user to choose the source folder, then saves the path to that folder to a variable named "source"
    source = filedialog.askdirectory()
    #inserts the "source" variable text into the Entry widget
    src.insert(0, source)

def chooseDestination():
    #allows the user to choose the source folder, then saves the path to that folder to a variable named "destination"
    destination = filedialog.askdirectory()
    #inserts the "destination" variable text into the Entry widget
    des.insert(0, destination)

def transfer_file():
    filepath1 = src.get()
    filepath2 = des.get()
    filenames = os.listdir(filepath1)
    for file in filenames:
        path = os.path.join(filepath1, file)
        seconds = os.path.getmtime(path)
        modtime = datetime.fromtimestamp(seconds)
        if modtime > (datetime.now()+timedelta(days = -1)):
            shutil.copy(path, filepath2)
    
b_chooseFile1 = tkinter.Button(m, text = "Browse1", width = 20, height = 3, command = chooseSource)
b_chooseFile1.grid(row = 0,column = 0,padx = (50, 10),pady = (50,50))

src = tkinter.Entry(m, width = 100)
src.grid(row=0, column=1, padx = 50, pady = 50)
       
b_chooseFile2 = tkinter.Button(m, text = "Browse2", width = 20, height = 3, command = chooseDestination)
b_chooseFile2.grid(row = 1,column=0,padx = (50, 10),pady = (10))

des = tkinter.Entry(m, width = 100)
des.grid(row=1, column=1, padx = 50, pady = 10)

b_chooseFile3 = tkinter.Button(m, text = "Browse3", width = 20, height = 3, command = transfer_file)
b_chooseFile3.grid(row=2,column=0,padx = (50, 10),pady = (50))


m.mainloop()



