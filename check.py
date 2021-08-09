import re

#This is a regular expression


'''
    This function check for input string and validate them.
    The function comes with some function parameter that will assist you to validate your inputs.

'''
def check_input(strs,name_='',mak='',char=3):
    valid = True

    while  valid:
        try:
            strs = input(f"Enter {name_} :")
            if len(strs.strip()):
                mak.append(strs)
                break
            else:
                print(f"{name_} cannot be empty ")
        except:
           break

#this check for email validation
def check_email(email,mak=''):
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z_.-]+\.[a-z]+')
    valid = True
    while valid:
        try:
            if(re.search(pattern,email)):
               valid =False
            else:
                print("Invalid Email")
                email = input(f"Enter valid email :")
        except:
            pass
    mak.append(email)


#this check for phonenumber validation
def check_phone_number(phonenumber,mak=''):

    pattern = re.compile(r'[0-9]{10}')
    valid = True
    while valid:
       try:
           if(re.search(pattern,phonenumber)):
               valid = False
           else:
                print("Invalid phone number ")
                phonenumber = input(f"Enter valid number (0000000000) :")
       except ValueError:
           pass
    mak.append(phonenumber)