import random 
import string 


# (optional) Here we're defining different stages of losing and how will the user see how many moves he has got left
loser_pics= ['''
 +----+
 |    O   
 |     
 |     
===''','''
 +----+
 |    O   
 |    |  
 |     
=== ''','''
 +----+
 |    O   
 |   /|  
 |     
=== ''','''
 +----+
 |    O   
 |   /|\  
 |     
=== ''','''
 +----+
 |    O   
 |   /|\  
 |   /   
=== ''','''
 +----+
 |    O   
 |   /|\  
 |   / \  
=== ''']

alphabet = list(string.ascii_lowercase)
words = []

# opening the file and getting all words (lines) with more than 3 letters
with open('english_words.txt') as f:
    words = [line.strip() for line in f if len(line)>4]

# generating a random index and choosing corresponding word from the list
def word_generator():
    global word
    random_index = random.randint(0,len(words))
    word=words[random_index]   
    return word


'''here 'word' is the goal that user is trying to find. 'new_word' is what user guesses and only the correct letters will be 
displayed and rest of the letters will be shown with a '_' . We'll also keep track of number of guesses with guess_count
 and guessed_letters will be for user to track which letters he has already tried.'''
def set_game():
    global new_word
    global guess_count
    global word
    global list_new_word
    global list_word
    global guessed_letters
    
    list_word = list(word)
    new_word = '_'*len(word)
    list_new_word = list(new_word)
    guess_count = 1
    guessed_letters = []
    return

# defining correct_count and wrong_count to track success of the player, these will be used when the player decides not to
# play anymore 
correct_count = 0
wrong_count = 0


def hangman():
    global new_word
    global guess_count
    global correct_count
    global wrong_count

    word_generator()
    set_game()

    while guess_count<=6 and new_word!=word:
        guess=input('guess a letter: ').lower()


        if guess in guessed_letters:
            print('you already guessed this letter')   

        elif guess in list_word:
            # if the guess is correct, we find which place that letter belongs to and add it on nword
            for i in range(len(word)):
                if guess==list_word[i]:
                    list_new_word[i]=guess
            new_word=''.join(list_new_word)
            print(f"you've tried these letters: {','.join(guessed_letters)} ")
            print(new_word)
        elif len(guess) != 1 or guess not in alphabet:
            print('Please enter a single letter each time')

        else:
            if guess_count == 6:
                print(loser_pics[guess_count-1])
            else:    
                print(f'{loser_pics[guess_count-1]}\n Wrong! You have',6-guess_count,'more guesses')
                guessed_letters.append(guess)
                print(f"You've tried these letters: {','.join(guessed_letters)} ")
                print(new_word)
            guess_count += 1
        continue

    if new_word == word:
        correct_count += 1
        print('you won')
        play_again=input('wanna play again? yes[y] or no[n]: ')
        if play_again.lower() == "y" or play_again.lower() == 'yes':
            hangman()
        else:
            print(f"Thanks for playing! You've guessed {correct_count}/{correct_count + wrong_count} words right")
            return
    else:
        wrong_count += 1
        print('you lost')
        print('the word was ',word)
        play_again=input('wanna play again? yes[y] or no[n]: ')
        if play_again.lower() == "y" or play_again.lower() == 'yes':
            hangman()
        else:
            print(f"Thanks for playing! You've guessed {correct_count}/{correct_count + wrong_count} words right")
            return

hangman()
