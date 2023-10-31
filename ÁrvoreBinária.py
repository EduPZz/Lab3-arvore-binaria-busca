class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        
    def insertNode(self, value):
        if value < self.key and self.left == None:
            self.left = BinaryTree(value)
        elif value < self.key and self.left != None:
            self.left.insertNode(value)
        elif value >self.key and self.right == None:
            self.right = BinaryTree(value)
        elif value >self.key and self.right != None:
            self.right.insertNode(value)
            
    def preOrder(self):
        print(self.key)
        if self.left!=None:
            self.left.preOrder()
        if self.right!=None:
            self.right.preOrder()
            
    def inOrder(self):
        if self.left!=None:
            self.left.inOrder()
        print(self.key)
        if self.right!=None:
            self.right.inOrder()

    def posOrder(self):
        if self.left!=None:
            self.left.posOrder()
        if self.right!=None:
            self.right.posOrder()
        print(self.key)
        
    def searchValue(self, value):
        if self.key==value:
            print("Achei!!!")
        elif value>self.key and self.right!=None:
            self.right.searchValue(value)
        elif value<self.key and self.left!=None:
            self.left.searchValue(value)
    
    def getValuePath(self, value):
        print(self.key, end=' ')

        if self.key==value:
            print("")
            return
        
        elif value>self.key and self.right!=None:
            print('->', end=' ')
            self.right.getValuePath(value)
            
        elif value<self.key and self.left!=None:
            print('->', end=' ')
            self.left.getValuePath(value)
        
    
#criando um nó
raiz = BinaryTree(20)
raiz.insertNode(10)
raiz.insertNode(8)
raiz.insertNode(15)
raiz.insertNode(40)
raiz.insertNode(30)
raiz.insertNode(50)

#
print("Pre-Ordem")
raiz.preOrder()
print("Em Ordem")
raiz.inOrder()
print("Pos-Ordem")
raiz.posOrder()

raiz.getValuePath(50)
raiz.removeValue(50)
