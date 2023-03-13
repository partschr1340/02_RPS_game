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
choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter for infinite mode
rounds = check_rounds()

mode = "regular"

if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds:

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
