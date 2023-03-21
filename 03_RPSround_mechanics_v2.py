def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer more than 0"

        if response == "":
            return response

        try:
            response = int(response)

            if response < 1:
                print(round_error)
                continue
            else:
                return response

        except ValueError:
            print(round_error)
            continue


# Main routine goes here

rounds_played = 0
mode = "regular"

choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"


def choice_checker(question):
    error = "please choose from rock/ paper/ scissors (or xxx to quit)"

    while True:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissors"


# Ask user for # of rounds, <enter for infinite mode
rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds:
    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode:Round {}".format(rounds_played + 1)
        # increase number of rounds for infinite mode so that our rounds
        # played is never equal to the number of rounds wanted
        rounds += 1
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or xxx to end:".format(choose_instruction))
    rounds_played += 1

    # End game if exit code is typed
    if choose == "xxx":
        break
