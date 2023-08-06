# Create an empty list for Football Management System
print("\n")
player = []

# Using append() to add elements to the list
player.append({"player_id": "10", "player_name":"Symen",})

# Using insert() to add elements at specific positions in the list
player.insert(1, {"player_id": "10", "player_name": "Symen",})

# Using extend() to add iterable elements to the list
additional_players = [
{"player_id": "7", "player_name": "Sandy",},
{"player_id": "1", "player_name": "Babu",}
]
player.extend(additional_players)
print(player,"\n")

# Create a list with numeric elements
numeric_list = [1, 4, 2, 5, 3]
print("Original list:",numeric_list)

# Write a program to swap the first and last elements in a list.
numeric_list[0], numeric_list[-1] = numeric_list[-1], numeric_list[0]
print("Swapped list:", numeric_list)

# Write a program to find the sum of the digits in a list.
sum_of_digits = sum(numeric_list)
print("\n Sum of digits in the list:", sum_of_digits)

# Write a program to find the smallest element in a list.
smallest_element = min(numeric_list)
print("\n Smallest element in the list:", smallest_element)


# Create a dictionary with numeric values
numeric_dict = {
"a": 10,
"b": 20,
"c": 30,
"d": 45,
"e": 50
}

# Find the sum of all the values in the dictionary
sum_of_values = sum(numeric_dict.values())
print("\n Sum of values in the dictionary:", sum_of_values)

# Sort the dictionary in ascending order based on keys
sorted_dict = dict(sorted(numeric_dict.items()))
print("\n Sorted dictionary (ascending order based on keys):", sorted_dict)

# Sort the dictionary in descending order of values using a lambda function
sorted_dict_desc = dict(sorted(numeric_dict.items(), key=lambda item: item[1], 
reverse=True))
print("\n Sorted dictionary (descending order based on values):", 
sorted_dict_desc)
print("\n")