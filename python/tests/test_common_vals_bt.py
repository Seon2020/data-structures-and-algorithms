import pytest 
from code_challenges.tree.tree import Node, BinaryTree
from code_challenges.common_vals_bt.common_vals_bt import tree_intersection

def test_tree_intersection(test_tree_one, test_tree_two):
    actual = tree_intersection(test_tree_one, test_tree_two)
    expected = [100,160,125,175,200,350,500]
    assert actual == expected

def test_one_empty_tree(test_tree_one):
    tree = BinaryTree()
    actual = tree_intersection(test_tree_one, tree)
    expected = []
    assert actual == expected

def test_two_empty_trees():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected

@pytest.fixture
def test_tree_one():
    tree = BinaryTree()
    one = Node(150)
    two = Node(100)
    three = Node(250)
    four = Node(75)
    five = Node(160)
    six = Node(200)
    seven = Node(350)
    eight = Node(125)
    nine = Node(175)
    ten = Node(300)
    eleven = Node(500)

    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    five.left = eight
    five.right = nine
    seven.left = ten
    seven.right = eleven

    return tree

@pytest.fixture
def test_tree_two():
    tree = BinaryTree()
    one = Node(42)
    two = Node(100)
    three = Node(600)
    four = Node(15)
    five = Node(160)
    six = Node(200)
    seven = Node(350)
    eight = Node(125)
    nine = Node(175)
    ten = Node(4)
    eleven = Node(500)

    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    five.left = eight
    five.right = nine
    seven.left = ten
    seven.right = eleven

    return tree