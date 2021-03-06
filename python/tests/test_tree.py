import pytest 
from code_challenges.tree.tree import Node, BinaryTree, BinarySearchTree

# Instantiate empty tree
def test_empty_tree():
  tree = BinaryTree()
  assert tree.root == None

# instantiate tree w/ single root node
def test_single_root_tree():
  root_node = 25
  tree = BinaryTree(root_node)
  assert tree.root == root_node

# add left child and right child to single root node
def test_left_right_child_tree():
  tree = BinaryTree()
  one = Node(25)
  two = Node(12)
  three = Node(30)
  tree.root = one
  one.left = two
  one.right = three
  assert one.left and one.right
  expected = two and three

  
# return collection from preorder traversal 
def test_bt_pre_order(test_tree):
  actual = test_tree.pre_order()
  expected = [1,2,4,5,3,6]
  assert actual == expected
  
# return collection from inorder traversal
def test_bt_in_order(test_tree):
  actual = test_tree.in_order()
  expected = [4,2,5,1,6,3]
  assert actual == expected

# return collection from postorder traversal 
def test_bt_post_order(test_tree):
  actual = test_tree.post_order()
  expected = [4,5,2,6,3,1]
  assert actual == expected

@pytest.fixture
def test_tree():
    tree = BinaryTree()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six

    return tree

# Binary Search Tree 
def test_success_add_node_to_bst(test_bst):
  test_bst.add(13)
  test_bst.add(23)
  assert test_bst.root.left.right.value == 13
  assert test_bst.root.right.left.left.value == 23

def test_success_bst_contains_value(test_bst):
  print()
  assert test_bst.contains(24) == True
  assert test_bst.contains(60) == False
  assert test_bst.contains(36) == True

@pytest.fixture
def test_bst():
  bst = BinarySearchTree()
  one = Node(15)
  two = Node(12)
  three = Node(25)
  four = Node(24)
  five = Node(29)
  six = Node(36)
  bst.root = one
  one.left = two
  one.right = three
  three.left = four
  three.right = five
  five.right = six
  return bst

# Find the Maximum Value in a Binary Tree
def test_find_maxval_bt(test_tree):
  expected = 6
  actual = test_tree.find_maximum_value()
  assert actual == expected

def test_find_maxval_onenode_bt():
  tree = BinaryTree(Node(-10))
  expected = -10
  actual = tree.find_maximum_value()
  assert actual == expected

# Breadth first code challenge
def test_breadth_first_even():
  tree = BinaryTree()
  a = Node('A')
  b = Node('B')
  c = Node('C')
  d = Node('D')
  e = Node('E')
  f = Node('F')

  tree.root = a 
  a.left = b
  a.right = c 
  b.left = d
  b.right = e
  c.left = f
  actual = tree.breadth_first()
  expected = ['A', 'B', 'C', 'D', 'E', 'F']
  assert actual == expected

def test_breadth_first_odd():
  tree = BinaryTree()
  a = Node('A')
  b = Node('B')
  c = Node('C')
  d = Node('D')
  e = Node('E')
  f = Node('F')
  g = Node('G')

  tree.root = a 
  a.left = b
  a.right = c 
  b.left = d
  b.right = e
  c.left = f
  c.right = g
  actual = tree.breadth_first()
  expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  assert actual == expected

def test_breadth_first_one_node():
  tree = BinaryTree()
  a = Node('A')
  tree.root = a 
  actual = tree.breadth_first()
  expected = ['A']
  assert actual == expected

