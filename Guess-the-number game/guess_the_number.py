import random

while True:
    secret_no = random.randint(1,100)
    guess_count = 0
    guess_limit = 0

    while True:
        print("What level of difficulty you want to play ?")
        x = input("Easy / Medium / Hard ?")
        x = x.lower()

        if x == "easy" or x == "e":
            print("Selected Difficulty: Easy")
            print("You will get 10 tries before the game ends.")
            guess_limit = 10
            break
        elif x == "medium" or x == "m":
            print("Selected Difficulty: Medium")
            print("You will get 6 tries before the game ends.")
            guess_limit = 6
            break
        elif x == "hard" or x == "h":
            print("Selected Difficulty: Hard")
            print("You will get 3 tries before the game ends.")
            guess_limit = 3
            break
        else:
            print("Invalid Input")

    while guess_count < guess_limit:
        guess = int(input("Guess the number :"))
        guess_count += 1

        if (guess - secret_no) > 20:
            print("Way Lower!")
        elif (guess - secret_no) < -20:
            print("Way Higher!")
        elif 0 < (guess - secret_no) < 20:
            print("Lower!")
        elif -20 < (guess - secret_no) < 0:
            print("Higher!")
        elif (guess - secret_no) == 0:
            print("You Got It !")
            print("Congratulations !")
            print(f"You got it in {guess_count} attempts.")
            break
        else:
            print("Invalid Input")

    if guess == secret_no:
        pass
    else:
        print("You lost!")



    play_again  = input("Want to play again (yes/no) ?\n").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing!")
        break