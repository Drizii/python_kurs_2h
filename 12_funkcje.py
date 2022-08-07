country_informations = {}
country_informations["Poland"] = ("Warszawa", 38.9)
country_informations["Germany"] = ("Berlin", 83)
country_informations["Slovatia"] = ("Bratysława", 5.5)


# for country in country_informations.keys():
#     print(country)
#
# country = input("Podaj kraj o jakim chcesz uzyskać informacje? ")
#
# country_informations = country_informations.get(country)
#
# print()
# print(country)
# print("___________________")
# print("Stolica " + country_informations[0])
# #print("Liczba mieszkańców (mln): " + country_informations[1]) # tak można jesli zrobimy z liczny str w slowniku poprzez ""
# print("Liczba mieszkańców (mln): " + str(country_informations[1]))
#
print("To można tez zapisać tak:")
country = input("Podaj kraj o jakim chcesz uzyskać informacje? ")

def show_country_information(country):
    c_informations = country_informations.get(country)

    print()
    print(country)
    print("___________________")
    print("Stolica " + c_informations[0])
    #print("Liczba mieszkańców (mln): " + country_informations[1]) # tak można jesli zrobimy z liczny str w slowniku poprzez ""
    print("Liczba mieszkańców (mln): " + str(c_informations[1]))


show_country_information(country)  # to jest wywoływanie funkcji

