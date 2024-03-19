import useful_functions
NAME_FESTIVAL = "MUSIC FARM FESTIVAL"
def get_tickets_lists(filename):
    types_of_tickets = []
    ticket_prices = []
    max_available_tickets = []
    tickets_sold = []
    ticket_file = open(filename)
    for line in ticket_file:
        line = line.rstrip()
        info_line = line.split(",")
        types_of_tickets.append(info_line[0])
        ticket_prices.append(float(info_line[1]))
        max_available_tickets.append(int(info_line[2]))
        tickets_sold.append(int(info_line[3]))
    ticket_file.close()
    return  types_of_tickets, ticket_prices, max_available_tickets, tickets_sold

# 1. Booking a Ticket
def booking_a_ticket():
    keep_track_fine_dinning = ""
    # tickets_file = open(filename)
    name = useful_functions.get_string("Enter your name => ")
    phone_number = useful_functions.get_positive_int("Enter your phone number => ")
    while True:
        ticket_type_choice = input(f"Choose the ticket type:\n" \
                            "1. Day 1\n" \
                            "2. Day 2\n" \
                            "3. Weekend-Camp ")
        if ticket_type_choice == "1":
            ticket_type = "Day 1"
            break
        elif ticket_type_choice == "2":
            ticket_type = "Day 2"
            break
        elif ticket_type_choice == "3":
            ticket_type = "Weekend-Camp"
            answer_fine_dining = "Yes"
            break
    people_in_group = useful_functions.get_number_max4("How many people in your group? ")
    if ticket_type == "Day 1"  or ticket_type == "Day 2":
        while True:
            fine_dining = useful_functions.get_string("Do you require a fine dining pass (Y/N)? ").upper()
            if fine_dining == "Y":
                answer_fine_dining = "Yes"
                keep_track_fine_dinning = f"FineDining{ticket_type},{people_in_group}\n"
                break
            elif fine_dining == "N":
                answer_fine_dining = "No"
                break

    print(f"\nBooking Details\n" \
           "---------------")
    print(f"\n{'Name:':<20}{name}\n" \
          f"{'No of People:':<20}{people_in_group}\n" \
          f"{'Ticket Type:':<20}{ticket_type}\n" \
          f"{'Fine Dining:':<20}{answer_fine_dining}\n" \
          f"{'Total Cost:'}\n")
    track_fine_dining = open("Extras.txt", "a")
    track_fine_dining.write(keep_track_fine_dinning)
    track_fine_dining.close()
    return name, phone_number, ticket_type, people_in_group, fine_dining, track_fine_dining

def main():
    tickets_menu_file = "Sales_2022.txt"
    type_of_ticket, ticket_price,  max_available_tickets, tickets_sold  = get_tickets_lists(tickets_menu_file)
    while True:
        print(f"{NAME_FESTIVAL}\n{len(NAME_FESTIVAL) * '='}")
        menu = (f"1. Make a Booking\n" \
                "2. Review Bookings\n" \
                "3. Exit")
        print(menu)
        choice = input("Enter your choice: ")
        if choice == '1':
            booking_a_ticket()
        elif choice == '2':
            pass
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()