"""Play the Brain Even Game."""

import random
import prompt


def main():
    """Play Brain Even game"""     
    print('Welcome to the Brain Games!') #ЧТО ЕСЛИ ПОПРОБОВАТЬ ПЕРЕИСПОЛЬЗОВАТЬ МЕТОД ИЗ ДРУГОГО ФАЙЛА BRAIN_GAMES.PY
    name = prompt.string('May I have your name? ') #ЧТО ЕСЛИ ПОПРОБОВАТЬ ПЕРЕИСПОЛЬЗОВАТЬ МЕТОД ИЗ ДРУГОГО ФАЙЛА CLY.PY
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".') 
    i = 0
    while i <= 2: 
        number = random.randint(0,100)
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question:', number)
        guess = prompt.string('Your answer: ')
        if guess != right_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(guess, right_answer))
            print("Let's try again, " + name + "!")
            return 
        print('Correct!')
        i += 1
    print('Congratulations, ' + name + '!')

        
if __name__ == '__main__':
    main()