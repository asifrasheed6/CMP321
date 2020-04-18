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
            elif expression[i] in ['%','/','*','+','-']:
                lnode = temp.pop()
                rnode = temp.pop()
                temp.append(Node(expression[i],lnode,rnode))
                variables=0
            else:
                temp.append(Node(expression[i]))
                variables+=1
        self.root = temp[0]
        return self
        
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
                
            elif expression[i] in ['%','/','*','+','-', '#']:
                level.data = expression[i]
            else:
                if isinstance(level.left, type(None)):
                    level.left = Node(expression[i])
                else:
                    level.right = Node(expression[i])
        return self
    
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
                
            elif expression[i] in ['%','/','*','+','-', '#']:
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
    
    def __str__(self):
        return self.genString(self.root)
    
    def __iter__(self):
        pass
        
print(ParseTree().fromPostfix('b - b b * a c * 4 * - # + 2 a * /'))

