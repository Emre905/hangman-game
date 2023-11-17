import random 
import string 


# (optional) Here we're defining different stages of losing and how will the user see how many moves he has got left
# We'll seperate all lines and one step at each time remove the last character (except for the first '|' signs).
# In the end we'll put back together it and append it to the list HANGMAN_PICS
LAST_PIC="""
 +----+
 |    O
 |   /|\\
 |   / \\
=== 
"""
HANGMAN_LAST_PIC=LAST_PIC.splitlines()
HANGMAN_PICS=['\n'.join(HANGMAN_LAST_PIC)]
for j in range(2,4):
    for i in range(3):
        if len(HANGMAN_LAST_PIC[-j]) > 2:
            HANGMAN_LAST_PIC[-j] = HANGMAN_LAST_PIC[-j][:-1].rstrip()
            HANGMAN_PICS.append('\n'.join(HANGMAN_LAST_PIC))
        else:
            continue
            
ALPHABET = list(string.ascii_lowercase)
WORDS = []

# opening the file and getting all words (lines) with more than 3 letters
with open('english_words.txt') as f:
    WORDS = [line.strip() for line in f if len(line.strip())>3]

# generating a random index and choosing corresponding word from the list
def word_generator():
    random_index = random.randint(0,len(WORDS)-1)
    word = WORDS[random_index]   
    return word


'''here 'word' is the goal that user is trying to find. 'guessed_word' is what user guesses and only the correct letters will be 
displayed and rest of the letters will be shown with a '_' . We'll also keep track of number of guesses with guess_count
 and guessed_letters will be for user to track which letters he has already tried.'''
def set_game(word):
    list_word = list(word)
    guessed_word = '_'*len(word)
    list_guessed_word = list(guessed_word)
    guess_count = 1
    guessed_letters = []
    return list_word, guessed_word, list_guessed_word, guess_count, guessed_letters

#defining a function that asks user at the end of each game to play again
def play_again():
    play = input('Would you like to play again? Yes [Y] or No [N]: ').lower()
    return play == 'y' or play == 'yes'

# Defining win_count and lose_count in the main function to track success of the player, these will be used when the player
# decides not to play anymore
def hangman(win_count = 0, lose_count = 0):
    
    word = word_generator()
    list_word, guessed_word, list_guessed_word, guess_count, guessed_letters = set_game(word)

    # Main part will work when the user still has guesses and didn't guess the correct word yet.
    while guess_count<=6 and guessed_word!=word:
        guess = input('guess a letter: ').lower()

        # First, putting 2 conditions to make sure the input is not given before and is a single letter from ALPHABET
        if guess in guessed_letters:
            print('you already guessed this letter')   
            
        elif len(guess) != 1 or guess not in ALPHABET:
            print('Please enter a single letter each time')
        
        # if the guess is correct, we find which place that letter belongs to and add it on guessed_word
        elif guess in list_word:
            for i in range(len(word)):
                if guess == list_word[i]:
                    list_guessed_word[i]=guess
            guessed_word = ''.join(list_guessed_word)
            print(f"you've tried these letters: {','.join(guessed_letters)} ")
            print(guessed_word)
            
        # when user guess is wrong, we print out how many attempts he has left and which letters was tried.
        else:
            if guess_count == 6:
                print(HANGMAN_PICS[-guess_count])
            else:    
                print(f'{HANGMAN_PICS[-guess_count]}\n Wrong! You have',6-guess_count,'more guesses')
                guessed_letters.append(guess)
                print(f"You've tried these letters: {','.join(guessed_letters)} ")
                print(guessed_word)
            guess_count += 1
        continue
        
    # When the user guesses the word correctly, we finish the game, increase the win count and ask to play again.
    if guessed_word == word:
        print('You won')
        win_count += 1
    else:
        print('You lost')
        print('The word was ', word)
        lose_count += 1
    
    # Offering to play again
    if play_again():
        hangman(win_count, lose_count)
    else:
        print(f"Thanks for playing! You've guessed {win_count}/{win_count + lose_count} words right")
        return

hangman(win_count, lose_count)
