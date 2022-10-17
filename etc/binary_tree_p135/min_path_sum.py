class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"<Node: value={self.value}, left={self.left}, right={self.right}>"


def min_path_sum(root):
    """"DFS"""

    m = float("inf")
    stack = [(root, root.value)]

    while stack:
        node, curr_sum = stack.pop()

        if not node.left and not node.right:
            print(curr_sum)
            if m > curr_sum:
                m = curr_sum
            continue

        if node.left:
            stack.append((node.left, curr_sum + node.left.value))
        if node.right:
            stack.append((node.right, curr_sum + node.right.value))

    return m


def test_p135_1():
    node = Node(10)
    assert min_path_sum(node) == 10


def test_p135_2():
    node = Node(10, Node(5), Node(5))
    assert min_path_sum(node) == 15


def test_p135_3():
    node = Node(10, Node(5, None, Node(2)), Node(5))
    assert min_path_sum(node) == 15


def test_p135_4():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1)))
    assert min_path_sum(node) == 16


def test_p135_5():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
    assert min_path_sum(node) == 15
