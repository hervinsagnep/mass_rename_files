import os
from tkinter import filedialog
from tkinter import *
#HI
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
root.wm_title("File Rename Program | Hervin Sagnep 2018")
#STATE
s = State()
#STATUS BAR
"""
status = Label(root,text="PDF SCANNER RENAME APP PROJECT JUNE 6, 2018 | HERVIN SAGNEP",fg='grey')
status.grid(row=9,column=5)
"""
#=============LABELS====================================
#BATCHES LABELS
batches_label = Label(root,text="BATCHES:")
batches_label.grid(row=4,column=0)
#OTHER LABELS
other_label = Label(root,text="OTHER:")
other_label.grid(row=4,column=1)
#DEVELOPMENT LABEL

merge_label = Label(root,text="DEVELOPMENT FILES:")
merge_label.grid(row=4,column=3)

"""
#FORMAT LABELS
reformat_label = Label(root,text="REFORMAT BATCHES/OTHER:")
reformat_label.grid(row=0,column=5)
"""
#FORMAT DEVELOPMENT LABELS
dev_label = Label(root, text="REFORMAT FILES:")
dev_label.grid(row=0,column=6)


#CUSTOM ENTRY LABELS

cus_label = Label(root, text="CUSTOM ENTRY:")
cus_label.grid(row=4,column=5)

#==========================================================================================
    
#=============BATCH:FUNCTIONS,BUTTON,LAYOUT================================================
#BRANCH FUNCTION(S)-BUTTON ATTRIBUTE-GRID BLOCK
def batch_1000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        one_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        one_thousand_format = ('{} {}{}{}-10{}{}'.format(prefix_num, year, month, one_thousand_template, batch_digits, pdf))
        os.rename(files, one_thousand_format)
        i = i + 1
button_1000 = Button(root,text="1000",command=batch_1000)
button_1000.grid(row=5,column=0)

def batch_2000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        two_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        two_thousand_format = ('{} {}{}{}-20{}{}'.format(prefix_num, year, month, two_thousand_template,batch_digits, pdf))
        os.rename(files, two_thousand_format)
        i = i + 1
button_2000 = Button(root,text="2000",command=batch_2000)
button_2000.grid(row=6,column=0)

def batch_6000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        six_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        six_thousand_format = ('{} {}{}{}-60{}{}'.format(prefix_num, year, month, six_thousand_template,batch_digits, pdf))
        os.rename(files, six_thousand_format)
        i = i + 1
button_6000 = Button(root,text="6000",command=batch_6000)
button_6000.grid(row=7,column=0)

def batch_9000():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        nine_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        nine_thousand_format = ('{} {}{}{}-90{}{}'.format(prefix_num, year, month, nine_thousand_template,batch_digits, pdf))
        os.rename(files, nine_thousand_format)
        i = i + 1
button_9000 = Button(root,text="9000",command=batch_9000)
button_9000.grid(row=8,column=0)
#===================================================================================================

#=============OTHERS:FUNCTIONS,BUTTON,LAYOUT================================================
def nda():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        nda = "NDA"
        nda_template = input("DD")
        pdf = ".pdf"
        nda_format = ('{} {} {}-{}-{}{}'.format(prefix_num, nda, month, nda_template, year, pdf))
        os.rename(files, nda_format)
        i = i + 1
button_NDA = Button(root,text="NDA",command=nda)
button_NDA.grid(row=5,column=1)

def posting_report():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        day = input("DD")
        posting_message = "POSTING REPORT.pdf"
        posting_format = ('{} {}-{}-{} {}'.format(prefix_num, month, day, year, posting_message))
        os.rename(files, posting_format)
        i = i + 1
button_posting_report = Button(root,text="POSTING REPORT",command=posting_report)
button_posting_report.grid(row=6,column=1)

def poundage_report():
    os.chdir(s.directory)
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        poundage_input = (input("BATCH NUMBER"))
        pdf = ".pdf"
        poundage_format = ('{} {}{}'.format(prefix_num, poundage_input, pdf))
        os.rename(files, poundage_format)
        i = i + 1
button_poundage_report = Button(root,text="POUNDAGE REPORT",command=poundage_report)
button_poundage_report.grid(row=7,column=1)

#===================================================================================================
#=====================MERGE BUTTONS==============================================
#MERGE/DEVELOPMENT FUNCTION AND GRID

def batch_1000_A():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i+1
        prefix_num = ('{0:03d}').format(dev_pre)
        one_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        suffix = "D"
        one_thousand_format = ('{} {}{}{}-10{} {}{}'.format(prefix_num, year, month, one_thousand_template,batch_digits,suffix, pdf))
        os.rename(files, one_thousand_format)
        i = i+1
button_1000 = Button(root,text="1000",command=batch_1000_A)
button_1000.grid(row=5,column=3)

def batch_2000_A():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        two_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        suffix = "D"
        two_thousand_format = ('{} {}{}{}-20{} {}{}'.format(prefix_num, year, month,two_thousand_template,batch_digits,suffix,pdf))
        os.rename(files, two_thousand_format)
        i = i + 1
