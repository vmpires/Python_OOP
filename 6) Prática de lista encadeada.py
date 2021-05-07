class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self._size = 0
		
	def __len__(self):
		return self._size
	
	def append(self, data):
		if self.head:
			pointer = self.head
			while(pointer.next):
				pointer = pointer.next
			pointer.next = Node(data)
			self._size += 1
		else:
		  	self.head = Node(data)
		  	self._size += 1
			  
	def index(self,data):
		pointer = self.head
		i = 0
		while (pointer):
			if pointer==data:
				return i
			pointer = pointer.next
			i += 1
			print(f"{data} not in list.")
			
	def __getitem__(self,index):
		pointer = self.head
		for i in range (index):
			if pointer!=None:
				pointer = pointer.next
			else:
				raise IndexError("list index out of range")
		if pointer!=None:
			return pointer.data
		else:
			raise IndexError("list index out of range")

	def __setitem__(self,index,elem):
		pointer = self.head
		for i in range (index):
			if pointer!=None:
				pointer = pointer.next
			else:
				raise IndexError("list index out of range")
		if pointer!=None:
			pointer.data = elem
		else:
			raise IndexError("list index out of range")
			
def sum_nodes(node):
	if node!=None:
		return node.data + sum_nodes(node.next)	  
	return 0


lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

for i in range(lista._size):
	print(f'Posição {i+1}: {lista[i]}')
print(f'Tamanho da lista: {len(lista)} itens')
print(f'A soma dos itens é: {sum_nodes(lista.head)}')