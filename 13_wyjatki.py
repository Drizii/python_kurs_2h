country_capitals = {"Polska": "Warszawa", "Niemcy": "Berlin", "Słowacja": "Bratysława"}

try:
    print(2 / 0)
    print(country_capitals["USA"])
except KeyError:
    print("Klucz jest nieprawidłowy")
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
finally:  # tym zamykamy, pliki, zasoby i inne takie
    print("To wyświtli sie zawsze")

print("Jestem tu")
