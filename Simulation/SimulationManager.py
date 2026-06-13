from Simulation.SimulationTypes.OperatingPoint import OperatingPoint 
from Simulation.SimulationTypes.Transient import Transient 

class SimulationManager(): 
    def __init__(self,circuit): 
        self.directives = [] 
        self.circuit = circuit 

    def addDirective(self,directive,arguments): 

        if directive[0] == "op":
            self.directives.append(OperatingPoint(arguments,self.circuit))
        
        if directive[0] == "tran": 
            self.directives.append(Transient(arguments,self.circuit))

    def runDirectives(self): 
        for directive in self.directives: 
            self.runDirective(directive)
    
    def runDirective(directive): 
        directive.run() 
        


        
        

