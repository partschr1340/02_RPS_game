# Version 2 - error message included when calling functions.


# Functions go here
def choice_checker(question, error):

    while True:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissors"

        # Check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)


# Main routine goes here


# Loop for checking purposes
user_choice = ""
while user_choice != "xxx":
    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose ROCK/PAPER/SCISSORS(r/p/s): ")

    # print out choice for comparison purposes
    print()
    print("You chose {}".format(user_choice))
    print()
