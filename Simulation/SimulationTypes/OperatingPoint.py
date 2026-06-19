from Simulation.MatrixBuilder import buildMatrix
from Simulation.Solver import matrixSolver


class OperatingPoint(): 
    def __init__(self,circuit): 
        self.circuit = circuit 

    def run(self): 
        matrix = buildMatrix(self.circuit,"op")
        solution = matrixSolver(matrix)
        for i in solution: 
            print(i)

     

    
        
