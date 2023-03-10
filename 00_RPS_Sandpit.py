# Functions go here

def choice_maker(question):
    error = "please choose from rock/ paper/ scissors (or xxx to quit)"

    while True:

        response = input(question).lower()

        if response == "r" or response == "rock":
            print()
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return

        # Check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)

#Looop for checking purposes





