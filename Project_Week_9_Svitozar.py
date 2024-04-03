import useful_functions
NAME_FESTIVAL = "MUSIC FARM FESTIVAL"
def get_tickets_lists(filename, extras_file):
    # Sales_2022.txt
    types_of_tickets = []
    ticket_prices = []
    max_available_tickets = []
    tickets_sold = []
    ticket_file = open(filename)
    for line in ticket_file:
        line = line.rstrip()
        if line:
            info_line = line.split(",")
            types_of_tickets.append(info_line[0])
            ticket_prices.append(int(info_line[1]))
            max_available_tickets.append(int(info_line[2]))
            tickets_sold.append(int(info_line[3]))
    ticket_file.close()
    # Extras.txt
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
    return  types_of_tickets, ticket_prices, max_available_tickets, tickets_sold, extras_ticket_type, extras_quantity
# 1. Booking a Ticket
def booking_a_ticket(types_of_tickets, ticket_prices, extras_quantity):
    ticket_day_list = []
    people_in_group_list = []
    feedback_to_user = ""
    # Greeting
    option = "BOOKING"
    full_name = f"{NAME_FESTIVAL} ({option})"
    print(f"\n{full_name}\n{len(full_name) * '='}")
    # Display price
    for i, name in enumerate(types_of_tickets):
        print(f"{i+1}. {name:<15}€{ticket_prices[i]:.2f}")
    # Collect booking data from user
    name = useful_functions.get_string("Enter your name => ")
    phone_number = useful_functions.get_positive_int("Enter your phone number => ")
    while True:
        ticket_type_choice = input("Choose the ticket type: ")
        if ticket_type_choice == "1" or ticket_type_choice == "2" or ticket_type_choice == "3":
            break
        else:
            print("Please enter a valid option.")
    people_in_group = useful_functions.get_number_max4("How many people in your group? ")
    while True:
        if ticket_type_choice == "1":
            ticket_type = "Day1"
            if people_in_group > 1 and people_in_group <= 4:
                while True:
                    fine_dining = useful_functions.get_answer_string("Do you require a fine dining pass (Y/N)? ").capitalize()
                    if fine_dining == "Y" or fine_dining == "Yes":
                        answer_fine_dining = "Yes"
                        extras_quantity[0] += people_in_group
                        price = (people_in_group * ticket_prices[0]) + (20 * people_in_group)
                        break
                    elif fine_dining == "N" or fine_dining == "No":
                        answer_fine_dining = "No"
                        price = ticket_prices[0] * people_in_group
                        break
                    else:
                        print('Please answer "Yes" or "No". ')
                break
            else:
                answer_fine_dining = "No"
                price = ticket_prices[0]
                break
        elif ticket_type_choice == "2":
            ticket_type = "Day2"
            if people_in_group > 1 and people_in_group <= 4:
                while True:
                    fine_dining = useful_functions.get_answer_string("Do you require a fine dining pass (Y/N)? ")
                    fine_dining = fine_dining.capitalize()
                    if fine_dining == "Y" or fine_dining == "Yes":
                        answer_fine_dining = "Yes"
                        extras_quantity[1] += people_in_group
                        price = (people_in_group * ticket_prices[1]) + (20 * people_in_group)
                        break
                    elif fine_dining == "N" or fine_dining == "No":
                        answer_fine_dining = "No"
                        price = ticket_prices[1] * people_in_group
                        break
                    else:
                        print('Please answer "Yes" or "No" ')
                break
            else:
                answer_fine_dining = "No"
                price = ticket_prices[1]
                break
        elif ticket_type_choice == "3":
            ticket_type = "Weekend-Camp"
            answer_fine_dining = "Included"
            price = ticket_prices[2] * people_in_group
            break
        else:
            print("Invalid choice. Please enter a valid option. ")
    ticket_day_list.append(ticket_type)
    people_in_group_list.append(people_in_group)
    # Display feedback to user
    feedback_to_user = (f"\nBooking Details\n" \
                    "---------------\n" \
                    f"{'Name:':<20}{name}\n" \
                    f"{'No of People:':<20}{people_in_group}\n" \
                    f"{'Ticket Type:':<20}{ticket_type}\n" \
                    f"{'Fine Dining:':<20}{answer_fine_dining}\n" \
                    f"{'Total Cost:':<20}€{float(price):.2f}\n")
    # info client_ticket_booking
    full_name_with_list = name.split(" ")
    full_name_with_ = "_".join(full_name_with_list)
    ticket_name_sale = open(f"{full_name_with_}_sale.txt", "w")
    ticket_name_sale.write(f"{ticket_type},{phone_number},{people_in_group},{price:.2f},{answer_fine_dining}")
    ticket_name_sale.close()
    return feedback_to_user, ticket_day_list, people_in_group_list, extras_quantity
