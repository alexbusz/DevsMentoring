# Zad 6.
# Wprowadź listę a = [3, 1, 5, 7, 9, 2, 6],
# wykonaj poniższe polecenia i zinterpretuj ich wyniki:
# a) a[3]
# b) a[1:4]
# c) a[3:]
# d) a[-3:]
# e) a[:3]
# f) a[3:-1]
# g) a[::2]
# h) a[5:2:-1]
# i) sum(a)
# j) 8 in a
# k) 4 not in a


a = [3, 1, 5, 7, 9, 2, 6]

# a) a[3]
wynik_a = a[3]
print("Wynik a):", wynik_a)
# Zwraca element o indeksie 3 w liście a. Wynik: 7


# b) a[1:4]
wynik_b = a[1:4]
print("Wynik b):", wynik_b)
# Zwraca podlistę od indeksu 1 do 4 (bez 4) w liście a. Wynik: [1, 5, 7]


# c) a[3:]
wynik_c = a[3:]
print("Wynik c):", wynik_c)
# Zwraca podlistę od indeksu 3 do końca listy a. Wynik: [7, 9, 2, 6]


# d) a[-3:]
wynik_d = a[-3:]
print("Wynik d):", wynik_d)
# Zwraca trzy ostatnie elementy listy a. Wynik: [9, 2, 6]


# e) a[:3]
wynik_e = a[:3]
print("Wynik e):", wynik_e)
# Zwraca podlistę od początku do indeksu 3 (bez 3) w liście a. Wynik: [3, 1, 5]


# f) a[3:-1]
wynik_f = a[3:-1]
print("Wynik f):", wynik_f)
# Zwraca podlistę od indeksu 3 do przedostatniego elementu w liście a. Wynik: [7, 9, 2]


# g) a[::2]
wynik_g = a[::2]
print("Wynik g):", wynik_g)
# Zwraca co drugi element listy a. Wynik: [3, 5, 9, 6]


# h) a[5:2:-1]
wynik_h = a[5:2:-1]
print("Wynik h):", wynik_h)
# Zwraca podlistę od indeksu 5 do 2 (włączając 5, ale bez 2)
# w kierunku malejącym. Wynik: [2, 9, 7]


# i) sum(a)
wynik_i = sum(a)
print("Wynik i):", wynik_i)
# Zwraca sumę wszystkich elementów listy a. Wynik: 33


# j) 8 in a
wynik_j = 8 in a
print("Wynik j):", wynik_j)
# Sprawdza, czy liczba 8 jest obecna w liście a. Wynik: False


# k) 4 not in a
wynik_k = 4 not in a
print("Wynik k):", wynik_k)
# Sprawdza, czy liczba 4 nie jest obecna w liście a. Wynik: True
