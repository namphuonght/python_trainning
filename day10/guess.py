"""
Build number guessing game

"""


# =============================================================================


__auth__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/10'
__status__ = 'development'


# =============================================================================


import random


# =============================================================================
class Guess(object):
    
    def __init__(self, N):
        self.N = N


# =============================================================================


    def ran_number(self):
        return random.randrange(1, self.N)


# =============================================================================


    def play(self):
        print("Guess a number between 1 and %d" %(self.N))

        number = self.ran_number()
        numberOfGuess = 0
        while True:
            guess = int(input('Player: '))
            if numberOfGuess > 9:
                print('\n You Loose!\n')
                break
            elif guess > number:
                print('Lower number please!\n')
                numberOfGuess += 1
            elif guess < number:
                print('Higher number please!\n')
                numberOfGuess += 1
            else:
                print("You guessed the number in %d attempts" %(numberOfGuess))
                break



