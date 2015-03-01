__author__ = 'oliver'
import numpy.random as num
import random
import copy
import matplotlib.pyplot as mpl
import numpy.random as npr
class FunctionWrapper:
    """
    Wraps a function in a useful object.
    """
    def __init__(self, name, function, argNum):
        """
        Creates a FunctionWrapper object.
        :param name: The name of the function
        :param function: The function that the object wraps
        :param argNum: The number of arguments required by function
        :return:
        """
        self.name = name
        self.function = function
        self.argNum = argNum

class FunctionNode:
    """
    A class that holds a node of the function tree
    """
    def __init__(self, functionWrapper, children):
        """
        Creates a Node object
        :param functionWrapper: The function wrapper of the function this Node will use
        :param children: List of children Nodes, leftmost nodes come first.
        :return:
        """
        self.functionWrapper = functionWrapper
        self.children = children

    def evaluate(self, parameters):
        """
        Evaluates this nodes children and then this node with parameters given.
        :param parameters: The parameters that will be used by the ParameterNodes
        :return:
        """
        childrenResults = [child.evaluate(parameters) for child in self.children] #Results from child Nodes
        return self.functionWrapper.function(childrenResults)

    def _asString(self, indent=0):
        """
        Recursive way to generate repr string
        :param indent:
        :return:String
        """
        retString = str(indent) + ':' + ('-' * indent) + self.functionWrapper.name + '\n'
        for child in self.children:
            retString += child._asString(indent + 1)

        #retString += '\n'

        return retString

    def __repr__(self):
        return self._asString(0)

class ParameterNode:
    def __init__(self, parameterIndex):
        self.parameterIndex = parameterIndex
    def evaluate(self, parameters):
        return parameters[self.parameterIndex]
    def _asString(self, indent = 0):
        return "{0}:{1}[[{2}]]\n".format(indent, '-' * indent, str(self.parameterIndex))
    def __repr__(self):
        return self._asString(0)

class ConstNode:
    def __init__(self, value):
        self.value = value
    def evaluate(self, parameters):
        return self.value
    def _asString(self, indent = 0):
        return "{0}:{1}{2}\n".format(indent, '-' * indent, self.value)
    def __repr__(self):
        return self._asString(0)

class Tester:
    def __init__(self, popSize, fitnessFunction, inputSize, testdata, functions):
        """

        :rtype : object
        """
        self.fitnessFunc = fitnessFunction
        self.testData = testdata
        self.functions = functions
        self.mutationRate = 0.5
        self.treeMutationRate = 0.8
        self.breedRate = 0.5
        self.inputSize = inputSize
        self.population = [self.makeRandomTree(0.4, 0.4) for x in range(popSize)]
        self.bestFitness = 0

    def makeRandomTree(self, functionProb, paramProb, maxDepth = 10):
        if random.random() < 0.3 and maxDepth > 0:
            func = random.choice(self.functions)
            children = [self.makeRandomTree(functionProb, paramProb, maxDepth) for i in range(func.argNum)]
            return FunctionNode(func,children)
        elif random.random() < paramProb and self.inputSize > 0:
            return ParameterNode(random.randint(0,self.inputSize - 1))
        else:
            return ConstNode(random.choice([random.random(), random.randint(0,10)]))

    def mutateTree(self, rootNode):
        if random.random() < self.treeMutationRate:
            return self.makeRandomTree(random.random(), random.random())
        else:
            result = copy.deepcopy(rootNode)
            if isinstance(result, FunctionNode):
                result.children = [self.mutateTree(c) for c in rootNode.children]
            return result

    def crossover(self, maleNode, femaleNode, top = True):
        if random.random() < 0.7 and not top:
            return copy.deepcopy(femaleNode)
        else:
            result = copy.deepcopy(maleNode)
            if isinstance(maleNode, FunctionNode) and isinstance(femaleNode, FunctionNode):
                result.children = [self.crossover(c, random.choice(femaleNode.children), False) for c in maleNode.children]
            return result

    def _rankFunction(self, rootNode):
        scores = [(self.fitnessFunc(rootNode, self.testData),rootNode) for rootNode in self.population]
        scores.sort()
        return scores
    def getBestFitness(self):
        return self.bestFitness

    def evolve(self, gens):
        for gen in range(gens):
            scores = self._rankFunction(self.population)
            newpop = [scores[0][1], scores[1][1]]
            self.bestFitness = scores[0][0]
            while len(newpop) < len(self.population):
                if random.random() < 0.5:
                    newpop.append(self.crossover(self.population[int(npr.beta(1,2) * (len(self.population) - 1))], self.population[int(npr.beta(1,2) * (len(self.population) - 1))]))
                else:
                    newpop.append(self.mutateTree(self.crossover(self.population[int(npr.beta(1,2) * (len(self.population) - 1))], self.population[int(npr.beta(1,2) * (len(self.population) - 1))])))
            self.population = newpop

def testDistribution(n):
    data = [int(x*100) for x in npr.beta(1,2)]
    mpl.hist(data, bins=20)
    mpl.show()

def iffunc(l):
    if l[0] > 0:
        return l[1]
    else:
        return l[2]

def isgreater(l):
    if l[0] > l[1]:
        return 1
    else:
        return 0

def div(l):
    if (l[1] == 0):
        return 0
    else:
        return l[0] / l[1]

def mod(l):
    if l[1] == 0:
        return 0
    else:
        return l[0] % l[1]

def cmpa(l):
    if l[0] == l[1]:
        return 1
    else:
        return 0

addw = FunctionWrapper("Add", lambda l: l[0] + l[1],2)
subw = FunctionWrapper("Subtract", lambda l: l[0] - l[1], 2)
mulw = FunctionWrapper("Multiply", lambda l: l[0] * l[1], 2)
divw = FunctionWrapper("Divide", div, 2)
ifw = FunctionWrapper("If...Then...Else...", iffunc, 3)
igtw = FunctionWrapper("Is...>...", isgreater, 2)
modw = FunctionWrapper("Modulo", mod, 2)
cmpaw = FunctionWrapper("Compare", cmpa, 2)

arithFunctions = [addw, subw, mulw, divw, modw]
logicFunctions = [ifw, igtw, cmpaw]

