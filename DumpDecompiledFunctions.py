from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import os

Program = getCurrentProgram()
DeInterface = DecompInterface()
DeInterface.openProgram(Program)

functions = list(Program.functionManager.getFunctions(True))

OutPath = os.path.join('D:\\', 'Test')
OutFile = OutPath + '\\' + Program.getName() + '.c'

for function in functions:
    results = DeInterface.decompileFunction(function, 0, ConsoleTaskMonitor())
    # print(results.getDecompiledFunction().getC())
    with open(OutFile, 'a+') as File:
        File.write(results.getDecompiledFunction().getC())
    File.close()

