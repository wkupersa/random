class Node:
    def __init__(self , *args):
        if len(args) > 1:
            raise  Exception("Node excepts one argument for value") 

        self.value = None
        if len(args)==1:
            self.value = args[0]
        self.left = None
        self.right = None


class BST:
    '''
    creates a tree of something sortable
    '''
    def __init__(self):
        self.base_ptr = None

    def insert(self, value):
        if self.base_ptr == None:
            pointer = self.base_ptr
            self.base_ptr = self.sub_insert(pointer,value)
        elif value < self.base_ptr.value:
            self.base_ptr.left = self.sub_insert(self.base_ptr.left,value)
            pass
        else:
            self.base_ptr.right = self.sub_insert(self.base_ptr.right,value)
            pass
    def sub_insert(self, pointer, value):
        if pointer == None:
            pointer = Node(value)
            
        elif value < pointer.value:
            pointer.left = self.sub_insert(pointer.left, value)
            
            pass
        else:
            pointer.right =  self.sub_insert(pointer.right, value)
            pass
        return pointer




    def recursive_print(self, *args):
        '''
        Recurse through the tree, if the node has a left pointer,
        call the function with it. 
        Else, print value 
        If it has a right pointer, call function in it.
        '''
        if len(args) == 0:
            pointer = self.base_ptr
        else:
            pointer = args[0]
        if pointer.left:
            self.recursive_print(pointer.left)
        print(pointer.value)
        if pointer.right:
            self.recursive_print(pointer.right)




import random
test = BST()
for i in range(1,20):
    test.insert(random.randint(1,1000))
test.recursive_print()


pass



