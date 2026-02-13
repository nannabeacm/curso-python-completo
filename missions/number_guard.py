code_working = True

while code_working:
    ask_user = input("Please say a number: ")
    try:
        converted_input = int(ask_user)
    except ValueError:
        print("That is not a number. Try again.")
    else:
        print("Thank you!")
        break