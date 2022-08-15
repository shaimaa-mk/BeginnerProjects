import random


def dice_game(flag):
    min_val = 1
    max_val = 6
    roll_dice = flag
    while roll_dice.lower() == 'y':
        print("Dices Rolling ...")
        my = random.randint(min_val, max_val)
        your = random.randint(min_val, max_val)

        print("The values are:")
        print(f"Your Dice: {your}")
        print(f"My Dice: {my}")
        if your > my:
            print("You win!")
        elif your < my:
            print("I win!")
        else:
            continue

        again = input("Would you to play again? Enter [y/n]")
        if again.lower() == 'y':
            continue
        elif again.lower() == 'n':
            print("That's Cool! Hav a nice day.")
            break


print("Welcome to Dice Game!")
answer = input("Hi there! Would you play Dice Game? Enter[y/n].")
dice_game(answer)




