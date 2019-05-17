x = int(input())
# assert x > 0, "Positive" <- NO!


def gcd(a, b):
    assert type(a) == int and type(b) == int
    assert a > 0 and b > 0
    while b != 0:
        r = a % b
        b = a
        a = r
    return a
