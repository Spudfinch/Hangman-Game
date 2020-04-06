import random


def scaffold(guesses):
    while guesses == 6:
        print("________")
        print("|     |")
        print("|     ")
        print("|    ")
        print("|     ")
        print("|_______")
        return ""
    if guesses == 5:
        print("________")
        print("|     |")
        print("|     0")
        print("|     ")
        print("|     ")
        print("|_______")
        return ""
    elif guesses == 4:
        print("________")
        print("|     |")
        print("|     0")
        print("|     !")
        print("|     ")
        print("|_______")
        return ""
    elif guesses == 3:
        print("________")
        print("|     |")
        print("|     0")
        print("|    /!\ ")
        print("|     ")
        print("|_______")
        return ""
    elif guesses == 2:
        print("________")
        print("|     |")
        print("|     0")
        print("|    /!\ ")
        print("|    ")
        print("|_______")
        return ""
    elif guesses == 1:
        print("________")
        print("|     |")
        print("|     0")
        print("|    /!\ ")
        print("|    /")
        print("|_______")
        return ""
    elif guesses == 0:
        print("________")
        print("|     |")
        print("|     0")
        print("|    /!\ ")
        print("|    / \ ")
        print("|_______")
        return ""


with open('sowpods.txt') as f:
    words = list(f)


def wd(w):
    random.shuffle(w)
    return random.choice(w)

print(words)
print(len(words))
print("the word is %s" % wd)
guesses_left = 6
word_to_guess = wd(words)
word_to_guess = list(word_to_guess)
word_to_guess.remove("\n")

print(word_to_guess)
correct_letters = list()
incorrect_letters = list()
game_over = True

while guesses_left > 0 and game_over == True:
    guessed_let = (input("guess a letter: "))
    if len(guessed_let) > 1:
        print("\nNo cheating! one letter at a time.")
    if len(guessed_let) == 0:
        print("\nNo guess is no good! pick a letter")
    if len(guessed_let) == 1:
        if guessed_let in correct_letters or guessed_let in incorrect_letters:
            print(scaffold(guesses_left))
            print("\nCorrect letters: " + "".join(correct_letters))
            print("\nIncorrect letters: " + "".join(incorrect_letters))
            print("\nYou've already guessed that one silly, guess again")
        if guessed_let not in word_to_guess and guessed_let not in incorrect_letters:
            guesses_left -= 1
            print(scaffold(guesses_left))
            incorrect_letters.append(guessed_let)
            print("\nGuess incorrect! You lose a life! ")
            print("\nYou have " + str(guesses_left) + " remaining.")
            print(scaffold(guesses_left))
        if guessed_let in word_to_guess and guessed_let not in correct_letters:
            print(scaffold(guesses_left))
            add = word_to_guess.count(guessed_let)
            for _ in range(add):
                correct_letters.append(guessed_let)
            print("\nWell done, you have found a letter")
        if len(word_to_guess) == len(correct_letters):
            print("\nWell done you have won! you live to hang another day!")
            play_again = input("\nWould you like to play again? yes or no?: ")
            if play_again == "yes":
                guesses_left = 6
                wd(words)
                word_to_guess = wd(words)
                word_to_guess = list(word_to_guess)
                word_to_guess.remove("\n")
                print(str(word_to_guess))
                incorrect_letters.clear()
                correct_letters.clear()
            if play_again == "no":
                break
        for index in word_to_guess:
            if index in correct_letters:
                print(" " + index + " ", end="")
            else:
                print(" _ ", end="")


if guesses_left == 0:
    print("\nYou have ran out of chances and have been hung by your neck.")
