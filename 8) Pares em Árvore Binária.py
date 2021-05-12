class Node: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
      
def get_evens(root):
    if root:
        if root.value % 2 == 0:
            print(root.value)
        if root.left:
            get_evens(root.left)
        if root.right:
            get_evens(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    get_evens(root)