#SCANNER RENAMER
import os
def bat_or_oth(kind):

    if kind == "BATCH":
        # BATCHES FUNCTIONS
        def batch_number(number):
            if number == 1000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    one_thousand_template = "20YYMMDD-10XX"
                    one_thousand_format = ('{}'.format(one_thousand_template))
                    os.rename(files,one_thousand_format)
            elif number == 2000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    two_thousand_template = "20YYMMDD-20XX"
                    two_thousand_format = ('{}'.format(two_thousand_template))
                    os.rename(files, two_thousand_format)
            elif number == 6000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    six_thousand_template = "20YYMMDD-60XX"
                    six_thousand_format = ('{}'.format(six_thousand_template))
                    os.rename(files,six_thousand_format)
            elif number == 9000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    nine_thousand_template = "20YYMMDD-90XX"
                    nine_thousand_format = ('{}'.format(nine_thousand_template))
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
                    nda_template = "20YYMMDD-10XX"
                    nda_format = ('{}'.format(nda_template))
                    os.rename(files, nda_format)
            elif type == "POUNDAGE REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    poundage_input = (input("BATCH NUMBER"))
                    poundage_format = ('{}'.format(poundage_input))
                    os.rename(files, poundage_format)
            elif type == "POSTING REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    month = ("MM")
                    day = ("DD")
                    year = (2018)
                    posting_message = "POSTING REPORT"
                    prefix_num = (files[:2])
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
    prefix_num = (files[:2]) <--------- Variable in "for" loops
    
    
PREFIX REMOVAL SCRIPT:
#REMOVE PREFIX
    
import os
os.chdir('/Users/hervinsagnep/Desktop/1')
for files in os.listdir():
    prefix_rem = (files[3:])
    os.rename(files,prefix_rem)
    
#MONTH INPUT

month = input("Month")

#NOTES:

1. USER INPUT FOR MONTH WILL ASK FOR INPUT OF EACH INDIVIDUAL FILE, NEED INPUT TO FORMAT WITH THE SINGLE INPUT INTEGER
2. DID NOT ACCOUNT FOR FILE TYPE EXTENSION TO BE INCLUDED IN FORMATTING
- ADD .PDF TO END OF EACH var_MESSAGE FORMAT


"""
