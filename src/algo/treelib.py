class treenode:
    def __init__(self, val = 0, left = 0, right = 0):
        self.__t = [str(self.__class__)]
        self.val = val
        self.left = left
        self.right = right
    def setfromlist(self, val:list):
        pass
    def getlist(self) -> list:
        l = []
        l.append(self.val)
        if str(type(self.left)) in self.__t:
            l.append(self.left.getlist())
        else:
            l.append(self.left)
        if str(type(self.right)) in self.__t:
            l.append(self.right.getlist())
        else:
            l.append(self.right)
        return(l)
    def getnode(self) -> str:
        l = self.getlist()
        return("")
    def __str__(self) -> str:
        return(self.getnode())
