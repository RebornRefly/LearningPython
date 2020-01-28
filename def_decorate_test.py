def body_decorate(func):
    def clothes(name):
        return '<clothes>{0}<clothes>'.format(name)

    return clothes


@body_decorate
def body(name):
    return '{0}'.format(name)


print(body('Tom'))
