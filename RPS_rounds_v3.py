# Function used to check input is valid

def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

rounds_played = 0
choose_instruction = "Please choose Rock(r), Paper(p) or Scissors(s)"

# Asl user for the # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode:" "Round {}".format(rounds_played + 1)
        print(heading)
        choose = input("{} or 'xxx' to end :".format(choose_instruction))

        # Ebd game if exit code is typed
        if choose == "xxx":
            break

        # rest of loop / game
        print("You chose {}".format(choose))

        rounds_played += 1

        # end game if requested # of rounds has been played
        if rounds_played == rounds:
            break
