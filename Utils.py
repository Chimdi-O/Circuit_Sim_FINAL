



def parseUnits(value): 
    i = len(value)-1 # suffix start 

    while i >=0 and value[i].isalpha(): 
        i -= 1

    num = value[:i+1]
    unit = value[i+1:]    

    unit_table = {
        "t":1e12, 
        "g":1e9,
        "meg":1e6, 
        "k":1e3, 
        "":1, 
        "m":1e-3, 
        "u":1e-6, 
        "n":1e-9,
        "p":1e-12,
        "f":1e-15}
    
    return float(num) * unit_table[unit.lower()]


