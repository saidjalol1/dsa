"""

A Tree is non-lenear, hierarchical data structure connected by edges.
Unlike linear sturucture (arrays, stacks, linked-lists, queues) where data stored sequentially,
tress stores the data in parent-child relationships.     

Key Tree Terminology:
    1) Root - The topmost node of the tree which has no parent
    2) parent & child - The direct decendant of the node is its child ,its ancestor is its parent
    3) Leaf - The bottomost node of the tree which has no child 
    4) Depth / height - the length of the root to the node (depth), of from the node to its deepest leaf ( height )


Types of the Tree:
    1) Binary Tree - A tree where each node has at most two children
    2) Binary Search Tree - A binary tree where the left child is less than the parent 
        and the right child is greater than the parent

Time complexity of Binary Search Tree:
    1) Insert / Set - takes O(log n) time at worst case it can be O(n) if the tree is skewed
    2) Delete - takes O(log n) time at worst case it can be O(n) if the tree is skewed
    3) Search / Lookup - takes O(log n) time at worst case it can be O(n) if the tree is skewed

"""



# Implementation of Binary Search Tree in Python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif val > current.val:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return 

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False