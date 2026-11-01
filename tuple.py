user_input = input("Enter comma-separated numbers: ")
number_list = [int(item.strip()) for item in user_input.split(",")]
number_tuple = tuple(number_list)

print("\n--- Generated Structures ---")
print("List:", number_list)
print("Tuple:", number_tuple)

print("\n--- Additional Information ---")
print(f"Total number of elements: {len(number_list)}")
print(f"First element: {number_list[0]}")
print(f"Last element: {number_list[-1]}")
print("List in reverse order:")
print(number_list[::-1])