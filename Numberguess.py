def numberguessgame():
    import random
    num = random.randint(1,10)

    print('I have chosen a number from 1 to 10. Please guess it. (5 Guesses)')
    i = 1
    gl = 5
    for i in range(1,6):
        guess = input()
        guess = int(guess)
        gl = 5 - i
        if guess < 0 or guess >10:
            print('You chose invalid number. Try again.')
            print('Guesses left : ' + str(gl))
            continue
        if guess == num:
            print('You guessed right. You Win.')
            break
        elif guess != num:
            print('Wrong. Try again.')
            print('Guesses left : ' + str(gl))
        if gl == 0:
            print('You lose. Chosen Number was: ' + str(guess))

        i = i + 1

numberguessgame()