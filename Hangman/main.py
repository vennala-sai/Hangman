#Step 5

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

game_over = False
lives = 6

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guess_tracker = []
for _ in range(word_length):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guess_tracker:
      print("You've already guessed this letter.")
    guess_tracker.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        game_over = True
        print("You win.")

    print(hangman_art.stages[lives])