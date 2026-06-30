

def SI_prefix(value): 
    
    unit_table = [ 
        [1e-15,"f"], 
        [1e-12,"p"], 
        [1e-9,"n"],
        [1e-6,"u"], 
        [1e-3,"m"], 
        [1,""],
        [1e3,"K"],
        [1e6,"Meg"], 
        [1e9,"G"],
        [1e12,"T"]]
    if value == 0:
        return "0"
    
    if abs(value) < unit_table[0][0]:
         return f"{value/unit_table[0][0]:.3g}" + unit_table[0][1]

    for i in range(len(unit_table)): 
        if abs(value) < unit_table[i][0]: 
            return f"{value/unit_table[i-1][0]:.3g}" + unit_table[i-1][1]
        
    return f"{value/unit_table[-1][0]:.3g}" + unit_table[-1][1]

