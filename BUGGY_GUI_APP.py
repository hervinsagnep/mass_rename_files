from tkinter import *
import os

#===========================FUNCTIONS===================================
root = Tk()
#BATCHES FUNCTIONS:
def batch_1000():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    year = (int(input("YEAR")))
    month = ((input("MONTH")))
    for files in os.listdir():
        prefix_num = (files[:2])
        one_thousand_template = "DD-10XX"
        pdf = ".pdf"
        one_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, one_thousand_template, pdf))
        os.rename(files, one_thousand_format)

def batch_2000():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    year = (int(input("YEAR")))
    month = ((input("MONTH")))
    for files in os.listdir():
        prefix_num = (files[:2])
        two_thousand_template = "DD-20XX"
        pdf = ".pdf"
        two_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, two_thousand_template, pdf))
        os.rename(files, two_thousand_format)

def batch_6000():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    year = (int(input("YEAR")))
    month = ((input("MONTH")))
    for files in os.listdir():
        prefix_num = (files[:2])
        six_thousand_template = "MMDD-60XX"
        pdf = ".pdf"
        six_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, six_thousand_template, pdf))
        os.rename(files, six_thousand_format)

def batch_9000():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    year = (int(input("YEAR")))
    month = ((input("MONTH")))
    for files in os.listdir():
        prefix_num = (files[:2])
        nine_thousand_template = "MMDD-90XX"
        pdf = ".pdf"
        nine_thousand_format = ('{} {}{}{}{}'.format(prefix_num, year, month, nine_thousand_template, pdf))
        os.rename(files, nine_thousand_format)

#OTHER FUNCTIONS:
def nda():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    year = (int(input("YEAR")))
    month = ((input("MONTH")))
    for files in os.listdir():
        prefix_num = (files[:2])
        nda = "NDA"
        nda_template = "DD"
        pdf = ".pdf"
        nda_format = ('{} {} {}-{}-{}'.format(prefix_num, nda, month, nda_template, year, pdf))
        os.rename(files, nda_format)

def posting_report():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    month = ((input("MONTH")))
    year = ((int(input("YEAR"))))
    for files in os.listdir():
        prefix_num = (files[:2])
        day = ("DD")
        posting_message = "POSTING REPORT.pdf"
        posting_format = ('{} {}-{}-{} {}'.format(prefix_num, month, day, year, posting_message))
        os.rename(files, posting_format)

def poundage_report():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    for files in os.listdir():
        prefix_num = (files[:2])
        poundage_input = (input("BATCH NUMBER"))
        pdf = ".pdf"
        poundage_format = ('{} {}{}'.format(prefix_num, poundage_input, pdf))
        os.rename(files, poundage_format)

#REFORMAT FUNCTION:
def reformat():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    for files in os.listdir():
        prefix_rem = (files[3:])
        os.rename(files, prefix_rem)

#=============GUI CODE=====================
#GUI ATTRIBUTES

#BATCHES ATTRIBUTES
batches_label = Label(root,text="BATCHES")
button_1000 = Button(root,text="1000",command=batch_1000)
button_2000 = Button(root,text="2000",command=batch_2000)
button_6000 = Button(root,text="6000",command=batch_6000)
button_9000 = Button(root,text="9000",command=batch_9000)

#OTHER ATTRIBUTES
other_label = Label(root,text="OTHER")
button_NDA = Button(root,text="NDA",command=nda)
button_posting_report = Button(root,text="POSTING REPORT",command=posting_report)
button_poundage_report = Button(root,text="POUNDAGE REPORT",command=poundage_report)

#REFORMAT ATTRIBUTES
reformat_label = Label(root,text="REFORMAT")
button_reformat = Button(root,text="1000",command=reformat)

#BATCHES GRID LAYOUT
batches_label.grid(row=0,sticky=E)
button_1000.grid(row=1,column=0)
button_2000.grid(row=2,column=0)
button_6000.grid(row=3,column=0)
button_9000.grid(row=4,column=0)

#OTHER LAYOUT
other_label.grid(row=0,column=1)
button_NDA.grid(row=1,column=0)
button_posting_report.grid(row=2,column=0)
button_poundage_report.grid(row=3,column=0)

#FORMAT LAYOUT
reformat_label.grid(row=0,column=2)
button_reformat.grid(row=2,column=0)


#STATUS BAR
status = Label(root,text="Hervin Sagnep: PDF SCANNER RENAME APP 2018",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
