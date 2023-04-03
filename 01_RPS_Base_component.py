import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an that is more than 0"

        # If infinite mode not choose, check response is an integer that is more than 0
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


def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# List of valid responses

rps_list = ["rock", "paper", "scissors", "xxx"]
yes_no_list = ["yes", "no"]

# Main routine goes here

# Ask user for # of rounds then loop
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Asl user for the # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode:" "Round {}".format(rounds_played + 1)
    else:
        heading = "normal mode :" "Round {}".format(rounds_played + 1, rounds)

    print(heading)

    choose_instruction = "Please choose rock (r)/ paper(p)/ scissors(s) or 'xxx' to exit"

    # Ask user for choice and check it's valid
    choose_error = "Please choose from Rock / Paper / Scissors (or xxx to end game)"

    # Ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice)

    # Compare choices
    if comp_choice == choose:
        result = "tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "scissors":
        result = "won"
    elif choose == "paper" and comp_choice == "rock":
        result = "won"
    elif choose == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"

    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(choose, comp_choice, result)

    # End game if exit code is typed
    if choose == "xxx":
        break

    # rest of loop / game
    print()
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they have played the game before.
# If 'no' show instructions


# ask user # of rounds then loop...

# Ask user if they want to see their game history
# If user answers 'yes' show game history

# Show game statistics
# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('******** END GAME SUMMARY ********')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
