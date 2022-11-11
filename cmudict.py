'''
Module
'''
def dict_reader_tuple(file_dict):
    """
    (str) -> tuple
    """
    with open(file_dict, 'r', encoding="utf8") as file:
        row_list_start = file.read().split('\n')
        if row_list_start[len(row_list_start)-1] == '':
            row_list_start.pop(len(row_list_start)-1)
        row_result_list = []
        for row in row_list_start:
            row_as_list = row.split(' ')
            local_tuple = ()
            local_tuple += (row_as_list[0],)
            local_tuple += (int(row_as_list[1]),)
            local_list = []
            for i in range(2, len(row_as_list)):
                local_list.append(row_as_list[i])
            local_tuple += tuple([local_list])
            row_result_list.append(local_tuple)
        if len(row_result_list) > 1:
            return row_result_list
        return row_result_list[0]

def dict_reader_dict(file_dict):
    """
    (str) -> dict
    """
    with open(file_dict, 'r', encoding="utf8") as file:
        result_dict = {}
        row_list_start = file.read().split('\n')
        row_list_start.pop(len(row_list_start)-1)
        for row in row_list_start:
            row_as_list = row.split(' ')
            if row_as_list[0] not in result_dict:
                local_tuple = ()
                for i in range(2, len(row_as_list)):
                    local_tuple += (row_as_list[i],)
                local_set = set()
                local_set.add(local_tuple)
                result_dict[row_as_list[0]] = local_set
            else:
                value = result_dict[row_as_list[0]]
                local_tuple = ()
                for i in range(2, len(row_as_list)):
                    local_tuple += (row_as_list[i],)
                value.add(local_tuple)
                result_dict[row_as_list[0]] = value
        return result_dict

def dict_invert(dct):
    """
    (object) -> dict
    >>> dict_invert({'WATER':{('W', 'A', 'T', 'E', 'R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    """
    dict_result = {}
    if type(dct) == dict:
        for element in dct:
            if len(dct[element]) not in dict_result:
                local_value = set()
                for value in dct[element]:
                    local_tuple = ()
                    local_tuple += (element,)
                    local_tuple += (value,)
                # local_tuple += (local_tuple,)
                    local_value.add(local_tuple)
                dict_result[len(dct[element])] = local_value
            else:
                local_value = dict_result[len(dct[element])]
                for value in dct[element]:
                    local_tuple = ()
                    local_tuple += (element,)
                    local_tuple += (value,)
                # local_tuple += (local_tuple,)
                    local_value.add(local_tuple)
                dict_result[len(dct[element])] = local_value
        return dict_result
    elif type(dct) == list:
        local_dictionary = {}
        result_dictionary = {}
        for element in dct:
            if element[0] not in local_dictionary:
                local_dictionary[element[0]] = [1, tuple(element[2])]
            else:
                local_value = local_dictionary[element[0]]
                local_value.append(tuple(element[2]))
                local_value[0] += 1
                local_dictionary[element[0]] = local_value
        for element in local_dictionary:
            if local_dictionary[element][0] not in result_dictionary:
                local_set = set()
                for value in local_dictionary[element]:
                    local_tuple = ()
                    if type(value) != int :
                        local_tuple += (element, value)
                        local_set.add(local_tuple)
                result_dictionary[local_dictionary[element][0]] = local_set
            else:
                value_in_result_dict = result_dictionary[local_dictionary[element][0]]
                for value in local_dictionary[element]:
                    if type(value) != int :
                        local_tuple = (element, value)
                        value_in_result_dict.add(local_tuple)
                result_dictionary[local_dictionary[element][0]] = value_in_result_dict
        return result_dictionary

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    print(dict_reader_tuple("cmudict.txt"))