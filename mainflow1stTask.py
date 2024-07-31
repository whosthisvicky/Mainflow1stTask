# Creating and manipulating a list
print("List Operations:")

# Create a list
my_list = [1, 2, 3, 4, 5]
print(f"Original List: {my_list}")

# Adding elements
my_list.append(6)
my_list.insert(0, 0)
print(f"List after adding elements: {my_list}")

# Removing elements
my_list.remove(3)  # Remove first occurrence of 3
removed_element = my_list.pop()  # Remove and return the last element
print(f"List after removing elements: {my_list}")
print(f"Removed element: {removed_element}")

# Modifying elements
my_list[2] = 10
print(f"List after modifying an element: {my_list}")

# Creating and manipulating a dictionary
print("\nDictionary Operations:")

# Create a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(f"Original Dictionary: {my_dict}")

# Adding elements
my_dict['occupation'] = 'Engineer'
print(f"Dictionary after adding an element: {my_dict}")

# Removing elements
del my_dict['age']
print(f"Dictionary after removing an element: {my_dict}")

# Modifying elements
my_dict['city'] = 'San Francisco'
print(f"Dictionary after modifying an element: {my_dict}")

# Creating and manipulating a set
print("\nSet Operations:")

# Create a set
my_set = {1, 2, 3, 4, 5}
print(f"Original Set: {my_set}")

# Adding elements
my_set.add(6)
my_set.add(3)  # Adding a duplicate element (set will ignore it)
print(f"Set after adding elements: {my_set}")

# Removing elements
my_set.remove(4)  # Will raise KeyError if the element is not found
# my_set.discard(7)  # Use discard to avoid KeyError if the element is not found
print(f"Set after removing an element: {my_set}")

# Modifying elements
# Sets do not support direct item assignment, so we will create a new set
my_set = {x * 2 for x in my_set}  # Example modification: doubling each element
print(f"Set after modifying elements: {my_set}")

