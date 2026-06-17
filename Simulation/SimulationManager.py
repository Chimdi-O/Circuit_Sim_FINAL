from Simulation.SimulationTypes.OperatingPoint import OperatingPoint 
#from Simulation.SimulationTypes.Transient import Transient 

class SimulationManager(): 
    def __init__(self,circuit): 
        self.directives = [] 
        self.circuit = circuit 

    def addDirective(self,directive,arguments): 

        if directive == "op":
            self.directives.append(OperatingPoint(self.circuit))
            
        
        if directive[0] == "tran": 
            #self.directives.append(Transient(arguments,self.circuit))
            pass

    def runDirectives(self): 
        for directive in self.directives: 
            self.runDirective(directive)
    
    def runDirective(self,directive): 
        directive.run() 
        


        
        

