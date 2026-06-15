
class Circuit(): 
    def __init__(self):
        self.components = [] 
        self.node_map = {} 
       
    def addComponent(self,comp): 
        self.components.append(comp) 

        for i in comp.nodes: 
            if i != "0" and i not in self.node_map: 
                if len(self.node_map) == 0: 
                    self.node_map[i] = 1 
                else: 
                    self.node_map[i] = len(self.node_map) 

    def __repr__(self): 
        netlist = [] 
        for component in self.components: 
            netlist.append(repr(component)) 
        
        return "\n".join(netlist) 