#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_new_list = list(my_list)    
    if idx in range(len(my_new_list)):
        my_new_list[idx] = element
        return (my_new_list)
    else:
        return (my_list)
