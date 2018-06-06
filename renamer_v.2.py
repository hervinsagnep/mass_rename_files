#SCANNER RENAMER
import os
def bat_or_oth(kind):
    if kind == "BATCH":
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
        batch_number(int(input("BATCH TYPE")))
    elif kind == "OTHER":
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
                    poundage_input = (input("Batch Number"))
                    poundage_format = ('{}'.format(poundage_input))
                    os.rename(files, poundage_format)
            elif type == "POSTING REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    month = ("MM")
                    day = ("DD")
                    year = (2018)
                    posting_message = "POSTING REPORT"
                    posting_format = ('{}-{}-{} {}'.format(month, day, year, posting_message))
                    os.rename(files, posting_format)
            else:
                print("INVALID TYPE")
        other_type(input("OTHER TYPE: NDA, POUNDAGE REPORT, POSTING REPORT"))
bat_or_oth(input("BATCH OR OTHER?"))


"""
os.chdir('/Users/hervinsagnep/Desktop/1') <---- Place holder for scanned file location at work

TO CHANGE FORMAT:

CHANGE PRINT STATEMENTS AT EACH FUNCTION TO - os.rename(files,variable name)

"""