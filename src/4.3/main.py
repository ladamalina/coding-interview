from __future__ import annotations
import logging
from typing import List, Optional


logging.basicConfig(level=logging.DEBUG)


class TreeNode:
    def __init__(self, value: int, left: TreeNode = None, right: TreeNode = None):
        self.value = value
        self.left = left  # type: Optional[TreeNode]
        self.right = right  # type: Optional[TreeNode]

    def __repr__(self):
        return '<{cls} value={v} left={left}, right={right}>'\
            .format(cls=self.__class__.__name__, v=self.value,
                    left=self.left.value if self.left is not None else self.left,
                    right=self.right.value if self.right is not None else self.right)

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right


class ListNode:
    def __init__(self, value: int, link_next: ListNode = None):
        self.value = value
        self.link_next = link_next  # type: Optional[ListNode]

    def __repr__(self):
        return '<{cls} value={v} next={next}>'\
            .format(cls=self.__class__.__name__, v=self.value, next=self.link_next)

    def __eq__(self, other):
        return self.value == other.value and self.link_next == other.link_next


depths = {}


def link_node_on_level(tree_node: Optional[TreeNode], level: int):
    if not tree_node:
        return
    link_node_on_level(tree_node.left, level + 1)

    new_node = ListNode(tree_node.value)
    if level in depths:
        depths[level]['tail'].link_next = new_node
        depths[level]['tail'] = new_node
    else:
        depths[level] = {'head': new_node, 'tail': new_node}

    link_node_on_level(tree_node.right, level + 1)


def tree_to_linked_list(tree_node: TreeNode) -> Optional[List[ListNode]]:
    if not tree_node:
        return []

    global depths
    depths = {}
    link_node_on_level(tree_node, 0)

    max_level = max(depths.keys())
    linked_lists = [depths[level]['head'] for level in range(0, max_level+1)]
    logging.debug('linked_lists: {}'.format(linked_lists))

    return linked_lists


if __name__ == "__main__":
    input_vars = [
        [
            TreeNode(2, left=TreeNode(1, left=TreeNode(0)), right=TreeNode(4, left=TreeNode(3))),
            [ListNode(2), ListNode(1, ListNode(4)), ListNode(0, ListNode(3))]
        ],
        [
            TreeNode(1, left=TreeNode(0), right=TreeNode(2)),
            [ListNode(1), ListNode(0, ListNode(2))]
        ],
        [
            TreeNode(3, left=TreeNode(1, left=TreeNode(0), right=TreeNode(2)),
                     right=TreeNode(5, left=TreeNode(4), right=TreeNode(6))),
            [ListNode(3), ListNode(1, ListNode(5)), ListNode(0, ListNode(2, ListNode(4, ListNode(6))))]
        ],
    ]

    for input_var in input_vars:
        print('input_var: {}'.format(input_var))
        assert tree_to_linked_list(input_var[0]) == input_var[1]
