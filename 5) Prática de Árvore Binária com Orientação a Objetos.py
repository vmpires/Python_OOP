class Node: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
      
          
def Sum_values(root): 
    if (root == None):
        return 0
    return (root.value + Sum_values(root.left) + 
                       Sum_values(root.right))

def Tree_height(root):
    if root is None:
        return 0
    else:
        return max(Tree_height(root.left), Tree_height(root.right)) + 1 


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    soma = Sum_values(root)
    altura = Tree_height(root)
    print("A soma de todos os nós é:", soma)
    print("A altura da árvore é: ", altura)