# Zachary Hoover || 8-15-23 || Python 1 Review: Lists

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("1. Introduction to Lists")

# Create and print list
item_list = [ 'table', 'desk', 'window', 'house', 'chair', 'chair', 'bench', 'computer', 'car', "window", "chair"]
print(f"  List of items: {item_list}")

input("\n Press Enter to Continue...")
print_header("2. Using append() to Add Elements")

# Add item to list, print new list
item_list.append("printer")
print(f"  '{item_list[-1]}' added to list.")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("3. Using insert() to Add Elements at a Specific Position")

# Inserts item into the list, prints the new list
item_list.insert(5, 'door')
print(f"  '{item_list[5]}' insterted at index 5")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("4. Using remove() to Delete an Element")

# Removes the second element in the list, prints the new list
print(f" Item at index 1 ('{item_list[1]}') was removed from the list")
item_list.remove(item_list[1])
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("5. Using pop() to Remove an Element by Index")

# use pop to remove first item in the list. Save popped item and print list and item
item = item_list.pop(0)
print(f"  Item at index 0 was popped ('{item}')")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("6. Slicing Lists")

# move elements from item_list to a new list, print both items, and both lists
new_items = []

# Pop items from old list
item1 = item_list.pop(1)
item2 = item_list.pop(1)

# Print removed items
print(f"  Items '{item1}'' and '{item2}' moved to new list. ")

# Add variables to new_items
new_items.append(item1)
new_items.append(item2)

# Print lists
print(f"\n  Old List: {item_list}")
print(f"\n  New List: {new_items}")

input("\n Press Enter to Continue...")
print_header("7. Modifying Elements")

# Get index of one of duplicate items
dup_index = item_list.index("chair")
item_list[dup_index] = "poster"

# Print message about change
print(f"  Changed item at index {dup_index} to '{item_list[dup_index]}'")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("8. Using while Loops with Lists")

# Remove all items called 'chair' from the list
while 'chair' in item_list:
    item_list.remove("chair")

# Print the changes and list
print("  All 'chair's have been removed from the list.")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("9. Using for Loops with Lists")

# Print all items in the list with index number
print("  Items in the list:")
for i in item_list:
    print(f"   {item_list.index(i)}. {i}")

input("\n Press Enter to Continue...")
print_header("10. Using if Statements with Lists")

# check for word, print result
if 'desk' in item_list:
    print(f"  'desk' was found at index {item_list.find('desk')}")
else:
    print("  This list does not contain word 'desk'")

input("\n Press Enter to Continue...")
print_header("11. Using sort() to Sort Lists")

# Sort the list, print the list
item_list.sort()

print("  The list has been sorted.")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
print_header("12. Using sorted() to View a Sorted List")

# use sorted to sort the list again (will have the same result)
sorted_list = sorted(item_list)

# Print the change and list
print("  The list has been sorted (uing sorted).")
print(f"  Sorted List: {sorted_list}")

input("\n Press Enter to Continue...")
print_header("13. Using extend() to Add Multiple Items")

# Create list to add, add list
add_list = ["photo", "mouse", "light", "blinds"]
item_list.extend(add_list)

# Print changed, and list
print(f"  List: {add_list} added to list.")
print(f"  List: {item_list}")

input("\n Press Enter to Continue...")
