import re 
import copy

def validate_date_format(date):
    validator = re.compile(r'''((3[01]|[12][0-9]|0?[1-9])[/\-]([1][0-2]|0?[1-9])[/\-]([12]\d{3}))''')
    global mo
    mo = validator.findall(date)
    if mo == None:
        return False
    else:
        return True
    
def Check_dates(match_list):
    final_matchlist = copy.deepcopy(match_list)
    for tup in match_list:

        date, day, month, year = tup
        if int(month) == 2:
            if year%4 == 0 or (year%100 == 0 and year%400) :
                if int(day) <= 29:
                    continue
                else:
                    final_matchlist.remove(tup)
                    continue
            else:
                if int(day) <= 28:
                    continue
                else:
                    final_matchlist.remove(tup)
                    continue
        if int(day) in [1,3,5,7,8,10,12]:
            if int(day) <= 31:
                continue
            else:
                final_matchlist.remove(tup)
                continue
        else:
            if int(day) == 31:
                final_matchlist.remove(tup)
                continue
            else:
                continue
    return final_matchlist

dates = "10-12-2993 , 09-30-2222, 0-2, 9-10-2003 "

if validate_date_format(dates):
    list = Check_dates(mo)
    print("The valid dates are : ")
    for t in list:
        print(t[0])









    