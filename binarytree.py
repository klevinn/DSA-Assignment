# from functions import open_pickles
# db = open_pickles()

class Node:
    def __init__(self, key, mode):
        self.left = None #Left subtree
        self.right = None #Right subtree
        a = lambda x: x.get_paxnum() if (mode == 1) \
                        else x.get_packcost()

        self.key = a(key) #Stored in Tree
        self.elements = [key]


# Insert a node
def insert(node, key, mode):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key, mode)

    if mode == 1:
        a = key.get_paxnum()
    else:
        a = key.get_packcost()

    # Traverse to the right place and insert the node
    if a == node.key:
        node.elements.append(key)
    elif a < node.key:
        node.left = insert(node.left, key, mode)
    else:
        node.right = insert(node.right, key, mode)

    return node


# Find the inorder successor
#the next smallest number 
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current

#Searching Algorithm
def search(root, val, mode):
    if mode == 1:
        val = val.get_paxnum()
    else:
        val = val.get_packcost()

    if root == None:
        return None
    elif root.key == val:
        return val
    elif val < root.key:
        return search(root.left, val, mode)
    elif val > root.key:
        return search(root.right, val, mode)


def BSTCreate(db, mode):
    for i in range(len(db)):
        if i == 0:
            tree = Node(db[i], mode)
        else:
            tree = insert(tree, db[i], mode)
    
    return tree



# def inorder(root):
#     if root is not None:
#         # Traverse left
#         inorder(root.left)

#         # Traverse root
#         print(str(root.key) + "->", end=' ')

#         # Traverse right
#         inorder(root.right)
