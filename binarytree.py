# from functions import open_pickles
# db = open_pickles()

class Node:
    def __init__(self, key, mode, index):
        self.left = None #Left subtree
        self.right = None #Right subtree
        a = lambda x: x.get_name().upper() if (mode == 1) \
                                else x.get_packname().upper() if (mode == 2) \
                                                    else x.get_paxnum() if (mode == 3) \
                                                                    else x.get_packcost()

        self.key = a(key) #Stored in Tree
        self.elements = {index:key}


# Insert a node
def insert(node, key, mode, index):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key, mode, index)

    if mode == 1:
        a = key.get_name().upper()
    elif mode == 2:
        a = key.get_packname().upper()
    elif mode == 3:
        a = key.get_paxnum()
    else:
        a = key.get_packcost()

    # Traverse to the right place and insert the node
    if a == node.key:
        node.elements[index] = key
    elif a < node.key:
        node.left = insert(node.left, key, mode, index)
    else:
        node.right = insert(node.right, key, mode, index)

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
def BSTsearch(root, val):
    # if mode == 1:
    #     val = val.get_paxnum()
    # else:
    #     val = val.get_packcost()

    if root == None:
        return {}
    elif root.key == val:
        return root.elements
    elif val < root.key:
        return BSTsearch(root.left, val)
    elif val > root.key:
        return BSTsearch(root.right, val)



def BSTCreate(db, mode):
    for i in range(len(db)):
        if i == 0:
            tree = Node(db[i], mode, i)
        else:
            tree = insert(tree, db[i], mode, i)
    
    return tree


# tree = BSTCreate(db, 1)

# def inorder(root):
#     if root is not None:
#         # Traverse left
#         inorder(root.left)

#         # Traverse root
#         print(str(root.key) + "->", end=' ')

#         # Traverse right
#         inorder(root.right)

# res = BSTsearch(tree, "Wei Ren")
# print(res)