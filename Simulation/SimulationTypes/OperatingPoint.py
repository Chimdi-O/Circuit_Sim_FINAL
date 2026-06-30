from Simulation.MatrixMaths import buildMatrix, matrixSolver
from SIunit import SI_prefix


class OperatingPoint(): 
    def __init__(self,circuit): 
        self.circuit = circuit 
        self.results_matrix = [] 

    def run(self): 
        matrix = buildMatrix(self.circuit,"op")
        self.results_matrix = matrixSolver(matrix)
        self.output()
        
    def output(self): 
        print("       --- Operating Point ---")

        node_index = 0 
        longest_node_len = 0    
        key_list = list(self.circuit.node_map.keys()) 

        for i in key_list: 
            if len(i) > longest_node_len: 
                longest_node_len = len(i)

        variable_box_size = longest_node_len + 4 
        longest_value_len = 0 
      
        # printing voltages
        while node_index < 3: 
            #pass
            
            node = self.circuit.reversed_node_map[node_index]
            value = round(self.results_matrix[node_index][-1],3)
            value = SI_prefix(value)

            print(f"{f"V({node})":<10} :       {value}V")

            node_index += 1 

        for i in self.circuit.components: 
            if i.name[0] == "C": 
                 print(f"{f"I({node})":<10} :       {0}A")
            
            elif i.name[0] == "R": 

                node1_V = 0 
                node2_V = 0 
                
                if i.nodes[0] != "0": 
                    node1_V = self.results_matrix[self.circuit.node_map[i.nodes[0]]][-1]
                
                if i.nodes[1] != "0": 
                    node2_V = self.results_matrix[self.circuit.node_map[i.nodes[1]]][-1]
                

                current = (node1_V - node2_V)/i.num_value
                current = SI_prefix(current)
                print(f"{f"I({i.name})":<10} :       {current}A")

 
            elif i.name[0] == "L" or i.name[0] == "V": 
                index = self.circuit.extra_unknown_map[i.name]
                current = self.results_matrix[index][-1]
                current = SI_prefix(current)
                print(f"{f"I({i.name})":<10} :       {current}A")

                pass 
                

        #for compoent
     

    
    