import neuralTree as nt
import functions as funcs
import matplotlib.pyplot as mpl
import inspect
def Test1():
    """
    Tried to evolve a program to compute the fibonacci sequence.
    This didn't work at all due to how to the fitness function was structured.
    It may have worked after enough generations.

    I tried to severely restrict the problem space by limiting it to just using
    add function nodes.

    The problem was that the fitness function relied on the last value outputted by the
    program, which is usually wrong. This could possibly be resolved by weighting the first results
    correctness higher relative to the rest of the test input.

    """
    def fitnessFunc(node, data):
        total = 0
        val = 1
        val1 = 0
        for set in data:
            temp = val
            val= abs(node.evaluate([val, val1]) - set[1])
            val1 = temp
            total += val
        return total
    tester = nt.Tester(90, fitnessFunc,2,[(1,1), (2,2), (3,3), (4,5), (5,8), (6,13), (7, 21), (8, 34), (9, 55)], [funcs.addw])
    #print tester.population
    tester.evolve(1000)
    print tester.population[0]
    print tester.getBestFitness()
    print tester.data
    mpl.plot(tester.data)
    mpl.show()

def Test2():
    """
    Second attempt to evolve a program that outputs the fibonacci sequence.
    I have given the program the correct last 2 values to compute with.
    This method worked instantaneously with the correct program being
    created in the first batch of programs.

    Shows that it's important to get the fitness function correct.

    """
    def fitnessFunc(node, data):
        total = 0
        for set in data:
            val= abs(node.evaluate([set[0], set[1]]) - set[2])
            total += val
        return total
    tester = nt.Tester(90, fitnessFunc,2,[(0,1,1), (1,1,2), (1,2,3), (2,3,5), (3,5,8), (5,8,13), (8,13, 21), (13,21, 34), (21,34, 55)], [funcs.addw])
    tester.evolve(100)
    print tester.population[0]
    print tester.getBestFitness()
    mpl.plot(tester.data)
    mpl.show()

#Test2()