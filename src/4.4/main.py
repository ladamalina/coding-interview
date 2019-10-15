from __future__ import annotations
import logging
from typing import Optional


logging.basicConfig(level=logging.DEBUG)


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None):
        self.value = value
        self.left = left  # type: Optional[Node]
        self.right = right  # type: Optional[Node]
        self.height = None

    def __repr__(self):
        return '<{cls} value={v} left={left}, right={right}>'\
            .format(cls=self.__class__.__name__, v=self.value,
                    left=self.left.value if self.left is not None else self.left,
                    right=self.right.value if self.right is not None else self.right)

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right


def is_balanced(node: Node) -> bool:
    if node is None:
        return True

    left_height = get_height(node.left)
    right_height = get_height(node.right)
    max_branch_height = max(left_height, right_height)
    if max_branch_height == 1:
        return True

    return (left_height == right_height) and is_balanced(node.left) and is_balanced(node.right)


def get_height(node: Optional[Node]) -> int:
    if node is None:
        return 0

    if node.height is not None:
        return node.height

    node.height = max(get_height(node.left), get_height(node.right)) + 1

    return node.height


if __name__ == "__main__":
    input_vars = [
        [
            Node(2, left=Node(1, left=Node(0)), right=Node(4, left=Node(3))), True
        ],
        [
            Node(1, left=Node(0), right=Node(2)), True
        ],
        [
            Node(1, left=Node(0), right=Node(2, right=Node(3, right=Node(4)))), False
        ],
        [
            Node(3, left=Node(1, left=Node(0), right=Node(2)), right=Node(5, left=Node(4), right=Node(6))), True
        ],
    ]

    for input_var in input_vars:
        print('input_var: {}'.format(input_var))
        assert is_balanced(input_var[0]) == input_var[1]
