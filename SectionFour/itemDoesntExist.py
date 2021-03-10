shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]


item_to_find = "albatross"
found_at = None


# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# a easier way to write the code without a for loop
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} no found".format(item_to_find))
