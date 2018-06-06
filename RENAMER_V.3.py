#PDF SCANNER RENAMER
#=====================INPUT MUST BE ALL CAPS==========================
import os
def bat_or_oth(kind):

    if kind == "BATCH":
        # BATCHES FUNCTIONS
        def batch_number(number):
            if number == 1000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                year = (int(input("YEAR")))
                month = ((input("MONTH")))
                for files in os.listdir():
                    prefix_num = (files[:2])
                    one_thousand_template = "DD-10XX"
                    pdf = ".pdf"
                    one_thousand_format = ('{} {}{}{}{}'.format(prefix_num,year,month,one_thousand_template,pdf))
                    os.rename(files,one_thousand_format)
            elif number == 2000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                year = (int(input("YEAR")))
                month = ((input("MONTH")))
                for files in os.listdir():
                    prefix_num = (files[:2])
                    two_thousand_template = "DD-20XX"
                    pdf = ".pdf"
                    two_thousand_format = ('{} {}{}{}{}'.format(prefix_num,year,month,two_thousand_template,pdf))
                    os.rename(files, two_thousand_format)
            elif number == 6000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                year = (int(input("YEAR")))
                month = ((input("MONTH")))
                for files in os.listdir():
                    prefix_num = (files[:2])
                    six_thousand_template = "MMDD-60XX"
                    pdf = ".pdf"
                    six_thousand_format = ('{} {}{}{}{}'.format(prefix_num,year,month,six_thousand_template,pdf))
                    os.rename(files,six_thousand_format)
            elif number == 9000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                year = (int(input("YEAR")))
                month = ((input("MONTH")))
                for files in os.listdir():
                    prefix_num = (files[:2])
                    nine_thousand_template = "MMDD-90XX"
                    pdf = ".pdf"
                    nine_thousand_format = ('{} {}{}{}{}'.format(prefix_num,year,month,nine_thousand_template,pdf))
                    os.rename(files, nine_thousand_format)
            else:
                print("INVALID BATCH TYPE")
        batch_number(int(input("BATCH TYPE: 1000,2000,6000,9000")))

    elif kind == "OTHER":
        # "OTHER FUNCTIONS"
        def other_type(type):
            if type == "NDA":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                year = (int(input("YEAR")))
                month = ((input("MONTH")))
                for files in os.listdir():
                    prefix_num = (files[:2])
                    nda = "NDA"
                    nda_template = "DD"
                    pdf = ".pdf"
                    nda_format = ('{} {} {}-{}-{}'.format(prefix_num,nda,month,nda_template,year,pdf))
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
                month = ((input("MONTH")))
                year = ((int(input("YEAR"))))
                for files in os.listdir():
                    prefix_num = (files[:2])
                    day = ("DD")
                    posting_message = "POSTING REPORT.pdf"
                    posting_format = ('{} {}-{}-{} {}'.format(prefix_num,month, day, year, posting_message))
                    os.rename(files, posting_format)
            else:
                print("INVALID TYPE")
        other_type(input("OTHER TYPE: NDA, POUNDAGE REPORT, POSTING REPORT"))

    elif kind == "REFORMAT":
        os.chdir('/Users/hervinsagnep/Desktop/1')
        for files in os.listdir():
            prefix_rem = (files[3:])
            os.rename(files, prefix_rem)
    else:
        print ("PLEASE INPUT VALID KIND")
bat_or_oth(input("BATCH,OTHER,REFORMAT?"))


"""
year = (int(input("YEAR")))
month = (int(input("MONTH")))

ADD PADDING TO MONTH (2,0) FORMATTING?

"""
