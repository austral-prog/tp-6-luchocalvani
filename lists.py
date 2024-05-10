def remove_elements(list_to_remove_elements):
    cantidad = len(list_to_remove_elements)
    if cantidad >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif cantidad < 6 and cantidad >= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif cantidad < 5 and cantidad > 0:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif cantidad == 0:
        return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0, "Pink")
    return list_to_add_elements


def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    len_1 = len(list_to_compare1)
    len_2 = len(list_to_compare2)
    if len_1 >= 3 and len_2 >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else: 
        return False


def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0]) >= 2:
        list_1 = list_of_lists_to_modify[0][:2]
    else:
        list_1 = list_of_lists_to_modify[0][:]
    if len(list_of_lists_to_modify[1]) >= 4:
        list_2 = list_of_lists_to_modify[1][1: 4]
    else:
        list_2 = list_of_lists_to_modify[1][1:]
    if len(list_of_lists_to_modify[2]) >= 2:
        list_3 = list_of_lists_to_modify[2][-2:]
    else:
        list_3 = list_of_lists_to_modify[2][:]
    list_of_lists_to_modify[0] = list_1
    list_of_lists_to_modify[1] = list_2
    list_of_lists_to_modify[2] = list_3
    return list_of_lists_to_modify
