import os
from tkinter import filedialog
from tkinter import *



# HI
class State:
    def __init__(self):
        self.month = "0"
        self.year = "2018"
        self.directory = "SELECT FOLDER"

    def setDir(self, directory):
        self.directory = directory

    def setYear(self, year):
        self.year = year

    def setMonth(self, month):
        self.month = month


root = Tk()
root.wm_title("Parser Program")
# STATE
s = State()
l = []
newlist = []
def dev_reformat():
    os.chdir(s.directory)
    for f in os.listdir():
        print(f[9:13])

    #beg_range = int(input("BEG BATCH RANGE"))
    #end_range = int(input("END BATCH RANGE")) + 1
    #for x in range(beg_range, end_range):
        #newlist.append(list(range(beg_range, end_range)))
    #for i in newlist[0]:
        #print(i)


button_reformat = Button(root,text="PARSE BATCHES",command=dev_reformat,fg="red")
button_reformat.grid(row=2,column=0)

"""
EXCEL FORMULA
=IFERROR(INDEX($A$2:$A$1999,MATCH(0,IFERROR(MATCH($A$2:$A$1999,$B$2:$B$399,0),COUNTIF($C$1:$C1,$A$2:$A$1999)),0)),"")

"""

def dev_reformat_1():
    os.chdir(s.directory)
    for f in os.listdir():
        l.append(f)
        l.sort()
    for i in l:
        print(i)

button_reformat = Button(root,text="PARSE OTHERS",command=dev_reformat_1,fg="red")
button_reformat.grid(row=3,column=0)

def dev_reformat_2():
    beg_range = int(input("BEG BATCH RANGE"))
    end_range = int(input("END BATCH RANGE")) + 1
    for x in range(beg_range, end_range):
        print(x)
button_reformat = Button(root,text="BATCH RANGE",command=dev_reformat_2,fg="red")
button_reformat.grid(row=1,column=0)





var_dir = StringVar()
label_dir = Label(root, textvariable=var_dir)
var_dir.set("Directory: " + s.directory)
label_dir.grid(row=0,column=1)
def choose_file(var):
    s.setDir(filedialog.askdirectory(title = "Choose a directory", mustexist = True))
    var_dir.set("Directory: " + s.directory)
button_browse = Button(root,text="CHOOSE DIRECTORY",command=lambda: choose_file(var_dir))
button_browse.grid(row=0,column=0)

root.mainloop()
