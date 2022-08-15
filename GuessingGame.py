import random
attempts = []


def show_score():
    if len(attempts) <= 0:
        print("It's your to taking!")
    else:
        print(f"The current high score is : {min(attempts)}")


def get_stated(flag, plname):
    random_number = int(random.randint(1, 10))
    attemp = 0
    show_score()
    while flag.lower() == 'yes':
        try:
            travl_num = int(input("Hey traveler! Pick Up a number:"))
            if travl_num < 0 or travl_num > 10:
                raise ValueError("Guess a right number between 1 and 10!")
            if travl_num == random_number:
                print(f"Congratulations {plname}! you got it.")
                attemp += 1
                attempts.append(attemp)
                print(f"It took you {attemp} attempts.")
                play_again = input("Would you play again? [Enter Yes/No]")
                if play_again.lower() == 'yes':
                    get_stated(play_again, plname)
                if play_again.lower() == 'no':
                    print("That's Cool. Have A nice day.")
                    break
            elif travl_num > random_number:
                print("It's lower!")
                attemp += 1
            elif travl_num < random_number:
                print("It's higher!")
                attemp += 1
        except ValueError as err:
            print("Oh no! It's not seem Valid Value. Try again ...")
            print(f"{err}")
    else:
        print("Have a nice day!")


def start_game():
    print(" Hi traveler! Welcome to Guessing Game")
    name = input(" What is your name?")
    wann_play = input(f"Then {name}, would you take a try with guessing game? [Enter Yes/No]")
    get_stated(wann_play, name)


start_game()
