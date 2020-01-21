# Raw string
print(r'http://www.google.com/')

# About input (Don't forget to change the type and encode)
# enter_int = int(input("Enter an int:"))
# print('int:' + str(enter_int))
# enter_byte = bytes(input('Enter a byte:').encode('utf-8'))
# print('byte:' + str(enter_byte.decode('utf-8')))
# enter_string = input('Enter Strings:').encode('utf-8')
# print('String:'+enter_string.decode('utf-8'))

# search String
s = '345685213'
print(s[::2])
print(s[2:6:])
print(s[::-1])  # step < 0
print(s.index('521'))
print(s[5:8:])

# split, format and join
a = 'I LOVE PYTHON'
sp = a.split(' ')
print(sp)
print('-'.join(sp))
fmt_test = '{0:^8} and {1:>8}'.format('wow', 'awesome')
print(fmt_test)
