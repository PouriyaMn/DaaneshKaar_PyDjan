usr = input('enter your username: '.title())
psw = input('enter your password: '.title())

if usr == 'admin' and psw == 'admin':
    print('Welcome')
elif usr == 'admin':
    print('Wrong Data')
else:
    print(f'Hello {usr}')
