def get_string(prompt):
    while True:
        try:
            name = input(prompt)
            length = len(name)
            if length > 0 and length < 15:
                break
        except:
            print("The length of the name must be between 1 and 14 characters.")
    return name
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