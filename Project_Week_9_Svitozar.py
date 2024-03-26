import useful_functions
NAME_FESTIVAL = "MUSIC FARM FESTIVAL"
def get_tickets_lists(filename, extras_file):
    types_of_tickets = []
    ticket_prices = []
    max_available_tickets = []
    tickets_sold = []
    ticket_file = open(filename)
    for line in ticket_file:
        if line:
            line = line.rstrip()
            info_line = line.split(",")
            types_of_tickets.append(info_line[0])
            ticket_prices.append(float(info_line[1]))
            max_available_tickets.append(int(info_line[2]))
            tickets_sold.append(int(info_line[3]))
    ticket_file.close()
    extras_ticket_type = []
    extras_quantity = []
    fine_dining_file = open(extras_file)
    for line in fine_dining_file:
        line = line.rstrip()
        if line:
            info_line1 = line.split(",")
            extras_ticket_type.append(info_line1[0])
            extras_quantity.append(int(info_line1[1]))
    fine_dining_file.close()
    print(extras_ticket_type, extras_quantity)
    return  types_of_tickets, ticket_prices, max_available_tickets, tickets_sold, extras_ticket_type, extras_quantity

# 1. Booking a Ticket
def booking_a_ticket(types_of_tickets, ticket_prices, extras_ticket_type, extras_quantity, keep_track_fine_dinning):
    # Greeting
    option = "BOOKING"
    full_name = f"{NAME_FESTIVAL} ({option})"
    print(f"{full_name}\n{len(full_name) * '='}")
    for i, name in enumerate(types_of_tickets):
        print(f"{i+1}. {name:<15}€{ticket_prices[i]:.2f}")
    # code
    price = 0
    name = useful_functions.get_string("Enter your name => ")
    phone_number = useful_functions.get_positive_int("Enter your phone number => ")
    while True:
        # ticket_type_choice = input(f"Choose the ticket type:\n" \
        #                     "1. Day 1\n" \
        #                     "2. Day 2\n" \
        #                     "3. Weekend-Camp ")
        ticket_type_choice = input("Choose the ticket type: ")
        if ticket_type_choice == "1":
            ticket_type = "Day1"
            people_in_group = useful_functions.get_number_max4("How many people in your group? ")
            if people_in_group > 1 and people_in_group <= 4:
                while True:
                    fine_dining = useful_functions.get_string("Do you require a fine dining pass (Y/N)? ").capitalize()
                    if fine_dining == "Y" or fine_dining == "yes":
                        answer_fine_dining = "Yes"
                        extras_quantity[0] += people_in_group
                        price = (people_in_group * ticket_prices[0]) + (20 * people_in_group)
                        break
                    elif fine_dining == "N" or fine_dining == "no":
                        price = ticket_prices[0] * people_in_group
                        answer_fine_dining = "No"
                        break
                    else:
                        print('Please answer "yes" or "no" ')
                break
            else:
                answer_fine_dining = "No"
                price = ticket_prices[0]
                break
        elif ticket_type_choice == "2":
            ticket_type = "Day2"
            people_in_group = useful_functions.get_number_max4("How many people in your group? ")
            if people_in_group > 1 and people_in_group <= 4:
                while True:
                    fine_dining = useful_functions.get_string("Do you require a fine dining pass (Y/N)? ").capitalize()
                    if fine_dining == "Y" or fine_dining == "yes":
                        answer_fine_dining = "Yes"
                        extras_quantity[1] += people_in_group
                        price = (people_in_group * ticket_prices[1]) + (20 * people_in_group)
                        break
                    elif fine_dining == "N" or fine_dining == "no":
                        answer_fine_dining = "No"
                        price = ticket_prices[1] * people_in_group
                        break
                    else:
                        print('Please answer "yes" or "no" ')
                break
            else:
                answer_fine_dining = "No"
                price = ticket_prices[1]
                break
        elif ticket_type_choice == "3":
            ticket_type = "Weekend-Camp"
            people_in_group = useful_functions.get_number_max4("How many people in your group? ")
            answer_fine_dining = "Included"
            price = ticket_prices[2] * people_in_group
            break
    # print(f"\nBooking Details\n" \
    #        "---------------")
    # print(f"{'Name:':<20}{name}\n" \
    #       f"{'No of People:':<20}{people_in_group}\n" \
    #       f"{'Ticket Type:':<20}{ticket_type}\n" \
    #       f"{'Fine Dining:':<20}{answer_fine_dining}\n" \
    #       f"{'Total Cost:':<20}€{price:.2f}\n")
    feedback_to_user = (f"\nBooking Details\n" \
           "---------------\n" \
           f"{'Name:':<20}{name}\n" \
           f"{'No of People:':<20}{people_in_group}\n" \
           f"{'Ticket Type:':<20}{ticket_type}\n" \
           f"{'Fine Dining:':<20}{answer_fine_dining}\n" \
           f"{'Total Cost:':<20}€{price:.2f}\n")
    ticket_name_sale = open(f"{name}_sale.txt", "w")
    ticket_name_sale.write(f"{ticket_type},{phone_number},{people_in_group},{price},{answer_fine_dining}")
    ticket_name_sale.close()
    # extras_track_file = open(keep_track_fine_dinning)
    # for k, name in enumerate(extras_ticket_type):
    #     extras_track_file.write(f"FineDining{name},{extras_quantity[k]}")
    # extras_track_file.close()
    # return name, phone_number, ticket_type, people_in_group, answer_fine_dining, price
    return feedback_to_user
def main():
    tickets_menu_file = "Sales_2022.txt"
    keep_track_fine_dinning = "Extras.txt"
    type_of_ticket, ticket_price,  max_available_tickets, tickets_sold, extras_ticket_type, extras_quantity  = get_tickets_lists(tickets_menu_file, keep_track_fine_dinning)
    while True:
        print(f"{NAME_FESTIVAL}\n{len(NAME_FESTIVAL) * '='}")
        menu = (f"1. Make a Booking\n" \
                "2. Review Bookings\n" \
                "3. Exit")
        print(menu)
        choice = input("Enter your choice: ")
        if choice == '1':
            feedback = booking_a_ticket(type_of_ticket, ticket_price, extras_ticket_type, extras_quantity, keep_track_fine_dinning)
            print(feedback)
            print(extras_ticket_type, extras_quantity)
        elif choice == '2':
            pass
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
main()