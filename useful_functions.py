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
                print("The name must be alphabetic and between 1 and 14 characters.")
        except:
            print("Error occured.")
    return full_name
def get_answer_string(prompt):
    while True:
        try:
            answer = input(prompt)
            answer_length = len(answer)
            if answer_length != 0 and answer.isalpha():
                break
            else:
                print("Error occured")
        except:
            print("Error occured")
    return answer
def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                break
            else:
                print("It must be a positive number ")
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
    # num = get_positive_int("Enter a number ")
    # print(num)
    # answer = get_answer_string("Y/N ?")
    # print(answer)
if __name__ == "__main__":
    main()