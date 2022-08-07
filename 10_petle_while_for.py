numer = 1

while numer < 6:
    print(numer)
    numer += 1

for number in range(1, 6):
    print(number)

for number in range(0, 20, 1): # ostatnia liczba wskazuje o jaki krok ma sie zwiekszac liczba
    if number == 15:
        break # przerywa
    elif number == 5:
        continue # przerywa aktualne wywolanie i przechodzi dalej
    print(number)