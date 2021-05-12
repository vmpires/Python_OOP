class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def get_evens(root):
    if root.data:
        if root.data % 2 == 0:
            print(root.data)
        if root.next:
            get_evens(root.next)
    else:
        print("Lista encadeada vazia")

def get_evens_two(root):
    if root.data:
        while root.data:
            if root.data % 2 == 0:
                print(root.data)
            root = root.next
            if root.next==None:
                return
    else:
        print("Lista vazia!")

segundo = Node(4)
terceiro = Node(6)
quarto = Node(7)
quinto = Node(9)
root = Node(2)
root.next = segundo
segundo.next = terceiro
terceiro.next = quarto
quarto.next = quinto
#get_evens(root)
get_evens_two(root)