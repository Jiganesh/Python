# Destructor

def div(a, b):
    print(a/b)


def smart_div(func):

    def inner(a, b):
        if b > a:
            a, b = b, a
        return func(a, b)

    return inner


div = smart_div(div)
div(5, 7)
