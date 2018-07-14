while True:
    response = input ('Type in any number and see '
     'if it is divisible by seven! ')
    type (response)
    if int(response) % 7 == 0:
        print ('''
        It is divisible by 7!
        ''')
        break 
    else:
        print ('''
        it is not! 
        ''')
