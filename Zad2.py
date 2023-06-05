# Zad 2.
# Napisz program pobierający od użytkownika liczbę n i wyświetlający wartość
# sumy 1 + 2 + 3 + … + n.
# # Podpowiedź: Aby obliczyć sumę, należy przeprowadzić instrukcje:
# suma += wartosc

n = int(input("Podaj liczbę n: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print("Suma liczb od 1 do", n, "wynosi:", suma)  # NO OK
print(f"Suma liczb od 1 do {n} wynosi: {suma}")  # OK
