from Interpreter import Interpreter


file = "SpiceTest.txt"


interpreter = Interpreter()
interpreter.parseFile(file)

print(interpreter.circuit)
interpreter.simulation_manager.runDirectives()



