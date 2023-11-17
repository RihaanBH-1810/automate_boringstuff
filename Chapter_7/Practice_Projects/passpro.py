import re

def check_password(passd):
    obj = re.compile(r'.*')
    if len(passd) < 9:
        return False
    elif(obj.search(r'[0-9]') == None or obj.search(r'[a-z]') == None or obj.search(r'[A-Z]') == None 
        or obj.search(r'[a-z]') == None):
        return False
    else:
        return True

passd1 = "12aAsssS21"
passd2 = "swsws1"
if(check_password(passd1)):
    print("Strong Password")
else:
    print("Weak password")

    
if(check_password(passd2)):
    print("Strong Password")
else:
    print("Weak password")
        
