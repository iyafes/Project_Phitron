class Book:
    def __init__(self, cat, id, name, quan):
        self.id = id
        self.name = name
        self.category = cat 
        self.quan = quan

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []
        self.returnedBooks = []

class Library:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []

    def addBook(self, cat, id, name, quan):
        book = Book(cat, id, name, quan)
        self.books.append(book)
        print(f"\t{name} Book added !")
    
    def addUser(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
        return user
    
    def borrowBook(self, user, id):
        for book in self.books:
            if book.id == id:
                if user.borrowedBooks:
                    print("\n\tAlready Borrowed")
                    return
                elif book.quan < 1:
                    print("\n\tNo Available Copies !")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quan -= 1
                    print(f"\n\t{book.name} borrowed successfully !")
                    return
        print("\n\tBook not found!")

    def returnBook(self, user, id):
        for book in self.books:
            if book.id == id:
                if user.returnedBooks:
                    print("\n\tAlready Returned !")
                    return
                
                else:
                    user.returnedBooks.append(book)
                    book.quan += 1
                    user.borrowedBooks.remove(book)
                    print(f"\n\t{book.name} returned successfully !")
                    return
        print("\n\tBook not found!")



pl = Library("Abdullah Al Masud", "Phitron Library")
admin = pl.addUser(1, 'Admin', 'admin')
rahim = pl.addUser(50, 'Rahim', '1234')
pybook = pl.addBook('Sci-Fi', 15, 'Dune', 1)


run = True
currentUser = None

while run:

    if currentUser == None:
        print("\n\tNo logged in user !")

        option = input("\nLogin / Registration (L/R): ")

        if option == 'R':
            id = int(input("\tEnter id: "))
            name = input("\tEnter Name: ")
            password = input("\tEnter Password: ")

            user = pl.addUser(id, name, password)
            currentUser = user
            print(f"\nHi {user.name} !\n")

        elif option == 'L':
            id = int(input("\tEnter id: "))
            password = input("\tEnter Password: ")

            match = False
            for user in pl.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    print(f"\nHi {user.name} !\n")
                    match = True
                    break
            if match == False:
                print("\n\tNo user found !")
    
    else:
        if currentUser.name == 'Admin':

            print("Options: \n")

            print("1: Add Book")
            print("2: Show Users")
            print("3: Show Books")
            print("4: Logout")

            choice = int(input("\nEnter Option: "))

            if choice == 1:
                cat = input("\tEnter Category: ")
                id = int(input("\tEnter id: "))
                name = input("\tEnter Name: ")
                q = int(input("\tEnter Quantity: "))

                pl.addBook(cat, id, name, q)
            
            elif choice == 2:
                if not pl.users:
                    print("\tNo User !")
                else:
                    for user in pl.users:
                        print(f"\t{user.name}, id: {user.id} ")
            
            elif choice == 3:
                if not pl.books:
                    print("\nNo Books !")
                else:
                    for book in pl.books:
                        print(f"\tName: {book.name}, id: {book.id}")

            elif choice == 4:
                currentUser = None

        else:
            print("Options: \n")

            print("1: Borrow Book")
            print("2: Return Book")
            print("3: Show Books")
            print("4: Show Borrowed Books")
            print("5: Show Returned Books")
            print("6: Logout")

            choice = int(input("\nEnter Option: "))

            if choice == 1:
                id = int(input("\tEnter id: "))
                pl.borrowBook(currentUser, id)

            elif choice == 2:
                id = int(input("\tEnter id: "))
                pl.returnBook(currentUser, id)
            
            elif choice == 3:
                if not pl.books:
                    print("\nNo Books !")
                else:
                    for book in pl.books:
                        print(f"\tName: {book.name}, id: {book.id}")

            elif choice == 4:
                if not currentUser.borrowedBooks:
                    print("\nNo borrowed books !\n")
                else:
                    for book in currentUser.borrowedBooks:
                        print("\nBorrowed Books:")
                        print(f"Name: {book.name}, id: {book.id}\n")

            elif choice == 5:
                if not currentUser.returnedBooks:
                    print("\nNo returned books !\n")
                else:
                    for book in currentUser.returnedBooks:
                        print("\nReturned Books:")
                        print(f"Name: {book.name}, id: {book.id}\n")


            elif choice == 6:
                currentUser = None









                    


