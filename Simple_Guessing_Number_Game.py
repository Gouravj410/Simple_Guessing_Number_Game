import random

def guess_number_game():
    while True:
        correct_num=random.randint(1, 10)
        print("Let's play Guessing Game.")
        print("I guessed a number Between 1 to 10")
        attempt=1
        while attempt<=3:
            num=int(input("Guess a number : "))
            if num<correct_num:
                print("Too Low!")
                if attempt<3:
                    print(f"You have left {3-attempt} Attempt.")
                else:
                    print("Game Over")
            elif num>correct_num:
                print("Too High!")
                if attempt<3:
                    print(f"You have left {3-attempt} Attempt.")
                else:
                    print("Game Over")
            else:
                print("""
                         *******************
                         *******************
                         **   Well Done!  **
                         **   You Win     **
                         *******************
                         *******************
                     """)
                break
            attempt+=1

        print(f"The Correct number is {correct_num}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

guess_number_game()
