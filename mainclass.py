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

        firstname = input("Enter Firstname : ")
        lastname = input("Enter Lastname : ")
        email = input("Enter email address : ")
        phonenumber = input("Enter Phone number : ")


        # self.firstname,self.lastname,self.email,self.phonenumber=firstname,lastname,email,phonenumber

        #puting this items into a list
        new_contact = [firstname,lastname,email,phonenumber]
        #putting the list into a dictonary
        self.address_db[firstname+lastname] = new_contact
        print("A new contact has being added")

    #this shows contact in db
    def show_all_contact(self):
        for v in self.address_db.items():
            for i in v:
                print(i)

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
