from Circuit.Circuit import Circuit
from Circuit.Components import Resistor, Inductor, Capacitor, VoltageSource
from Simulation.SimulationManager import SimulationManager


class Interpreter(): 

    def __init__(self): 
        
        self.circuit = Circuit()
        self.simulation_manager = SimulationManager(self.circuit) 

    def parseFile(self,filepath): 
        with open(filepath) as f: 
            for line in f: 
                self.parseLine(line)


    def parseString(self,lines): 
        lines = lines.split("\n")

        for line in lines: 
            self.parseLine(line)

    def parseLine(self,line): 
        line = line.strip()
        
        if not line or line.startswith("*"): 
            return 

        elif line.startswith("."): 
            tokens = line[1:].split() 
            directive = self.parseDirectives(tokens)
            self.directive = directive

        else: 
            tokens = line.split() 
            comp = self.parseComponent(tokens)
            self.circuit.addComponent(comp)


    def parseDirectives(self,tokens): 
        directive = tokens[0]
        arguments = tokens[1:]

        self.simulation_manager.addDirective(directive,arguments)

        



    def parseComponent(self,tokens): 
        
        name = tokens[0]
        # some type of if statement when we have components with different number of nodes 
        nodes = tokens[1:3]
        value = tokens[3]

        if name.startswith("R"): 
            return Resistor(name,nodes,value)

        elif name.startswith("C"): 
            return Capacitor(name,nodes,value)

        elif name.startswith("L"): 
            return Inductor(name,nodes,value)
        
        elif name.startswith("V"): 
            return VoltageSource(name,nodes,value)
    




