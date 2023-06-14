#Zdefinuj funkcję, która znajdzie i zwróci indeks największego elementu z przekazanej jako
# parametr listy

nums = [4, 6, 8, 24, 12, 2]

def find_largest_index(numbers):
    max_value = max(numbers)
    max_index = numbers.index(max_value)
    return max_index

nums = [4, 6, 8, 24, 12, 2]
largest_index = find_largest_index(nums)
print("Indeks największego elementu:", largest_index)
