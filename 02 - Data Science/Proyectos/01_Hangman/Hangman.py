import random
import os

def Hangman(): 
 
    words = []

    with open("./words.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))
        word = random.choice(words)
        print(word)

    lives = 5

    gap = []

    gap = ["_" for l in range(len(word)-1)]
    
    End_of_game = False

    while not End_of_game:
        input_letter = input("Enter a letter: ").strip().lower()
        assert input_letter.isalpha(), "solo puedes ingresar letras"
        #p=position
        for p in range(len(word)):
            letter = word[p]
            if letter == input_letter:
                gap[p] = letter
        if input_letter not in word:
            lives -=1
            print(f"You have {lives} lives")
            if lives == 0:
                End_of_game = True
                print("You Lose!")
        print(f"{' '.join(gap)}")

        if "_" not in gap:
            os.system("cls")
            End_of_game = True
            print("You Win, Congratulation!")
           



def run():
    Hangman()



if __name__ == '__main__':
    run()
