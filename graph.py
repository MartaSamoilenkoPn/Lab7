'''
Module
'''
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.
def get_graph_from_file(file_name):
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding="utf8") as file:
        graph_list = []
        str_read = file.read()
        row_list = str_read.split('\n')
        for row in row_list:
            local_list = row.split(',')
            local_list[0] = int(local_list[0])
            local_list[1] = int(local_list[1])
            graph_list.append(local_list)
        return graph_list
        