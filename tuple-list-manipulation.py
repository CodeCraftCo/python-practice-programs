#A Python program demonstrating conversion between tuples and lists to add elements and manipulate immutable tuples.
# Initial tuple
fruits_tuple = ("Apple", "Banana", "Cherry")

# Convert tuple to list
fruits_list = list(fruits_tuple)

# Add a fruit to the list
fruits_list.append("Date")

# Convert list back to tuple
fruits_tuple = tuple(fruits_list)

# Add 5 fruit names to the tuple
fruits_tuple += ("Elderberry", "Fig", "Grape", "Honeydew", "Indian Plum")

print(fruits_tuple)