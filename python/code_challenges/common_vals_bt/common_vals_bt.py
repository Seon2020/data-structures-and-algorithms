from code_challenges.hashtable.hashtable import Hashtable
from code_challenges.tree.tree import Node, BinaryTree

def tree_intersection(tree1, tree2) -> list:
    common_vals = []
    if tree1.root and tree2.root:
        tree1_list, tree2_list = tree1.pre_order(), tree2.pre_order()
        hashy = Hashtable()
        for val in tree1_list: hashy.add(str(val), "number")
        for val in tree2_list: 
            if hashy.contains(str(val)): common_vals.append(int(val))
    return common_vals
