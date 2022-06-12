import random

#def Hangman(): 
 
words = []

with open("./words.txt", "r", encoding="utf-8") as f:
    for line in f:
        words.append(str(line))
    word = random.choice(words)
    print(word)





# def run():
    
# #    Hangman()



# if __name__ == '__main__':
#     run()
