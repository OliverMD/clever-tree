# clever-tree
A genetic programming tool for python. With tests and other weird things.

## Use

### For genetic programming

For genetic programming you're going to want to use the Tester class from neuralTree.py
You also need to create your own fitness function to pass to the constrcutor of the Tester
class. The fitness function takes a Node as a parameter and a list as the second parameter.

The list is supposed to be your test dataset, which can be set from an instance of Tester.
It's up to you to decide how to structure this list. I usually have it as a list of tuples
with each tuple as a different test.

Please look at the tests to identify how to use it.

### As a neural network

I'm still yet to implement this functionality

## Tests

### Test1 and Test2
These are some really tests that try to eveolve a program that generates the fibonacci sequence.
Test1 doesn't accomplish this but Test2 does and shows the difference between a good and bad fitness
function.

## Plans
1. Allow for what all intents and purposes is a neural network to be evolved.
2. Implement a back propagation algorithm for such a use.
3. Run some tests and see wht interesting things it can be used for.
4. I may port this to a more efficient language in the future.
