import random
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)
#The random.choice() method is used to randomly select a word from the word_bank list and to assign it to the word variable.
guessedWord = ['_'] * len(word)
#In Python, you can multiply a list by an integer and the list will repeat that amount of times
attempts = 10
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()
   
  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
        print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: ' + word)
