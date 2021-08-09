import check
import card
class Contact:
    total_address = 0
    address_db = {}

    def __init__(self,firstname='',lastname='',email='',phonenumber=''):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.phonenumber=phonenumber

    #Add a new contact to the book
    def add_new_contact(self):

        new_contact = []


        check.check_input("firstname","Firstname",new_contact)
        check.check_input("lastname","Lastname",new_contact)
        email = input("Enter email : ")
        check.check_email(email,new_contact)
        phonenumber = input(f"Enter  phonenumber (0000000000) :")
        check.check_phone_number(phonenumber,new_contact)

        try:
            if self.address_db is not {}:
                if self.address_db[new_contact[0]+new_contact[1]] ==self.address_db.keys():
                    print("Address already exist ")
        #putting the list into a dictonary
        except KeyError:
            self.address_db[new_contact[0]+new_contact[1]] = new_contact
            print("A new contact has being added")

    #this shows contact in db
    def show_all_contact(self):
        for v in self.address_db.items():
            new_list = []
            new_list.append(v[1])
            for i in new_list:
                card.console_card_printer(i[0],i[1],i[2],i[3])


    def delete_contact(self):
        contacts = input("Enter Contact to Delete : ")
        try:
            del self.address_db[contacts]
            print(f'{contacts} has been successfuly deleted.')
        except KeyError:
            print("No contact found ")

    #this allows a contact to be edited
    def edit_contact(self):
        contacts = input("Enter Contact to Edit : ")
        if contacts in self.address_db:
            try:

                firstname = input("Edit Firstname : ")
                lastname = input("Edit Lastname : ")
                email = input("Edit email address : ")
                phonenumber = input("Edit Phone number : ")

                self.firstname,self.lastname,self.email,self.phonenumber=firstname,lastname,email,phonenumber
                #puting this items into a list
                new_contact = [firstname,lastname,email,phonenumber]

                #updating the dictionary
                new_key = firstname+lastname
                self.address_db[new_key] = new_contact
                self.address_db.pop(contacts)
            except:
                pass
        else:
            print(f"{contacts} cannot be found in the database")

        #this allows you to search through the database
    def search_contact(self):
        contacts = input("Enter Contact to Search : ")
        if contacts in self.address_db:
            print(self.address_db[contacts])
        else:
            print("No search match ")

    @staticmethod
    def error_msg(err):
        def __str__():
            return err
