
dict1 = {}
n1 = int(input("Enter number of elements in first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

dict2 = {}
n2 = int(input("Enter number of elements in second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)


merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)


sorted_dict = dict(sorted(merged_dict.items()))
print("Sorted dictionary:", sorted_dict)



text = input("Enter a string: ")
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:", frequency)



set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

print("Set 1:", set1)
print("Set 2:", set2)

common_elements = set1.intersection(set2)
print("Common elements:", common_elements)