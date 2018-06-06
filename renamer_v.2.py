import os
def bat_or_oth(kind):

    if kind == "BATCH":
        # BATCHES FUNCTIONS
        def batch_number(number):
            if number == 1000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    one_thousand_template = "2018MMDD-10XX"
                    pdf = ".pdf"
                    one_thousand_format = ('{} {}{}'.format(prefix_num,one_thousand_template,pdf))
                    os.rename(files,one_thousand_format)
            elif number == 2000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    two_thousand_template = "2018MMDD-20XX"
                    pdf = ".pdf"
                    two_thousand_format = ('{} {}{}'.format(prefix_num,two_thousand_template,pdf))
                    os.rename(files, two_thousand_format)
            elif number == 6000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    six_thousand_template = "2018MMDD-60XX"
                    pdf = ".pdf"
                    six_thousand_format = ('{} {}{}'.format(prefix_num,six_thousand_template,pdf))
                    os.rename(files,six_thousand_format)
            elif number == 9000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    nine_thousand_template = "2018MMDD-90XX"
                    pdf = ".pdf"
                    nine_thousand_format = ('{} {}{}'.format(prefix_num,nine_thousand_template,pdf))
                    os.rename(files, nine_thousand_format)
            else:
                print("INVALID BATCH TYPE")
        batch_number(int(input("BATCH TYPE: 1000,2000,6000,9000")))

    elif kind == "OTHER":
        # "OTHER FUNCTIONS"
        def other_type(type):
            if type == "NDA":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    nda_template = "NDA MM-DD-2018"
                    pdf = ".pdf"
                    nda_format = ('{} {}{}'.format(prefix_num,nda_template,pdf))
                    os.rename(files, nda_format)
            elif type == "POUNDAGE REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    poundage_input = (input("BATCH NUMBER"))
                    pdf = ".pdf"
                    poundage_format = ('{} {}{}'.format(prefix_num,poundage_input,pdf))
                    os.rename(files, poundage_format)
            elif type == "POSTING REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    prefix_num = (files[:2])
                    month = ("MM")
                    day = ("DD")
                    year = (2018)
                    posting_message = "POSTING REPORT.pdf"
                    posting_format = ('{} {}-{}-{} {}'.format(prefix_num,month, day, year, posting_message))
                    os.rename(files, posting_format)
            else:
                print("INVALID TYPE")
        other_type(input("OTHER TYPE: NDA, POUNDAGE REPORT, POSTING REPORT"))
    else:
        print ("PLEASE INPUT VALID KIND")
bat_or_oth(input("BATCH OR OTHER?"))


"""
os.chdir('/Users/hervinsagnep/Desktop/1') <---- Place holder for scanned file location at work

TO CHANGE FORMAT:

CHANGE PRINT STATEMENTS AT EACH FUNCTION TO - os.rename(files,variable name)

CONCERN:

COMPUTER WILL NOT ALLOW FILES TO ALL BE RENAMED TO THE TEMPLATE

FIXES:

ASSIGN FILES TO BE RENAMED AS NUMBER AND WILL BE MERGED WITH THE FORMATING

EX.
FUNCTION TO RENAME ALL FILES WITH DIGITS STARTING FROM 00. COMBINE THE DIGITS WITH THE FORMAT
00 NDA MMDDYYYY
01 NDA MMDDYYYY

THE PREFIX DIGITS MUST BE REMOVED MANUALLY

LIST OF NUMBERS:

[0:101] 

PREFIX SCRIPT:

import os
os.chdir('/Users/hervinsagnep/Desktop/1')
for files in os.listdir():
    prefix_num = (files[:2]) <--------- Variable in "for" loops, 
    WHEN FILES ARE SCANNED THEY ARE GIVEN RANDOM NAMES MAY
    HAVE TO SPLICE MORE DIGITS TO ENSURE TOTALLY RANDOM PREFIX AND MAINTATIN ORDER OF FILES
       
PREFIX REMOVAL SCRIPT:
#REMOVE PREFIX
    
import os
os.chdir('/Users/hervinsagnep/Desktop/1')
for files in os.listdir():
    prefix_rem = (files[3:])
    os.rename(files,prefix_rem)
    
#MONTH INPUT * ISSUE

month = input("Month")

INPUT NEEDS TO BE PUT FOR ALL FUNCTIONS THAT HAVE MONTHS IN TEMPLATE

1. USER INPUT FOR MONTH WILL ASK FOR INPUT OF EACH INDIVIDUAL FILE, NEED INPUT TO FORMAT WITH THE SINGLE INPUT INTEGER

#FILE EXTENSTION * ISSUE:

1. DID NOT ACCOUNT FOR FILE TYPE EXTENSION TO BE INCLUDED IN FORMATTING
- ADD .PDF TO END OF EACH var_MESSAGE FORMAT?
- TAKE PDF EXTENSTION FROM ORIGINAL FILE NAME,STORE IN VARIABLE, THEN USE VARIABLE AS PARMETER FOR FORMATTING

*FIXED WITH pdf = ".pdf" in each "for" loop


"""
