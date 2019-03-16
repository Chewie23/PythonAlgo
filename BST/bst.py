"""
BST implementation in Python makes literally no sense

Since it's taking higher level data structures to make higher level data
structures. But if it's for practice, eff it.
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.balance_factor = 0

    #One thing I want to do is to streamline this so I don't do the return a
    #copy
    #And I know, recursion won't scale, but it so nice to have
    def _add_node(self, cur_node, node):
        if cur_node == None:
            return node
        elif node.val > cur_node.val:
            cur_node.right = self._add_node(cur_node.right, node)
        elif node.val <  cur_node.val:
            cur_node.left = self._add_node(cur_node.left, node)
        else:
            print("Node {} exists already".format(node.val))
        return cur_node

    #This is the "public" function that the user would use to add, covering up
    #the awkward implementation
    def add(self, node):
        self.root = self._add_node(self.root, node)

    def balance(self):
        """
        Balance is achieved when two subtrees are +1, 0, or -1 in terms of
        height. All we care about here is a balance factor:
        balance_factor = height(left) - height(right)
        
        With that in mind, how would I do this?
        """
        print("No idea")


if __name__ == "__main__":
    b = BST()
    node_list = [Node(3), Node(4), Node(2), Node(4)]

    for node in node_list:
        b.add(node)

    print(b.root.right.val)


