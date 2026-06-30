from Interpreter import Interpreter


file = "SpiceTest.txt"


interpreter = Interpreter()
interpreter.parseFile(file)


interpreter.simulation_manager.runDirectives()



