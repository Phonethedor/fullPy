class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
            runner = self.head#inicializa el runner (el que sigue) como el propio head
            while (runner != None):
                print(runner.value)
                runner = runner.next#invoca el metodo del nodo para que el proximo runner sea el .next del nodo
            return self
    def add_to_back(self, val):
        if self.head == None:	
            self.add_to_front(val)	
            return self	
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	
        return self  
    def insert_at(self,val,n):
        pass      
    def remove_from_front(self):
        runner = self.head
        self.head = runner.next
        return self
    def remove_from_back(self):
        if(self.head !=None and self.head.next!=None):
            runner = self.head
            while(runner.next.next != None):
                runner = runner.next
            runner.next = None
        elif(self.head.next == None):
            self.head.value=None
        return self
    def remove_val(self, val):
        runner = self.head
        if runner.value == val:
            self.head = runner.next
            return self
        while (runner.next.value != val):
            runner = runner.next
        temp = runner.next
        runner.next = temp.next
        return self
    def insert_at(self, val, n):
        runner = self.head
        if n==0:
            self.add_to_front(val)
        else:
            c = 1
            while c < n:
                runner = runner.next
                c += 1
            temp = runner.next
            nuevo = SLNode(val)
            runner.next = nuevo
            nuevo.next = temp
        return self

#falta add en cualquier posicion, eliminar front, back y cualquiera
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()