import random


def laske_pi_likiarvo(pisteiden_maara):
    n = 0

    for _ in range(pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            n += 1

    pi_likiarvo = 4 * n / pisteiden_maara
    return pi_likiarvo


pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))

pi_likiarvo = laske_pi_likiarvo(pisteiden_maara)
print(f"Piin likiarvo on: {pi_likiarvo}")
