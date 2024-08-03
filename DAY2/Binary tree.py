class Tree:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = '  ' * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, treeNode):
        self.children.append(treeNode)

node_1 = Tree('Drinks', [])
node_2 = Tree('Hot', [])
node_3 = Tree('Cold', [])
node_4 = Tree('Tea', [])
node_5 = Tree('Coffee', [])
node_6 = Tree('Pepsi', [])
node_7 = Tree('Thumbsup', [])
node_8 = Tree('Coke', [])

# Add children
node_1.addChild(node_2)
node_1.addChild(node_3)
node_2.addChild(node_4)
node_2.addChild(node_5)
node_3.addChild(node_6)
node_3.addChild(node_7)
node_3.addChild(node_8)

print(node_1)
