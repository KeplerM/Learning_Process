import random

list_word = []
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    for line in f:
        list_word.append(str(line))
    #print(list_word)
    word = random.choice(list_word)
    print(word)


lives = len(word)

d = []

for w in range(len(word)-1):
    d += "_"


end_of_game = False

while not end_of_game:
    letter_input = input("Enter a letter: " ).lower()
    for p in range(len(word)):
        letter = word[p]
        if letter == letter_input:
            d[p] = letter
    if letter_input not in word:
        lives -= 1
        print(f"You have {lives} lives")
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(f"{' '.join(d)}")

    if "_" not in d:
        end_of_game = True
        print("You win, Congratulation!")
#print(d)