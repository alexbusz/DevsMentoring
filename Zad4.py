# Zad 4.
# Napisz program wyświetlający nazwę dnia tygodnia zależnie od liczby wprowadzonej
# przez użytkownika (1 – poniedziałek ,…, 7 – niedziela, inna – „nie ma takiego dnia”)

day_num = int(input("Podaj numer dnia tygodnia: "))

if day_num == 1:
    print("Poniedziałek")
elif day_num == 2:
    print("Wtorek")
elif day_num == 3:
    print("Środa")
elif day_num == 4:
    print("Czwartek")
elif day_num == 5:
    print("Piątek")
elif day_num == 6:
    print("Sobota")
elif day_num == 7:
    print("Niedziela")
else:
    print("Nie ma takiego dnia")
