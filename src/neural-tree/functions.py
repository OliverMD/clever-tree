from neuralTree import *
__author__ = 'oliver'
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

sumw = FunctionWrapper("Sum", sum, 20, True)
tanhw = FunctionWrapper("tanh", lambda l: math.tanh(l[0]), 1)
netFunctions = [sumw, tanhw]
arithFunctions = [addw, subw, mulw, divw, modw]
logicFunctions = [ifw, igtw, cmpaw]