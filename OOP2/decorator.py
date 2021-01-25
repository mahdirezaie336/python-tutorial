def decorator(validator):
    def checker(func):
        def ret(*x):
            if validator(*x):
                return func(*x)
            return 'error'

        return ret

    return checker


def validator(*x):
    cond = True
    for i in x:
        cond &= (i >= 0)
    return cond


@decorator(validator)
def f(*x):
    mult = 1
    for i in x:
        mult *= i
    return mult**0.5


print(f(4, 9))
print(f(-4))
