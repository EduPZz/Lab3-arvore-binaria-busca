import json

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

    def getHeigth(self):    
        if self.left!=None:
            return 1 + self.left.getHeigth()
        if self.right!=None:
            return 1 + self.right.getHeigth()
        return 1
    
    def getMaxValueObj(self):
        if self.right!=None:
            return self.right.getMaxValueObj()
        return self
    
    def getMinValueObj(self):
        if self.left!=None:
            return self.left.getMinValueObj()
        return self
    

    def updateParentReference(self, parent, target=None):
        if parent.left == self:
            parent.left = target
        else:
            parent.right = target

    def removeValue(self, value, parent=None):

        if self.key==value:
            if self.left is None and self.right is None:
                self.updateParentReference(parent)
            elif self.left is None:
                self.updateParentReference(parent, self.right)
            elif self.right is None:
                self.updateParentReference(parent, self.left)
            else:
                if self.left.getHeigth() > self.right.getHeigth():
                    max_value = self.left.getMaxValueObj()
                    self.updateParentReference(parent, max_value)
                    max_value.right = self.right
                else:
                    min_value = self.right.getMinValueObj()
                    self.updateParentReference(parent, min_value)
                    min_value.left = self.left
        elif value>self.key and self.right!=None:
            self.right.removeValue(value, self)
        elif value<self.key and self.left!=None:
            self.left.removeValue(value, self)
        else:
            print("Não achei o valor para remover")

    def to_dict(self):
        d = {'key': self.key}

        if self.left is not None:
            d['left'] = self.left.to_dict()
        if self.right is not None:
            d['right'] = self.right.to_dict()

        return d


#criando um nó
raiz = BinaryTree(20)
raiz.insertNode(10)
raiz.insertNode(8)
raiz.insertNode(15)
raiz.insertNode(9)
raiz.insertNode(40)
raiz.insertNode(30)
raiz.insertNode(50)


print("Pre-Ordem")
raiz.preOrder()
print("Em Ordem")
raiz.inOrder()
print("Pos-Ordem")
raiz.posOrder()


json_string = json.dumps(raiz.to_dict(), indent=4)
print("######Árvore Original#####")
print(json_string)


raiz.getValuePath(50)
raiz.removeValue(40)

json_string = json.dumps(raiz.to_dict(), indent=4)
print("######Árvore Modificada######")
print(json_string)

