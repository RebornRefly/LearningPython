d1 = {'name': 'guess', 'age': 'inf', 'city': 'Heaven'}
print(d1)
d2 = dict(a=1, b=2, c=3)
print(d2)
print(d1['age'])
d1.setdefault('sex', 'male')
print(d1)
d2.update([('d', 4)])
print(d2)
d2.pop('d')
print(d2)
