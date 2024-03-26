def get_string(prompt):
    while True:
        try:
            answer = input(prompt)
            length = len(answer)
            if answer.isalpha() and length > 0 and length < 15:
                break
            else:
                print("The name must be alphabetic and between 1 and 14 characters.")
        except:
            print("Error occured ")
    return answer
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
    print(name)
if __name__ == "__main__":
    main()