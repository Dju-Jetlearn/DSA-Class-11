class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def traversal(root):
    if root is not None:
        if root.left is not None:
            traversal(root.left)
        print(root.data)
        if root.right is not None:
            traversal(root.right)

def insert(root, ke):
    if root == None:
        return Node(ke)
    if ke < root.data:
        root.left = insert(root.left, ke)
    else:
        root.right = insert(root.right, ke)
    return root

def search(root, ki):
    if root.data == ki:
        return root
    elif ki < root.data and root.left is not None:
        return search(root.left, ki)
    elif ki > root.data and root.right is not None:
        return search(root.right, ki)
    else:
        return -1

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

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

user = input("Do you want to insert a number, search for one, or delete one? ")

if user == "Insert":
    userinput = int(input("What number do you want to insert? "))
    insert(root, userinput)
    traversal(root)
elif user == "Search":
    userinput = int(input("What number do you want to search for? "))
    a = search(root, userinput)
    if a == -1:
        print(userinput, "doesn't exist. Sorry.")
    else:
        print(userinput, "is in fact in our tree! Good job!")
elif user == "Delete":
    userinput = int(input("What number do you want to delete? "))
    a = delete(root, userinput)
    traversal(root)
else:
    print("That is not a valid choice, please choose the options available, and remember there are no spaces, and the first letter is capital.")