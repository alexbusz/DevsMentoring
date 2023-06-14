#Napisz funkcję, która jako argument przyjmuje 10-cio elementową listę liczb całkowitych.
# Ma ona zwrócić przefilitrowaną listę elementów składającą się tylko z liczb dwucyfrowych
# wyselekecjonowanych z odebranej listy.

def filter_two_digit_numbers(numbers):
    result = []
    for num in numbers:
        if 10 <= num <= 99:
            result.append(num)
    return result

numbers = [55, 12, 7, 101, 42, 89, 77, 37, 25, 63]
filtered_numbers = filter_two_digit_numbers(numbers)
print(filtered_numbers)
