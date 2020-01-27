user_in = int(input('Please enter an integer:'))
print('The number is:{0}\n'.format(user_in))
judge = user_in % 10 % 2
if judge == 0:
    print('Even.\n')
else:
    print('Odd.\n')
