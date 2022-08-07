user_choice = -1

tasks = []


def show_tasks():
    task_index = 0
    for task in tasks:
        print("[" + str(task_index) + "] " + task)
        task_index += 1


def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano nowe zadanie")


def delete_task():
    try:
        task_index = int(input("Podaj indeks zadania do usunięcia: "))
        tasks.pop(task_index)
        print("Usunięto zadanie o podanym indeksie")
    except IndexError:
        print("Zadanie o podanym indeksie nie istnieje!")


def save_tasks_to_file():
    file = open("lista_zadan.txt", "w")
    for task in tasks:
        file.write(task + "\n")

    file.close()
    print("Poprawnie zapisano zmiany to pliku")


def load_tasks_from_file():
    try:
        file = open("lista_zadan.txt", "r")
        for task in file.readlines():
            tasks.append(task.strip())

            file.close()
            print("Odczytano zadania z pliku")
    except FileNotFoundError:
        return


load_tasks_from_file()


while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    elif user_choice == 2:
        add_task()
    elif user_choice == 3:
        delete_task()
    elif user_choice == 4:
        save_tasks_to_file()

    print("-------------------")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")

    user_choice = int(input("Wybierz co chcesz zrobić: "))
