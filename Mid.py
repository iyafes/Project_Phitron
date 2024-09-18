class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)
        
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []
        
    def entry_show(self, id, movie_name, time):
        show_details = (id, movie_name, time)
        self._show_list.append(show_details)
        seat = [['Free' for x in range(self._cols)] for y in range(self._rows)]
        self._seats[id] = seat

    def book_seats(self, id, list_of_seats):
        if id not in self._seats:
            print("\n\tSHOW ID IS INVALID!")

        for row, col in list_of_seats:
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"\n\tSEAT ({row}, {col}) IS INVALID!")
            if self._seats[id][row][col] != 'Free':
                print(f"\n\tSEAT ({row}, {col}) IS ALREADY BOOKED!")

            else:
                print(f"\n\tSEAT ({row}, {col}) IS BOOKED FOR SHOW {show_id}\n")
                self._seats[id][row][col] = 'Booked'

    def view_show_list(self):
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("\n\tSHOW ID IS INVALID!")
        
        seats = self._seats[id]
        for row in range(self._rows):
            for col in range(self._cols):
                if seats[row][col] == 'Free':
                    print(f"Row: {row}, Col: {col}")

cinema_1 = Star_Cinema()
cinema_1.entry_hall(Hall(7, 7, 1))
cinema_1.hall_list[0].entry_show("1", "MOVIE 123", "2:00 PM")
cinema_1.hall_list[0].entry_show("2", "MOVIE ABC", "5:00 PM")

while True:
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

    choice = int(input("\nENTER OPTION: "))
    if choice == 1:
        print("---------------------")
        cinema_1.hall_list[0].view_show_list()
        print("---------------------")
    
    elif choice == 2:
        show_id = input("\nENTER SHOW ID: ")
        cinema_1.hall_list[0].view_available_seats(show_id)

    elif choice == 3:
        show_id = input("\nENTER SHOW ID: ")
        num_of_seats = int(input("\nENTER NUMBER OF SEATS: "))
        seat_list = []
        try:
            for i in range(num_of_seats):
                row = int(input(f"\nENTER ROW FOR SEAT {i + 1}: "))
                col = int(input(f"\nENTER COLUMN FOR SEAT {i + 1}: "))
                seat_list.append((row, col))

                cinema_1.hall_list[0].book_seats(show_id, seat_list)
                
        except:
            print("\n\tNOT AVAILABLE\n")
    
    elif choice == 4:
        break

    else:
        print("\n\tINVALID CHOICE\n")
