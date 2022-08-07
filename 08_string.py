name = "wojtek"
print(len(name))
print(name.capitalize()) # metoda capitalize nie przyjmuje argumentów,
                         # powoduje ona zmienienie pierszej litery an duża
print(name.upper()) # wszystkie litery duze
print(name.lower()) # wszystkie litery male
print(name[0]) # wyśwpietla piersza litere wyrazu, liczenie od 0
print(name[0:2]) # 0 to indeks poczatkowy, a 2 to liczba liter jakie chcemy wyświetlic
print(name[4:]) # wyswitla od 6 litery do konca wyrazu
print(name[::-1] + " notototot") # liczenie od końca

channel = "Jak nauczyć się programować"
print(channel.split(" ")) # w "" znak rodzielenia stringa

#łączenie wyrazów
join_string = " " # definiowanie rodzaju łącznika w ""
print(join_string.join(["Jak", "żyć", "panie", "premierze"]))

print(name.startswith("w")) # sprawdza jaką literą zaczyna się wyraz (istotna wielkość litery)
print(name.startswith("W"))
print(name.endswith("k")) # sprawdza jaką literą kończy się wyraz (istotna wielkość litery)
print(name.endswith("K"))

print(name.rstrip("k")) #usuwa dana pierwsza litere na prawym koncu wyrazu
print(name.lstrip("w")) #usuwa dana pierwsza litere na lewym koncu wyrazu
print(name.strip("w")) #usuwa dana pierwsza litere na prawym i lewym koncu wyrazu
print(name.strip()) # usuwa nadmierne SPACJE

first_name = "Wojtek"
last_name = "Kowalewicz"

print(first_name + " " + last_name)
print(join_string.join([first_name, last_name]))

james_bond = 7
print(str(james_bond).zfill(3)) # zfill wypelnia zerami, w nawiasie podajemy długość frazy jaka ma powstac