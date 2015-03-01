import neuralTree as nt

def Test1():
    def fitnessFunc(node, data):
        total = 0
        for set in data:
            total += abs(node.evaluate([set[0]]) - set[1])
        return total
    tester = nt.Tester(20, fitnessFunc,1,[(1,1), (2,4), (3,9), (4,16)], nt.arithFunctions)
    tester.functions = nt.arithFunctions
    tester.evolve(100)
    print tester.population[0]
    print tester.getBestFitness()

Test1()