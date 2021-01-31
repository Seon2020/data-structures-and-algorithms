class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class BinaryTree:
  def __init__(self, root=None):
    self.root = root
  
  def pre_order(self) -> list:
    result = []
    def traverse(root):
      result.append(root.value)
      if root.left:
        traverse(root.left)
      if root.right:
        traverse(root.right)
    traverse(self.root)
    return result

  def in_order(self) -> list:
    result = []
    def traverse(root):
      if root.left:
        traverse(root.left)
      result.append(root.value)
      if root.right:
        traverse(root.right)
    traverse(self.root)
    return result

  def post_order(self) -> list: 
    result = []
    def traverse(root):
      if root.left:
        traverse(root.left)
      if root.right:
        traverse(root.right)
      result.append(root.value)
    traverse(self.root)
    return result

class BinarySearchTree(BinaryTree):
  def add(self, value): 
    node = Node(value)
    current = self.root
    if not current:
      self.root = node
      return
    while current:
      if node.value < current.value:
        if not current.left:
          current.left = node
          break
        current = current.left
      else:
        if not current.right:
          current.right = node
          break
        current = current.right
        
  def contains(self, value): 
    current = self.root
    while current:
      if value == current.value:
        return True
      elif value < current.value:
        current = current.left
      elif value > current.value:
        current = current.right
    return False