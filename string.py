text = input("Enter a string: ")

old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

replaced = text.replace(old_char, new_char)
print("After replacement:", replaced)

reversed_string = text[::-1]
print("Reversed string:", reversed_string)

if text == reversed_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

char = input("Enter a character to find its frequency: ")
print("Character Frequency:", text.count(char))

words = text.split()
print("Number of words:", len(words))