# 2. Bookings Review
def bookings_review(new_ticket_name_list, new_people_in_group_list):
    # Greeting
    option = "Review Bookings"
    full_name = f"{NAME_FESTIVAL} ({option})"
    print(f"\n{full_name}\n{len(full_name) * '='}")
    # Tickets_sold Summary
    day1_list = []
    day2_list = []
    weekend_camp_list = []
    for i, type in enumerate(new_ticket_name_list):
        if type == "Day1":
            day1_list.append(int(new_people_in_group_list[i]))
        elif type == "Day2":
            day2_list.append(int(new_people_in_group_list[i]))
        else:
            weekend_camp_list.append(int(new_people_in_group_list[i]))
    total_day1 = sum(day1_list)
    total_day2 = sum(day2_list)
    total_weekend_camp = sum(weekend_camp_list)
    return total_day1, total_day2, total_weekend_camp
# 3. Exit
def exit_option(sales_file, extras_file, type_of_ticket, new_ticket_name_list, new_people_in_group_list, ticket_price, max_available_tickets, extras_ticket_type, extras_quantity_new_list):
    day1_list = []
    day2_list = []
    weekend_camp_list = []
    for j, name in enumerate(new_ticket_name_list):
        if name == "Day1":
            day1_list.append(int(new_people_in_group_list[j]))
        elif name == "Day2":
            day2_list.append(int(new_people_in_group_list[j]))
        else:
            weekend_camp_list.append(int(new_people_in_group_list[j]))
    total_day1 = sum(day1_list)
    total_day2 = sum(day2_list)
    total_weekend_camp = sum(weekend_camp_list)
    total_all_days_list = []
    total_all_days_list.append(total_day1)
    total_all_days_list.append(total_day2)
    total_all_days_list.append(total_weekend_camp)
    # The bookings file Sales_2024.txt is updated.
    change_sales_file = open(sales_file, "w")
    for i, name in enumerate(type_of_ticket):
        change_sales_file.write(f"{name},{ticket_price[i]},{max_available_tickets[i]},{total_all_days_list[i]}\n")
    change_sales_file.close()
    # The file extras.txt keeps track of the number attending the fine dining (updated).
    extras_track_file = open(extras_file, "w")  # open file in write mode
    for k, name in enumerate(extras_ticket_type):
        extras_track_file.write(f"{name},{extras_quantity_new_list[k]}\n")  # write data to file
    extras_track_file.close()  # Close the file after writing
def main():
    sales_file = "Sales_2024.txt"
    extras_file = "Extras.txt"
    type_of_ticket, ticket_price, max_available_tickets, tickets_sold, extras_ticket_type, extras_quantity = get_tickets_lists(sales_file, extras_file)
    new_ticket_name_list = []
    new_people_in_group_list = []
    extras_quantity_new_list = []
    extras_quantity_new_list += extras_quantity
    while True:
        cow = "\U0001F404"
        tractor = "\U0001F69C"
        sunflower = "\U0001F33B"
        multiple_musical_notes = "\U0001F3B6"
        guitar = "\U0001F3B8"
        full_emoji = f"{guitar}{cow}{multiple_musical_notes}{tractor}{sunflower}"
        full_greeting = f"{NAME_FESTIVAL} {full_emoji}"
        print(f"{full_greeting}\n{len(full_greeting) * '=' + '======'}")
        menu = (f"1. Make a Booking\n" \
                "2. Review Bookings\n" \
                "3. Exit")
        print(menu)
        choice = input("\nEnter your choice: ")
        if choice == '1':
            feedback, ticket_name_list, people_in_group_list, extras_quantity_new = booking_a_ticket(type_of_ticket, ticket_price, extras_quantity_new_list)
            print(feedback)
            while True:
                return_button = input("Press Return to continue: ")
                if return_button == "":
                    break
                else:
                    print("Invalid input. Press Return to continue:")
            new_ticket_name_list += ticket_name_list
            new_people_in_group_list += people_in_group_list
        elif choice == '2':
            day1, day2, weekend_camp = bookings_review(new_ticket_name_list, new_people_in_group_list)
            print(f"{'Day1:':<20}{day1}\n{'Day2:':<20}{day2}\n{'Weekend-Camp:':<20}{weekend_camp}\n")
            print(f"{'Fine Dining Day 1:':<20}{extras_quantity_new_list[0]}\n{'Fine Dining Day 2:':<20}{extras_quantity_new_list[1]}\n")
        elif choice == '3':
            exit_option(sales_file, extras_file, type_of_ticket, new_ticket_name_list, new_people_in_group_list, ticket_price, max_available_tickets, extras_ticket_type, extras_quantity_new_list)
            print("Exiting...")
            print("\U0001F44B")
            break
        else:
            print("Invalid choice. Please enter a valid option. ")
main()