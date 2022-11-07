"""
Module
"""
def common_names(female_names, male_names):
    """
    Function finds and returns common names of fameles and males.
    (List, List) -> Set
    >>> common_names(['Onnie', 'Vinnie'],['Onnie','Vinnie'])
    {'Onnie'}
    >>> common_names([],[])
    set()
    """
    letters = ["A", "E", "I", "O", "U", "Y"]
    result_list = set()
    for female_name in female_names:
        if female_name in male_names and female_name != '':
            if female_name[0] in letters:
                result_list.add(female_name)
    return result_list

def names_read(file_name):
    """
    Function reads file and returns list of names.
    """
    with open(file_name, 'r', encoding="utf8") as file:
        str_names = file.read()

        str_list = str_names.split('\n')
        str_list.pop(len(str_list)-1)
        return str_list

if __name__ == "__main__":
    print(common_names([], []))
    print(len(common_names(names_read('female.txt'), names_read('male.txt'))))
    print('male len = ', len(names_read('male.txt')))
    import doctest
    print(doctest.testmod())
