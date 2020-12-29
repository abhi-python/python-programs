class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lend_dict = {}

    def displaybooks(self):
        print(f"We have the following books in Library : {self.name}")    
        for book in self.booklist:
            print(book)
    
    def lendbook(self, user, book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.") 
        else:
            print(f"Book is already being used by {self.lend_dict[book]}")    

    def addbook(self, book):
        self.booklist.append(book)
        print("The book has been added to the book List")

    def returnbook(self, book):
        self.lend_dict.pop(book)  
        print("The book has been return in the library.")  

if __name__ == "__main__":
    abhi = Library(["Python", "C++", "Ruby", ".net"], "Abhilash Library")

    while(True):
        print(f"Welcome to the {abhi.name}. Enter your choice to continue :")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Remove a Book")
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("Enter the valid Choice.")
            continue
        else:
            user_choice = int(user_choice)    

        if user_choice == 1:
            abhi.displaybooks()
        
        elif user_choice == 2:
            book = input("Enter the name of book you want to lend :")
            user = input("Enter your name : ")
            abhi.lendbook(user, book)


        elif user_choice == 3:
            book = input("Enter the book you want to add : ")
            abhi.addbook(book)

        elif user_choice == 4:
            book = input("Enter the book you want to return : ")
            abhi.returnbook(book)
        
        else:
            print("Please enter the valid Choice.")  

        print("Press q to quit and c to continue")   
        user_choice1 = ""
        while(user_choice1!="q" and user_choice1!="c"):
            user_choice1 = input()
            if user_choice1 == "q":
                exit()
            elif user_choice1 == "c":
                continue                      