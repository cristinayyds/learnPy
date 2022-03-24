numbers = [1, 2, 3, 5, 65, 75]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(odd)
print(even)
print(numbers)





