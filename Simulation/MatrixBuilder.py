
def BuildMatrix(Circuit,mode): 
    extra_unknown_map = {} 

    extra_unknowns = ["V"]

    if mode == "op": 
          extra_unknowns.append("L")

    for component in Circuit.components: 
        if component.name[0] in extra_unknowns: 
             extra_unknown_map[component.name] = len(Circuit.node_map) + len(extra_unknown_map) 

    n = len(Circuit.node_map)+len(extra_unknown_map)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for component in Circuit.components: 
         matrix = component.stamp(matrix,Circuit.node_map,extra_unknown_map)
        