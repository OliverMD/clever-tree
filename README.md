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

## Tests

### Test1 and Test2
These are some really tests that try to eveolve a program that generates the fibonacci sequence.
Test1 doesn't accomplish this but Test2 does and shows the difference between a good and bad fitness
function.

