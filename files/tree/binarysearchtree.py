# from functions import open_pickles
# db = open_pickles()

"""
Concept Of Binary Search Tree:
Elements Lesser than the root Node will be in the left subtree 
WHile elements greater than the root node will be in the right subtree

Lambda function to designate the key for VERY top node 
General Consesus that for mode : 1 = Name, 2 = Package Name, 3 = Number of Pax, 4 = Cost Per Pax
Uses upper for easier Comparisons Later on
"""
class Node:
    def __init__(self, key, mode, index):
        self.left = None #Left subtree
        self.right = None #Right subtree

        a = lambda x: x.get_name().upper() if (mode == 1) \
                                else x.get_packname().upper() if (mode == 2) \
                                                    else x.get_paxnum() if (mode == 3) \
                                                                    else x.get_packcost()

        #Identifier of the node
        self.key = a(key) 

        #Storing of elements in a Dictionary, JUST in case of duplicates
        #Index is used for later editting of the Data in ORIGINAL database
        self.elements = {index:key}

"""
Insert a node

Basically Create the Tree, if the node inputted is a None

If the element you want to insert is the same value as the identifier of the node
Store the value in the Dictionary in the node, while saving the index as the key

Due to concept of Binary Search Tree, if the Element is of a lesser value will traverse the right subtree of the node and vice versa
In the right/left subtree, recursion of the insert function is done again untll it returns the node
"""

def insert(node, key, mode, index):
    if (node is None):
        return Node(key, mode, index)

    if (mode == 1):
        a = key.get_name().upper()
    elif (mode == 2):
        a = key.get_packname().upper()
    elif (mode == 3):
        a = key.get_paxnum()
    else:
        a = key.get_packcost()

    if (a == node.key):
        node.elements[index] = key
    elif (a < node.key):
        node.left = insert(node.left, key, mode, index)
    else:
        node.right = insert(node.right, key, mode, index)

    return node

"""
Find the inorder successor
the next smallest number , greater than the node

Using the concept of BST, the node put into the function will be the right subtree of wthe root we want the inorder successor of.
Then we will check the left subtree to determine the smallest Number
"""
def minValueNode(node):
    current = node

    while(current.left is not None):
        current = current.left

    return current

"""
Searching ALgo

If result not found:
Return Empty dictionary because the way my searching Logic works uses a dictionary

If result found return the dictionary stored in the root

Same idea of using the BST concept, traverse the left subtree if lesser than the root and vice versa
"""
def BSTsearch(root, val):
    if (root == None):
        return {} 
    elif (root.key == val):
        return root.elements
    elif (val < root.key):
        return BSTsearch(root.left, val)
    elif (val > root.key):
        return BSTsearch(root.right, val)

#Tree creation
def BSTCreate(db, mode):
    for i in range(len(db)):
        #Highest Node
        if (i == 0):
            tree = Node(db[i], mode, i)
        else:
            tree = insert(tree, db[i], mode, i)
    
    return tree

"""
Tree Sort

Inorder traversal, #inverse inorder for descending
Uses Inorder traversal of the tree to get a sorted list 
Inorder is All elements of Left Subtree, root, then all elements of right subtree
"""
def treeSort(root, arr, inv):
    if (root is not None):
        # Traverse left
        if (inv == 1):
            treeSort(root.left, arr, inv)
        else:
            treeSort(root.right, arr, inv)

        for i in root.elements:
            arr.append(root.elements[i])

        # Traverse right
        if (inv == 1):
            treeSort(root.right, arr, inv)
        else:
            treeSort(root.left, arr, inv)
    
    return arr


#Test Code
# tree = BSTCreate(db, 3)
# print(inorder(tree, [], 2))