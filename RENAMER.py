#SECOND HARVEST SCANNER RENAME
import os
def bat_or_oth(kind):
    if kind == "Batch":
        def batch_number(number):
            if number == 1000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    one_thousand_template = "20YYMMDD-10XX"
                    print('{}'.format(one_thousand_template))
            elif number == 2000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    two_thousand_template = "20YYMMDD-20XX"
                    print('{}'.format(two_thousand_template))
            elif number == 6000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    six_thousand_template = "20YYMMDD-60XX"
                    print('{}'.format(six_thousand_template))
            elif number == 9000:
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    nine_thousand_template = "20YYMMDD-90XX"
                    print('{}'.format(nine_thousand_template))
            else:
                print("Invalid Batch Type")
        batch_number(int(input("Batch Type")))
    elif kind == "Other":
        def other_type(type):
            if type == "NDA":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    one_thousand_template = "20YYMMDD-10XX"
                    print('{}'.format(one_thousand_template))
            elif type == "POUNDAGE REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    poundage_input = (input("Batch Number"))
                    print('{}'.format(poundage_input))
            elif type == "POSTING REPORT":
                os.chdir('/Users/hervinsagnep/Desktop/1')
                for files in os.listdir():
                    month = ("MM")
                    day = ("DD")
                    year = (2018)
                    posting_message = "POSTING REPORT"
                    print('{}-{}-{} {}'.format(month, day, year, posting_message))
            else:
                print("Invalid Type")
        other_type(input("Other Type: NDA, POUNDAGE REPORT, POSTING REPORT"))
bat_or_oth(input("Batch or Other?"))