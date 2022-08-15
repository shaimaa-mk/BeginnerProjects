import os
import re
import random
# os.system('clear' if os.name == 'posix' else 'cls')


def play(flag):
    start = flag
    while start:
        print("\n")
        print("Rock, Paper, Scissors  - Shoot")
        userChoice = input("Choose : [R]ock, [P]aper, [S]cissors")
        if not re.match('[ReSsPp]', userChoice):
            print("Please choose a letter !")
            print("[R]ock, [P]aper, [S]cissors")
            continue
        print(f"Your Choice : {userChoice}")
        choices = ['P', 'R', 'S']
        opponenetChoice = random.choice(choices)
        print(f"I choice {opponenetChoice}")
        if opponenetChoice == userChoice.upper():
            print("Tie!")
        elif opponenetChoice == 'R' and userChoice.upper() == 'S':
            print("Scissors beats rock. I win!")
            continue
        elif opponenetChoice == 'S' and userChoice.upper() == 'P':
            print("Scissors beats paper. I win!")
            continue
        elif opponenetChoice == 'P' and userChoice.upper() == 'R':
            print("Paper beats rock. I win!")
            continue
        else:
            print("You win!")
            again = input("Would you play again? Enter [Yes/No]")
            if again.lower() == 'yes':
                play(True)
            elif again.lower() == 'no':
                print("Have a nice day.")
                break


answer = input("Welcome to RockPaperScissors Game! Enter Yes to Play, or No to get out.")
if answer.lower() == 'yes':
    play(True)
elif answer.lower() == 'no':
    print("Have a nice day.")

