from tkinter import *
import os

root = Tk()
"""
batches_label = Label(root, text="BATCHES")
batches_others = Label(root, text="OTHERS")
batches_reformat = Label(root, text="REFORMAT")

batches_label.grid(row=0,sticky=N)
batches_others.grid(row=1,sticky=N)
batches_reformat.grid(row=2,sticky=N)
"""
root.mainloop()

#ROWS LABEL SCRIPT

"""
batches_label = Label(root, text="BATCHES")
batches_others = Label(root, text="OTHERS")
batches_reformat = Label(root, text="REFORMAT")

batches_label.grid(row=0,sticky=N)
batches_others.grid(row=1,sticky=N)
batches_reformat.grid(row=2,sticky=N)
"""


#BATCHES BUTTONS WITH FUNCTIONS
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


button_1000 = Button(root,text="1000",command=batch_1000)
button_2000 = Button(root,text="2000",command=batch_2000)
button_6000 = Button(root,text="6000",command=batch_6000)
button_9000 = Button(root,text="9000",command=batch_9000)


#OTHERS BUTTONS WITH FUNCTIONS
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


button_NDA = Button(root,text="NDA",command=nda)
button_posting_report = Button(root,text="POSTING REPORT",command=posting_report)
button_poundage_report = Button(root,text="POUNDAGE REPORT",command=poundage_report)

#REFORMAT BUTTON WITH FUNCTION
def reformat():
    os.chdir('/Users/hervinsagnep/Desktop/1')
    for files in os.listdir():
        prefix_rem = (files[3:])
        os.rename(files, prefix_rem)


button_REFORMAT = Button(root,text="1000",command=reformat)

#BINDS 