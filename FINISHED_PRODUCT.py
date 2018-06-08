import os
from tkinter import filedialog
from tkinter import *

class State:
    def __init__(self):
        self.month = "01"
        self.year = "2000"
        self.directory = "/Users/hervinsagnep/Desktop/1"

    def setDir(self, directory):
        self.directory = directory
    
    def setYear(self, year):
        self.year = year
    
    def setMonth(self, month):
        self.month = month

root = Tk()
#STATE
s = State()
#STATUS BAR
status = Label(root,text="PDF SCANNER RENAME APP PROJECT JUNE 6, 2018",fg='grey')
status.grid(row=7,column= 5)

#=============LABELS====================================
#BATCHES LABELS
batches_label = Label(root,text="BATCHES")
batches_label.grid(row=3,column=0)
#OTHER LABELS
other_label = Label(root,text="OTHER")
other_label.grid(row=3,column=1)
#FORMAT LABELS
reformat_label = Label(root,text="REFORMAT")
reformat_label.grid(row=3,column=2)
#==========================================================================================
    
#=============BATCH:FUNCTIONS,BUTTON,LAYOUT================================================
#BRANCH FUNCTION(S)-BUTTON ATTRIBUTE-GRID BLOCK
def batch_1000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    for files in os.listdir():
        prefix_num = (files[:2])
        one_thousand_template = "DD-10XX"
        pdf = ".pdf"
        one_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, one_thousand_template, pdf))
        os.rename(files, one_thousand_format)
button_1000 = Button(root,text="1000",command=batch_1000)
button_1000.grid(row=4,column=0)

def batch_2000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    for files in os.listdir():
        prefix_num = (files[:2])
        two_thousand_template = "DD-20XX"
        pdf = ".pdf"
        two_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, two_thousand_template, pdf))
        os.rename(files, two_thousand_format)
button_2000 = Button(root,text="2000",command=batch_2000)
button_2000.grid(row=5,column=0)

def batch_6000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    for files in os.listdir():
        prefix_num = (files[:2])
        six_thousand_template = "MMDD-60XX"
        pdf = ".pdf"
        six_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, six_thousand_template, pdf))
        os.rename(files, six_thousand_format)
button_6000 = Button(root,text="6000",command=batch_6000)
button_6000.grid(row=6,column=0)

def batch_9000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    for files in os.listdir():
        prefix_num = (files[:2])
        nine_thousand_template = "MMDD-90XX"
        pdf = ".pdf"
        nine_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, nine_thousand_template, pdf))
        os.rename(files, nine_thousand_format)
button_9000 = Button(root,text="9000",command=batch_9000)
button_9000.grid(row=7,column=0)
#===================================================================================================

#=============OTHERS:FUNCTIONS,BUTTON,LAYOUT================================================
def nda():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    for files in os.listdir():
        prefix_num = (files[:2])
        nda = "NDA"
        nda_template = "DD"
        pdf = ".pdf"
        nda_format = ('{} {} {}-{}-{}{}'.format(prefix_num, nda, month, nda_template, year, pdf))
        os.rename(files, nda_format)
button_NDA = Button(root,text="NDA",command=nda)
button_NDA.grid(row=4,column=1)

def posting_report():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    for files in os.listdir():
        prefix_num = (files[:2])
        day = ("DD")
        posting_message = "POSTING REPORT.pdf"
        posting_format = ('{} {}-{}-{} {}'.format(prefix_num, month, day, year, posting_message))
        os.rename(files, posting_format)
button_posting_report = Button(root,text="POSTING REPORT",command=posting_report)
button_posting_report.grid(row=5,column=1)

def poundage_report():
    os.chdir(s.directory)
    for files in os.listdir():
        prefix_num = (files[:2])
        poundage_input = (input("BATCH NUMBER"))
        pdf = ".pdf"
        poundage_format = ('{} {}{}'.format(prefix_num, poundage_input, pdf))
        os.rename(files, poundage_format)
button_poundage_report = Button(root,text="POUNDAGE REPORT",command=poundage_report)
button_poundage_report.grid(row=6,column=1)

#===================================================================================================
#=============REFORMAT:FUNCTIONS,BUTTON,LAYOUT================================================
def reformat():
    os.chdir(s.directory)
    for files in os.listdir():
        prefix_rem = (files[3:])
        os.rename(files, prefix_rem)
button_reformat = Button(root,text="REFORMAT",command=reformat)
button_reformat.grid(row=4,column=2)

#===================================================================================================
#=============CHOOSE FILE================================================

var_year = StringVar()
label_year = Label(root, textvariable=var_year)
var_year.set("Year: " + s.year)
label_year.grid(row=2,column=2)

var_month = StringVar()
label_month = Label(root, textvariable=var_month)
var_month.set("Month: " + s.month)
label_month.grid(row=1,column=2)

var_dir = StringVar()
label_dir = Label(root, textvariable=var_dir)
var_dir.set("Directory: " + s.directory)
label_dir.grid(row=0,column=2)

def choose_file(var):
    s.setDir(filedialog.askdirectory(title = "Choose a directory", mustexist = True))
    var_dir.set("Directory: " + s.directory)
button_browse = Button(root,text="CHOOSE DIRECTORY",command=lambda: choose_file(var_dir))
button_browse.grid(row=0,column=1)



entry_month=Entry(root,bd=4)
entry_month.insert(0, s.month)
entry_month.grid(row=1,column=0)

def set_month(month, var):
    s.setMonth(month)
    var.set("Month: " + s.month)
button_month = Button(root,text="SET MONTH",command=lambda: set_month(entry_month.get(), var_month))	
button_month.grid(row=1,column=1)

entry_year=Entry(root,bd=4)
entry_year.insert(0, s.year)
entry_year.grid(row=2,column=0)

def set_year(year, var):
    s.setYear(year)
    var.set("Year: " + s.year)
button_year = Button(root,text="SET YEAR",command=lambda: set_year(entry_year.get(), var_year))
button_year.grid(row=2,column=1)

#===================================================================================================
root.mainloop()
