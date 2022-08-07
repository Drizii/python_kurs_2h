file = open("c_and_c.txt", "w+") # r - plik do odczytu, w - plik do zapisu, w+ - plik do zapisu i odczytu

country_capitals = {"Polska": "Warszawa",
                    "Niemcy": "Berlin",
                    "Słowacja": "Bratysława"}

for country, capitals in country_capitals.items():
    file.write(country + " - " + capitals + "\n")

file.close()

###

file = open("c_and_c.txt")

# for line in file.read():
#     print(line, end="")

for line in file.readlines():
    print(line)

file.close()