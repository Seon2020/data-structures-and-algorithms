from code_challenges.fizz_buzz_tree.fizz_buzz_tree import newNode, newTree

def test_fizzbuzz():
    tree = newTree()
    tree.root = newNode(1)
    nodes = []
    for i in range(2, 50):
        nodes.append(newNode(i))
    for node in nodes:
        tree.root.child.append(node)
    tree.fizzbuzz()
    assert tree.show_all_vals() == ["FizzBuzz" if i%15 ==0  else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in range(1,50)]