# Programming Languages Lab (CMP321L)
# Lab 9 Exercise 1
class Node:
    def __init__(self, data, left = None, right = None):
        self.data, self.left, self.right = data, left, right
    def __str__(self):
        return self.data
    
class ParseTree:
    def __init__(self, root = None):
        self.root = root
    def __str__(self):
        pass # to be implemented
    def fromPostfix(self, expression=""):
        level = Node('None')
        parent = []
        self.root = level
        
        for i in range(len(expression)):
            
            if expression[i] == '(':
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
                
                if level.left.data == 'None':
                    level.left = None
                if level.right.data == 'None':
                    level.right = None
                
                parent.pop()
                
            elif expression[i] in ['%','/','*','+','-']:
                level.data = expression[i]
            
            else:
                if isinstance(level.left, type(None)):
                    level.left = Node(expression[i])
                else:
                    level.right = Node(expression[i])
        
        return self.str()
    
    def str():
        return None
                            
            
node = ParseTree().fromPostfix('(AB*)(CD/)+')

