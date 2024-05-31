#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    if ordered_list:
        ordered_list.append(ordered_list[-1] + 1)
    else:
        ordered_list.append(1)  # If the list is empty, start with 1

def remove_items_from_list(ordered_list, items_to_remove):
    ordered_list[:] = [item for item in ordered_list if item not in items_to_remove]

if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
