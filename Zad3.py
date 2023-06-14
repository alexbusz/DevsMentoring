#Napisz funkcję fizz_buzz, która przyjmuje argument liczbowy.
#Jeżeli liczba jest podzielna przez 3, funkcja powinna zwrócić “Fizz”.
#Jeżeli liczba jest podzielna przez 5, zwróć “Buzz”.
#Jeżeli liczba jest podzielna równocześnie przez 3 i 5, zwróć “FizzBuzz”.
#W przeciwnym razie, zwracaj przekazaną liczbę.

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"45
    else:
        return str(number)

number = int(input("Podaj liczbę: "))
result = fizz_buzz(number)
print(result)




