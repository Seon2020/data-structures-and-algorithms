class newNode:
    def __init__(self, value):
        self.value = value 
        self.child = []

class newTree: 
    def __init__(self, root=None):
        self.root = root
    
    def show_all_vals(self):
        all_values = []
        def check_values(node):
            all_values.append(node.value)
            if node.child:
                for child in node.child:
                    check_values(child)
        check_values(self.root)
        return all_values

    def fizzbuzz(self):
        def traverse(node):
            if node.child:
                for child in node.child:
                    if child.value % 15 == 0:
                        child.value = "FizzBuzz"
                    elif child.value % 5 == 0:
                        child.value = "Buzz"
                    elif child.value % 3 == 0:
                        child.value = "Fizz"
        traverse(self.root)
