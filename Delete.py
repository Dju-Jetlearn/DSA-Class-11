class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def InOrderTraversal(root):
    if root is not None:
        if root.left is not None:
            InOrderTraversal(root.left)
        print(root.data)
        if root.right is not None:
            InOrderTraversal(root.right)

def insert(root, ke):
    if root == None:
        return Node(ke)
    if ke < root.data:
        root.left = insert(root.left, ke)
    else:
        root.right = insert(root.right, ke)
    return root

def delete(root, ke):
    if root is None:
        return root
    if ke < root.data:
        root.left = delete(root.left, ke)
    elif ke > root.data:
        root.right = delete(root.right, ke)
    else:
        #Case 1, Node has no child - directly delete the node
        if root. left is None and root.right is None:
            return None #to indicate that this node should be removed
        
        #Case 2, Node with one child - delete the node and replace it with its child

        #left side
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        #right side

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        #Case 3, Node with two children - find min of right side and delete the node and replace with min child, or find max of left, and replace node with max child
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

user = int(input("How many noms do you want in the tree? "))
root = None

for i in range(user):
    n = int(input("What nom should be here? "))
    root = insert(root, n)

print("BST before deletion")
InOrderTraversal(root)

userinput = int(input("What nom do you want to delete? "))

a = delete(root, userinput)

print("BST after deletion")
InOrderTraversal(root)