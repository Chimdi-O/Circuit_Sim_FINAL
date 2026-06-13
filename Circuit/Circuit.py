
class Circuit(): 
    def __init__(self):
        self.components = [] 

    def addComponent(self,comp): 
        self.components.append(comp)

    def __repr__(self): 
        netlist = []
        for component in self.components: 
            netlist.append(repr(component))
        
        return "\n".join(netlist)