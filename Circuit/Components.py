from Utils import parseUnits

class Component(): 
    def __init__(self,name,nodes,str_value): 
        self.name = name 
        self.nodes = nodes 
        self.str_value = str_value
        self.num_value = parseUnits(str_value)
    
    def __repr__(self): 
        node_str = " ".join(self.nodes)
        return f"{self.name} {node_str} {self.str_value}"


class Resistor(Component): 
    pass 

class Capacitor(Component): 
    pass 

class Inductor(Component): 
    pass 

class VoltageSource(Component): 
    pass 
