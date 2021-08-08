import re

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
def check_email(email):
    pass

#this check for phonenumber validation
def check_phone_number(phonenumber):
    pass