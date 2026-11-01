numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original list:", numbers)

h = int(input("Enter a number to search: "))
if h in numbers:
    print("Number found")
else:
    print("Number not found")

index = int(input("Enter index to update: "))
value = int(input("Enter new value: "))
numbers[index] = value
print("After updating:", numbers)

value = int(input("Enter a number to add: "))
numbers.append(value)
print("After adding:", numbers)

value = int(input("Enter a number to remove: "))
if value in numbers:
    numbers.remove(value)
    print("After removing:", numbers)
else:
    print("Number not found")

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)