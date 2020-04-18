# Programming Languages Lab (CMP321L)
# Lab 9 Exercise 1
class Node:
    def __init__(self, data, left = None, right = None):
        self.data, self.left, self.right = data, left, right
    def __str__(self):
        return self.data
    
class ParseTree:
    def __init__(self, root = None):
        self.root = root # root node
    
    # Create Parse Tree from PostFix notation
    def fromPostfix(self, expression=""):
        temp = []
        variables = 0
        for i in range(len(expression)):
            if expression[i] in [' ','(',')']:
                pass
            elif expression[i] == '-' and variables==1:
                node = temp.pop()
                temp.append(Node(expression[i],node))
                variables=0
            elif expression[i] == '#':
                node = temp.pop()
                temp.append(Node(expression[i],node))
                variables=0
            elif expression[i] in ['%','/','*','+','-','^']:
                lnode = temp.pop()
                rnode = temp.pop()
                temp.append(Node(expression[i],lnode,rnode))
                variables=0
            else:
                temp.append(Node(expression[i]))
                variables+=1
        self.root = temp[0]
        self.reverse()
        return self
    
    # Mirror the tree
    def reverse(self, node='None'):
        if isinstance(node,type(None)):
            return
        if node=='None':
            node = self.root
        
        if not (isinstance(node.left,type(None)) and isinstance(node.right,type(None))):
            node.left,node.right = node.right,node.left
        self.reverse(node.left)
        self.reverse(node.right)
    
    # Create Parse Tree from InFix notation
    def fromInfix(self, expression=""):
        level = Node('None')
        parent = []
        self.root = level
        
        for i in range(len(expression)):
            if expression[i]==' ':
                pass
            elif expression[i] == '(':
                if isinstance(level.left, type(None)):
                    level.left = Node('None')
                    parent.append(level)
                    level = level.left
                else:
                    level.right = Node('None')
                    parent.append(level)
                    level = level.right
            
            elif expression[i] == ')':
                level = parent[-1]
                parent.pop()
                
            elif expression[i] in ['%','/','*','+','-', '#', '^']:
                level.data = expression[i]
            else:
                if isinstance(level.left, type(None)):
                    level.left = Node(expression[i])
                else:
                    level.right = Node(expression[i])
        return self
    
    # Create Parse Tree from PreFix notation
    def fromPrefix(self, expression=""):
        level = Node('None')
        parent = []
        self.root = level
        
        for i in range(len(expression)):
            if expression[i]==' ':
                pass
            elif expression[i] == '(':
                if isinstance(level.left, type(None)):
                    level.left = Node('None')
                    parent.append(level)
                    level = level.left
                else:
                    level.right = Node('None')
                    parent.append(level)
                    level = level.right
            
            elif expression[i] == ')':
                level = parent[-1]
                parent.pop()
                
            elif expression[i] in ['%','/','*','+','-', '#', '^']:
                level.data = expression[i]
            else:
                if isinstance(level.left, type(None)):
                    level.left = Node(expression[i])
                else:
                    level.right = Node(expression[i])
        return self
    
    # Helper function for __str__, would recursively generate the string
    def genString(self, node, depth=0):
        string = ""
        if isinstance(node,type(None)):
            return string
            
        string+=self.genString(node.left,depth+1)
        string+=(depth*"  |")+"-("+str(node.data)+")\n"
        string+=self.genString(node.right,depth+1)
        return string
    
    # Recursive function that returns infix notation from Parse tree
    def infix(self, node='None'):
        if isinstance(node,type(None)):
            return ''
        if node=='None':
            node = self.root
        
        string = ''
        string+=self.infix(node.left)
        string+=node.data
        string+=self.infix(node.right)
        return string
    
    def postfix(self, node='None'):
        if isinstance(node,type(None)):
            return ''
        if node=='None':
            node = self.root
        
        string = ''
        string+=self.postfix(node.left)
        string+=self.postfix(node.right)
        string+=node.data
        return string
    
    def prefix(self, node='None'):
        if isinstance(node,type(None)):
            return ''
        if node=='None':
            node = self.root
    
        string = ''
        string+=node.data
        string+=self.prefix(node.left)
        string+=self.prefix(node.right)
        return string
    
    def __str__(self):
        return self.genString(self.root)
    
    def __iter__(self):
        return iter(self.prefix())

print(ParseTree().fromInfix("(a+b)/2"))

print(list(ParseTree().fromPostfix("x y ^")))

print(ParseTree().fromInfix("(a+b)/2").postfix())

xs = 'x y ^'

print(ParseTree().fromInfix( ParseTree().fromPostfix( xs).infix()).postfix())
