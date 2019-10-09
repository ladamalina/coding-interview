import queue


def does_path_exists(graph: dict, source_node: int, destination_node: int) -> bool:
    if source_node == destination_node:
        return True

    if source_node not in graph or destination_node not in graph:
        raise ValueError

    visited_nodes = {}
    q = queue.Queue()
    for next_node in graph.get(source_node):
        q.put(next_node)
    while not q.empty():
        current_node = q.get()
        if current_node == destination_node:
            return True
        if current_node in visited_nodes:
            continue
        for next_node in graph.get(current_node):
            q.put(next_node)
        visited_nodes[current_node] = True

    return False


if __name__ == "__main__":
    input_vars = [
        [
            {2: [], 3: [8, 10], 5: [11], 7: [8, 11], 8: [9], 9: [], 10: [], 11: [2, 9, 10]},
            7, 10, True
        ],
        [
            {2: [], 3: [8, 10], 5: [11], 7: [8, 11], 8: [9], 9: [], 10: [], 11: [2, 9, 10]},
            3, 10, True
        ],
        [
            {2: [], 3: [8, 10], 5: [11], 7: [8, 11], 8: [9], 9: [], 10: [], 11: [2, 9, 10]},
            3, 2, False
        ],
    ]

    for input_var in input_vars:
        print('input_var: {}'.format(input_var))
        assert does_path_exists(input_var[0], input_var[1], input_var[2]) == input_var[3]
