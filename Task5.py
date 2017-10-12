while True:
    x = input('Input your number, please ')
    try:
        print('The next number for the number', int(x), 'is', int(x)+1, '\n The previous number for the number', int(x), 'is', int(x)-1)
        break
    except ValueError:
        print('Try again')
        continue

