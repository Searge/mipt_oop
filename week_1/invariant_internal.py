x = int(input('Enter a number: '))

if x % 3 == 0:
    print("Число делится на три.")
elif x % 3 == 1:
    print("При делении на три остаток - один.")
else:
    assert x % 4 == 2
    # assert здесь является комментарием, гарантирующим истинность утверждения
    print("Остаток при делении на три - два.")


 x = int(input())
 assert x > 0, "Positive"

def gcd(a, b):
    assert type(a) == int and type(b) == int
    assert a > 0 and b > 0
    while b != 0:
        r = a % b
        b = a
        a = r
    return a
