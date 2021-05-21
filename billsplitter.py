import random

number = input('Enter the number of friends joining (including you):')
try:
    number = int(number)
except ValueError:
    print('\nNo one is joining for the party')
else:

    if number < 1:
        print('\nNo one is joining for the party')
    else:
        print('\nEnter the name of every friend (including you), each on a new line:')
        guests = {input(): 0 for _ in range(number)}
        try:
            bill = int(input('Enter the total bill value:\n'))
        except ValueError:
            pass
        else:
            answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
            if answer == 'Yes':
                choice = random.choice([*guests.keys()])
                print(f'{choice} is the lucky one!')

                part = round(bill / (number - 1), 2)
                guests = {key: part for key in guests}
                guests[choice] = 0

            else:
                print('No one is going to be lucky')
                part = round(bill / number, 2)
                guests = {key: part for key in guests}

            print(guests)
