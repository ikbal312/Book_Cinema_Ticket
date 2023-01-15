class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        Star_Cinema.entry_hall(Star_Cinema, self)  # changed

    def entry_show(self, id, movie_name, time):
        self.__show_list.append(tuple((str(id), str(movie_name), str(time))))
        _list = []
        for row in range(self.__rows):
            l = []
            for col in range(self.__cols):
                l.append(chr(row+65) + str(col))
            _list.append(l)
        self.__seats[str(id)] = _list     #changed

    def book_seats(self, customer_name, phone_no, id, seat):
        invaldSeat = []
        alreadyBooked = []
        booked = []

        is_Id_Valid = False
        for show_id, a_name, b_time in self.__show_list:
            if show_id == id:
                is_Id_Valid = True
                movie_detail = (a_name, b_time)
                break
        if is_Id_Valid:
            for r, c in seat:
                if -1 < r < self.__rows and -1 < c < self.__cols:
                    if self.__seats[id][r][c] == "X":
                        alreadyBooked.append(chr(r+65)+str(c))
                    else:
                        self.__seats[id][r][c] = "X"
                        booked.append(chr(r+65)+str(c))
                else:
                    invaldSeat.append(chr(r+65)+str(c))
        else:
            print("Id didn't match with any show!")
            return

        if len(booked) != 0:
            print("\n", 5*"#", "TICKET  BOOKED SUCCESSFULLY!!", 5*"#")
            print(90*"-")
            print(
                f"NAME: {customer_name}\nPHONE NUMBER: {phone_no}\n\nMOVIE NAME: {movie_detail[0]:25} MOVIE TIME:{movie_detail[1]}\nTICKETS: ", end="")
            for seat in booked:
                print(f" {seat}", end="")
            print(f"\nHALL: {self.__hall_no}\n")
            print(90*"-", "\n")

        if len(invaldSeat) != 0:
            print("\n", 90*"-")
            print(f"INVALID SEAT NO -", end="")
            for seat in invaldSeat:
                print(f" {seat}", end="")
            print(" TRY AGAIN!")
            print(90*"-", "\n")

        if len(alreadyBooked) != 0:
            print("\n", 90*"-")
            print("THESE SEATS ALREADY WERE BOOKED - ", end="")
            for seat in alreadyBooked:
                print(f" {seat}", end="")
            print("\n", 90*"-", "\n")

    def view_show_list(self):
        print(90*"-")
        for id, movie_name, time in self.__show_list:
            print(
                f"MOVIE NAME:{movie_name:15}SHOW ID: {id:12}TIME: {time}")
        print(90*"-")

    def view_available_seats(self, id):
        is_Id_Valid = False
        for show_id, customer_name, time in self.__show_list:
            if show_id == id:
                is_Id_Valid = True
                movieInfo = (customer_name, time)
                break

        if is_Id_Valid:
            print(
                f"MOVIE NAME: {movieInfo[0]:10} TIME:{movieInfo[1]}")
            print("X for already booked seats")
            print(90*"-")
            for row in self.__seats[id]:
                for seat in row:
                    print(f"{seat:5}", end="")
                print()
            print(90*"-")
        else:
            print("Id didn't match with any show!")


def display():
    hall = Hall(3, 4, "B20")
    hall.entry_show(1, "Hakim", "18 Nov 2022 5:00PM")
    hall.entry_show(2, "shipan", "18 Nov 2022 6:00PM")
    hall.entry_show(3, "Rahim", "18 Nov 2022 7:00PM")
    while (True):
        print("\n\n1. View all show today\n2. Available seats\n3. Book tickets\n \n")
        opt = input("Enter the option: ")
        if opt == '1':
            hall.view_show_list()
            print("\n")
        elif opt == '2':
            show_id = input("Enter id:")
            print("\n")
            hall.view_available_seats(show_id)
        elif opt == '3':
            name = input("Enter customer name: ")
            ph_num = input("Enter customer phone_no: ")
            show_id = input("Enter id: ")
            num_ticket = int(input("Enter number of ticket: "))
            seat_l = []
            for _ in range(num_ticket):
                seat_num = input("Enter seat no:")
                if seat_num[0].isalpha() and seat_num[1:].isdigit():
                    r = ord(seat_num[0])-65
                    c = int(seat_num[1:])
                    seat_l.append((r, c))
                else:
                    print(60*"-")
                    print("Id didn't match with any show!")
                    print(60*"-")
            if len(seat_l) != 0:
                hall.book_seats(name, ph_num, show_id, seat_l)
        else:
            print("This option didn't correct!")


display()
