# Functions go here
def choice_checker(question):
    while True:

        # Ask user for choice(Put it in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            print()
            return "rock"

        elif response == "p" or response == "paper":
            print()
            return "paper"

        # Check for exit code
        elif response == "xxx":
            print()
            print()
            return response

        else:
            if response == "s" or response == "scissors":
                print()
                return "scissors"

            # If user chooses anything other than r/p/s display error message
            else:
                print()
                print("==============================================================")
                print("*Please choose rock, paper, or scissors ( or 'xxx' to quit )*")
                print("==============================================================")
                print()


# Main routine goes here


# loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check if it's valid
    user_choice = choice_checker("Choose ROCK/ PAPER / SCISSORS(R/P/S):")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))
    print()


