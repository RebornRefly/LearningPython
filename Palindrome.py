def IsPali(s):
    if s[0] == s[-1]:
        print('It is Palindrome.')
    else:
        print('Not.')


s = input('Enter chinese:')
IsPali(s)
