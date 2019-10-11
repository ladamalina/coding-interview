from __future__ import annotations
import logging
from typing import Optional


logging.basicConfig(level=logging.DEBUG)


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None):
        self.value = value
        self.left = left  # type: Optional[Node]
        self.right = right  # type: Optional[Node]

    def __repr__(self):
        return '<{cls} value={v} left={left}, right={right}>'\
            .format(cls=self.__class__.__name__, v=self.value,
                    left=self.left.value if self.left is not None else self.left,
                    right=self.right.value if self.right is not None else self.right)

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right


def list_to_tree(l: list) -> Optional[Node]:
    if not l:
        return None

    list_len = len(l)
    mid_index = list_len // 2
    logging.debug('list_len={}, mid_index={}'.format(list_len, mid_index))

    n = Node(l[mid_index])
    n.left = list_to_tree(l[:mid_index])
    n.right = list_to_tree(l[mid_index+1:])

    logging.debug('n={}'.format(n))

    return n


if __name__ == "__main__":
    input_vars = [
        [
            [0, 1, 2, 3, 4], Node(2, left=Node(1, left=Node(0)), right=Node(4, left=Node(3)))
        ],
        [
            [0, 1, 2], Node(1, left=Node(0), right=Node(2))
        ],
        [
            [0, 1, 2, 3, 4, 5, 6], Node(3, left=Node(1, left=Node(0), right=Node(2)),
                                        right=Node(5, left=Node(4), right=Node(6)))
        ],
    ]

    for input_var in input_vars:
        print('input_var: {}'.format(input_var))
        assert list_to_tree(input_var[0]) == input_var[1]
