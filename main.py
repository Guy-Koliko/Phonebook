from mainclass import Contact as ct
from os import system, name

b = ct()

def main():

    bannermotd()
    menu()


def addcontact():

    b.add_new_contact()

def menu():

    while True:
        sh = input(" Your choice : ")
        if sh == 'A'.lower():

            addcontact()
            main()
            # clear()

        elif sh =='S'.lower():
            bannermotd()
            showcontact()
        elif sh =='D'.lower():
            deletecontact()
        elif sh =="E".lower():
            editcontact()
        elif sh =="C".lower():
            searchcontact()

        else:
            print("You have make a wrong choice,  [(Add) OR (Show) contact].")
            menu()

def bannermotd():
    motd = " WELCOME TO EDEM'S PHONEBOOK SERVICE"
    menu_msg = "WHAT DO YOU WANT TO DO"
    lines = "_"*len(menu_msg)
    star = "*"*len(motd)
    banner = f'''
                {star}
                {motd}
                {star}
                {star}
                    {menu_msg}
                    {lines}
                    ADD NEW CONTACT [A]
                    SHOW ALL CONTACT [S]
                    DELETE A CONTACT [D]
                    SEARCH FOR A CONTACT [C]
                    EDIT CONTACT [E]
                {star}


             '''
    print(banner)

def showcontact():
    b.show_all_contact()

#delete contacta

def deletecontact():
    showcontact()
    b.delete_contact()

def editcontact():
    showcontact()
    b.edit_contact()

def searchcontact():
    b.search_contact()


main()