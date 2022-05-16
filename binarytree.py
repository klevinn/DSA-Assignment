class Node:
    def __init__(self, key, mode):
        self.left = None #Left subtree
        self.right = None #Right subtree
        self.obj = key #Stored in Tree

        a = lambda x: x.get_name() if (mode == 1) \
                                else x.get_packname() if (mode == 2) \
                                                    else x.get_paxnum() if (mode == 3) \
                                                                    else x.get_packcost()
        
        self.key = a


# Insert a node
def insert(node, key, mode):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key, mode)

    a = lambda x: x.get_name() if (mode == 1) \
                            else x.get_packname() if (mode == 2) \
                                                else x.get_paxnum() if (mode == 3) \
                                                                else x.get_packcost()

    # Traverse to the right place and insert the node
    if a < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node