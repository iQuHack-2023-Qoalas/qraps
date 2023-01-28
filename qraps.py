from numpy.random import randint

winning_bets = (7, 11)
losing_bets = (2, 3, 12)
other_bets = (1, 4, 5, 6, 8, 9, 10, 12)

user_balance = int(input('How much money would you like to load onto your account? [in USD] \n'))
initial_balance = user_balance

def run_point_bets(i, user_balance, bet):
    j = randint(1, 13)              #REPLACE
    print('You have rolled ' + str(j) + '.')
    if (j == i):
        print('Congratulations! You have won ' + str(bet) + ' USD.' )
        new_balance =  2*bet + user_balance
        return True
    elif(j == 7):
        print('I am sorry to inform you that you have lost ' + str(bet) + ' USD.')
        return False
    else:
        return run_point_bets(i, user_balance, bet)

def pa_yn(balance):                #Play again yes or no
    inp = input('Your current balance is ' + str(balance) + ' USD. Do you want to play again? [y/n] \n')
    if (inp == 'y'):
        return True
    elif (inp == 'n'):
        return False
    else:
        print('You must choose between [y/n]')
        return pa_yn(balance)

play_again = True           #We want the user to potentially play multiple rounds

while (play_again == True):

    bet = int(input('How much do you want to bet? \n'))
    i = randint(1, 13)                  #REPLACE
    print('You have rolled ' + str(i) + '.')
    while (bet > user_balance):

        print('You do not have enough money in your account')
        bet = int(input('Please input a number less than or equal to the balance in your account.'))

    user_balance -= bet

    if ((i in winning_bets)):
        print('Congratulations! You have won ' + str(bet) + ' USD.' )
        user_balance += 2*bet

    elif (i in losing_bets):
        print('I am sorry to inform you that you have lost ' + str(bet) + ' USD. ')
        pass

    elif (i in other_bets):
        bool = run_point_bets(i, user_balance, bet)
        print(bool)
        if bool == True:
            user_balance += 2 * bet
        elif bool == False:
            pass

    play_again = pa_yn(user_balance)

print('Thank you for participating. You have earned a total of ' + str(user_balance - initial_balance) + ' USD.')

