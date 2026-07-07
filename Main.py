from Interpreter import Interpreter


file = "SpiceTest.txt"


interpreter = Interpreter()
interpreter.parseFile(file)
# for current 

interpreter.simulation_manager.runDirectives()



