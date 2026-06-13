from Interpreter import Interpreter


file = "Circuit_Sim_FINAL/SpiceTest.txt"


interpreter = Interpreter()
interpreter.parsefile(file)

print(interpreter.circuit)



