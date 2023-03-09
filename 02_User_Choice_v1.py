# Functions go here
def choice_checker(question):
    while True:

        response = input(question).lower()

        if response == "r" or response == "rock":
            return response

        elif response == "p" or response == "paper":
            return response
        else:
            if response == "s" or response == "scissors":
                return response
            else:
                print()
                print("Please choose rock, paper, or scissors")
                print()


# Main routine goes here


# Ask user for choice and check it's valid
user_choice = choice_checker("Choose rock/ paper/ scissors (r/p/s)")

