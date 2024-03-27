def get_string(prompt):
    while True:
        try:
            answer = input(prompt)
            answer = answer.capitalize()
            parts = answer.split(" ")
            full_name_list = []
            name_length = len(parts)
            amount_isalpha = 0
            length_all_parts = 0
            for part in parts:
                if part.isalpha():
                    amount_isalpha += 1
                    length_all_parts += len(part)
                    full_name_list.append(part.capitalize())
                    full_name = " ".join(full_name_list)
            if name_length == amount_isalpha and 0 < len(full_name) < 15:
                break
            else:
                print("The name must be alphabetic and between 1 and 14 charactersAAAAAAAA.")
        except:
            print("Error occured.")
    return full_name
def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                break
        except:
            print("Error occured")
    return num

def get_number_max4(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 1 and num <= 4:
                break
            else:
                print("Max 4 tickets")
        except:
            print("Error occured")
    return num
def main():
    name = get_string("Enter your name: ")
    print(f"Name: {name}")
if __name__ == "__main__":
    main()