button_2000 = Button(root,text="2000",command=batch_2000_A)
button_2000.grid(row=6,column=3)

def batch_6000_A():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        six_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        suffix = "D"
        six_thousand_format = ('{} {}{}{}-60{} {}{}'.format(prefix_num, year, month, six_thousand_template,batch_digits,suffix,pdf))
        i = i + 1
        os.rename(files, six_thousand_format)
button_6000 = Button(root,text="6000",command=batch_6000_A)
button_6000.grid(row=7,column=3)

def batch_9000_A():
    os.chdir(s.directory)
    year = s.year
    month = s.month
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        nine_thousand_template = input("DD")
        batch_digits = input("BATCH DIGITS")
        pdf = ".pdf"
        suffix = "D"
        nine_thousand_format = ('{} {}{}{}-90{} {}{}'.format(prefix_num, year, month, nine_thousand_template,batch_digits,suffix, pdf))
        i = i + 1
        os.rename(files, nine_thousand_format)
button_9000 = Button(root,text="9000",command=batch_9000_A)
button_9000.grid(row=8,column=3)

#================================================================================
#=============REFORMAT:FUNCTIONS,BUTTON,LAYOUT================================================
"""
def reformat():
    os.chdir(s.directory)
    for files in os.listdir():
        prefix_rem = (files[7:])
        os.rename(files, prefix_rem)
button_reformat = Button(root,text="REFORMAT",command=reformat,fg="red")
button_reformat.grid(row=1,column=5)
"""
#===================================================================================================
#=============DEVELOPMENT REFORMAT:FUNCTIONS,BUTTON,LAYOUT================================================
def dev_reformat():
    os.chdir(s.directory)
    for files in os.listdir():
        prefix_rem = (files[4:])
        os.rename(files, prefix_rem)
button_reformat = Button(root,text="REFORMAT",command=dev_reformat,fg="red")
button_reformat.grid(row=1,column=6)

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
label_dir.grid(row=0,column=1)

def choose_file(var):
    s.setDir(filedialog.askdirectory(title = "Choose a directory", mustexist = True))
    var_dir.set("Directory: " + s.directory)
button_browse = Button(root,text="CHOOSE DIRECTORY",command=lambda: choose_file(var_dir))
button_browse.grid(row=0,column=0)

entry_month=Entry(root,bd=4)
entry_month.insert(0, s.month)
entry_month.grid(row=1,column=1)

def set_month(month, var):
    s.setMonth(month)
    var.set("Month: " + s.month)
button_month = Button(root,text="SET MONTH",command=lambda: set_month(entry_month.get(), var_month))	
button_month.grid(row=1,column=0)

entry_year=Entry(root,bd=4)
entry_year.insert(0, s.year)
entry_year.grid(row=2,column=1)

def set_year(year, var):
    s.setYear(year)
    var.set("Year: " + s.year)
button_year = Button(root,text="SET YEAR",command=lambda: set_year(entry_year.get(), var_year))
button_year.grid(row=2,column=0)
#============================CUSTOM ENTRY BUTTON AND LABEL=====================================================

def custom_entry():
    os.chdir(s.directory)
    i = 0
    for files in os.listdir():
        dev_pre = i + 1
        prefix_num = ('{0:03d}').format(dev_pre)
        enter_name = (input("ENTER CUSTOM BATCH NUMBER"))
        pdf = ".pdf"
        poundage_format = ('{} {}{}'.format(prefix_num, enter_name, pdf))
        os.rename(files, poundage_format)
        i = i + 1
custom_entry_button = Button(root,text="CUSTOM ENTRY",command=custom_entry)
custom_entry_button.grid(row=5,column=5)

#=============================================================================================================


#===================================================================================================
root.mainloop()


"""
ENSURE PROPER SCANNING OF FILES AND THAT THE SCANNED FILES ARE ALL IN THE SAME BATCH NUMBER TYPE, MISTAKES MAY ARISE WHERE THERE CAN BE A DOUBLE SCAN AND RENAMING WILL BECOME COMPLICATED
OR WILL CAUSE THE DELETION OF THE FILE IF IT IS RENAMED
"""

"""
THINGS TO ADD/FIX:
-ADD: CUSTOM ENTRY BUTTON: FIGURE OUT GRID LOCATION
-FIX: ELIMINATE THE NEED FOR THE NEED OF SPLICING REGULAR BATCH NUMBERS, IMPLEMENT THE BETTER
ORDERING SYSTEM SYNTAX. LOOK AT MERGE.
-FIX: FORMAT OF BUTTONS
-FIX: WHEN NEW NUMBERING SYSTEM FOR REGULAR BATCH NUMBERS IS IMPLEMENTED, ABLE TO HAVE SINGLE
FORMAT BUTTON INSTEAD OF 2


FORMAT BUTTON:

BUTTON
WHEN PRESSED RUN MESSAGE BOX
IF MESSAGE BOX == "YES" EXECUTE FORMAT
IF MESSAGE BOX == "NO" EXIT

"""