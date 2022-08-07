names_list = []
names_list.append("wojtaszek")
names_list.append("maciaszek")
names_list.append("adaś")
names_list.append("adaś")

print(names_list)

for name in names_list:
    print(name)

names_list.reverse()

for name in names_list:
    print(name)


names_list.sort()
for name in names_list:
    print(name)

names_list.sort(reverse=True)
for name in names_list:
    print(name)

print("-----------------------------")
print(names_list[0])

print(names_list.count("adaś"))
print(len(names_list))
print(names_list.pop(1))
names_list.remove("wojtaszek")
print(names_list)

names_list.clear()
print(names_list)

print("KROTKA")  #struktura niezmienna

krotka_list = ("Woj", "22", "huehue")

print(len(krotka_list))
print(krotka_list.count("22"))

print("SET stons wyszli")  #set, nie ma duplikacji danych, elementy setu sa niemutowalne i nieuporządkowane
                          # do set nie da sie dodać listy, ale da sie dodać tuple

set_list = {"a", "b", "a"}

set1 = set()
set1.add("Bartek")
set1.add("Calineczka")
set1.add("usun to")
set1.add("usun to1")

set1.remove("usun to") # jeśli nie znajdzie takiego obiektu to zwraca błąd
set1.discard("usun to1") # a tu nie zwraca

print(set1)

set2 = {"xd"}
set3 = {"xddddd"}
set5 = set2.union(set3) #aby polaczyc dwa set uzywamy union, union zwraca nam nowy set
print(set5)
set3.update(set2) # update dodaje set do setu
print(set3)

print("usuwanie roznic w setach")
name_set1 = {"Arek", "Bartek", "Zbyszek"}
name_set2 = {"Bartek"}

name_set3 = name_set1.difference(name_set2) # z set1 usunieto obiekty znajdujace sie w set2

for name in name_set3:
    print(name)

print("szukanie czesci wspólnych")
name_set1 = {"Arek", "Bartek", "Zbyszek"}
name_set2 = {"Bartek"}

name_set3 = name_set1.intersection(name_set2) # intersection szuka czesci wpolnych

for name in name_set3:
    print(name)

print("wyswietla czesci rózne z obu zbiorów")
name_set1 = {"Arek", "Bartek", "Zbyszek"}
name_set2 = {"Bartek"}

name_set3 = name_set1.symmetric_difference(name_set2) #symmetric_difference

for name in name_set3:
    print(name)

name_set2.clear() # czysci set

print("dodawanie set dfo listy")
list_of_names = ["imie z listy"]

list_of_names.extend(name_set1) #extend rozszerza liste o elementy z listy
print(list_of_names)

print("SŁOWNIK")

countries_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_capitals["Czechia"] = "Prague" # dodanie nowego elementu do słownika
print(countries_capitals)

for country in countries_capitals.keys():
    print(country)

for capital in countries_capitals.values():
    print(capital)

for country, capital in countries_capitals.items():
    print(country + " - " + capital)

print("Pobieranie wartości klucza")
print(countries_capitals["Poland"]) # w przypadku braku wyrzuca błąd
print(countries_capitals.get("Poland")) #w przypadku braku zwraca None

print("Ustawia wartość domyślną jeśli nie ma danego klucza w słowniku, jeśli jest dany klucz to zwraca jego wartosc")
print(countries_capitals.setdefault("USA", "Washington DC"))
print(countries_capitals)

countries_capitals["Poland"] = "Bialystok"  #zamienia wartosc klucza
print(countries_capitals)

countries_capitals.pop("Poland") # usuwa klucz i jego wartosc z słownika
print(countries_capitals)

print(countries_capitals.popitem())  #usuwa ostatnio dodana wartosc do slownika

if "Poland" in countries_capitals:
    print("No jest")
else:
    print("nie znaleziono")