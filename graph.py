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


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [3, 2], 5: [1]}
    """
    dictionary = {}
    for element in edge_list:
        if element[0] in dictionary:
            local_list = dictionary.get(element[0])
            local_list.append(element[1])
            dictionary[element[0]] = local_list
        else:
            local_list = []
            local_list.append(element[1])
            dictionary[element[0]] = local_list

        if element[1] in dictionary:
            local_list = dictionary.get(element[1])
            local_list.append(element[0])
            dictionary[element[1]] = local_list
        else:
            local_list = []
            local_list.append(element[0])
            dictionary[element[1]] = local_list
    return dictionary

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph.keys():
        for value in graph[edge[0]]:
            if value == edge[1]:
                return True
    return False

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] in graph:
        value = graph[edge[0]]
        value.append(edge[1])
        graph[edge[0]] = value
    else:
        graph[edge[0]] = [edge[1]]
    if edge[1] in graph:
        value = graph[edge[1]]
        value.append(edge[0])
        graph[edge[1]] = value
    else:
        graph[edge[1]] = [edge[0]]
    return graph

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in graph.keys():
        value = graph[edge[0]]
        if edge[1] in value:
            value.pop(value.index(edge[1]))
        graph[edge[0]] = value
    if edge[1] in graph.keys():
        value = graph[edge[1]]
        if edge[0] in value:
            value.pop(value.index(edge[0]))
        graph[edge[1]] = value
    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph.keys():
        graph[node] = []
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph.keys():
        graph.pop(node)
        for key in graph.keys():
            if node in graph[key]:
                local_value = graph[key]
                local_value.pop(local_value.index(node))
                graph[key] = local_value
    return graph

def convert_to_dot(graph):
    """
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    """
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    print(get_graph_from_file('data1.txt'))