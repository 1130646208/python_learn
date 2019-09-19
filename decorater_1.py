from functools import wraps


def outer(fun):
    "outer doc"
    print("I am the outer function")
    @wraps(fun)
    def wraper():
        print("before wrap")

        fun()
        print("after wrap")
    return wraper


@outer
def inn():
    "inn doc"
    print("I am the inn function!")


inn()

print(inn.__doc__)
