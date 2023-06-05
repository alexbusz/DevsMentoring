# Zad 5.
# Wprowadź krotkę d = (1, [2, 4], 'tekst', 3 + 5j) i:
# a) wyświetl jej ostatni element
# b) wyświetl jej pierwszy i drugi element
# c) sprawdź, czy tekst 'abc' jest elementem krotki

d = (1, [2, 4], 'tekst', 3 + 5j)

# a) Wyświetlanie ostatniego elementu
ostatni_element = d[-1]   # last_elem
print("Ostatni element krotki: ", ostatni_element)  # f-stringi !

# b) Wyświetlanie pierwszego i drugiego elementu
pierwszy_element = d[0]
drugi_element = d[1]
print("Pierwszy element krotki: ", pierwszy_element)
print("Drugi element krotki: ", drugi_element)

# c) Sprawdzanie, czy 'abc' jest elementem krotki
# is_elem =
print(f"Czy 'abc' jest elementem krotki? {'abc' in d}")
