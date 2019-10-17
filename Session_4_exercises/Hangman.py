# Hangman game is developed. A random word is generated and the user has 7 guesses to figure out the word
from random_word import RandomWords
from PyDictionary import PyDictionary
r = RandomWords()
dictionary = PyDictionary()
word_of_the_game = r.get_random_word(hasDictionaryDef="true", minLength=6, maxLength=10)  # Return a single random word
#print(word_of_the_game)
print(dictionary.meaning(word_of_the_game))     # gets the meaning of the input word to assist user
guess_counter = 0  # keeps a count of the number of guesses so far

#  creating an empty string with blanks to keep track of the letters correctly guessed
blank_word = []
length = int(len(word_of_the_game))
for i in range(0, length):
    blank_word.append("_")
print(blank_word)

# looping till the user gets the word right or he has used up all his guesses

while guess_counter <= 7:
    x = input("Take a guess: ")    # gets a guess letter from the user
    flag = word_of_the_game.find(x)     # finds the index position of the first occurence of the letter if it exists
    if flag >= 0:
        while flag >= 0:
            blank_word_list = list(blank_word)
            blank_word[flag] = x        # replacing the position of the correctly found letter in the blank word
            if word_of_the_game.count(x) == 1:
                print(blank_word)
            word_of_the_game = word_of_the_game.replace(x, '_', 1)  # replace it in original input string
            flag = word_of_the_game.find(x)     # recursive call in case more than one occurence of a letter is there
    else:
        guess_counter = guess_counter + 1      # if not found, increase the guess count

    if guess_counter == 7:      # if guess count reaches 7, exit the loop
        break
    if word_of_the_game.count("_") == len(word_of_the_game):    # if all letters are found, exit the loop
        break

if guess_counter == 7:
    print("Player one lost! Please try again")
elif len(blank_word) == len(word_of_the_game) and guess_counter != 7:
    print("Player one wins!!")

print(blank_word)
