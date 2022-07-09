# Acceptance Criteria
## When scrolling through your Replit, it should be easy to tell what section your solutions belong to with commented titles.
## When running your Replit, there should be no errors displayed in the console.
## If there are errors you could not solve, comment out the lines throwing errors and explain what steps you used to try and fix them.
## Make sure your thought question answers are commented out.


## ---------------
#Functional Prompt
##Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
## Given an array of integers in random order, running it through your pure function solution should sort it in ascending order.
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# Once a functional solution to this problem has been implemented, answer the following questions.
## How does this solution ensure data immutability?  No inputs or global data is changed. 
## Is this solution a pure function? Why or why not? Yes, it takes input array and returns a sorted array in a variable
## Is this solution a higher order function? Why or why not? No, there is no function passing
## Would it have been easier to solve this problem using a different programming style? No, it's fine
## Why in particular is functional programming a helpful paradigm when solving this problem? OOP is unnecessary for this


## ---------------
# Object Oriented Prompt
# # Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# # First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# # Define a repair() method that will update the condition of the podracer to "repaired".
# # Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
# # Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

## Given a pod created from your defined Podracer class, running pod.repair() and printing the pod.condition afterwards should display "repaired" in the console.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

## Given another new_pod created from your defined AnakinsPod class with a max_speed of 2, running new_pod.boost() and printing the new_pod.max_speed afterwards should display "4".
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

## Given a third_pod created from your defined SebulbasPod class, running third_pod.flame_jet() and printing the third_pod.condition afterwards should display "thrashed" in the console.
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        self.condition = "thrashed"

# # Once an Object Oriented solution has been implemented, answer the following questions:
# # How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# # # Encapsulation - external interface perform actions on the object
# # # Abstraction - contains internal data/characteristics not accessible to the outside
# # # Inheritance - classes AnakinsPod and SebulbasPod are derivations of the parent Podracer class
# # # Polymorphism - does not exist in this model as no methods are overwritten
# # Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? - There is code reusability for each of the derived child classes/objects
# # How in particular did Object Oriented Programming assist in the solving of this problem? -- By formating it in an object-style,  it makes the design easier to understand by objectifying the solution and provides code reusability and makes it easy to add additional derivation of the parent class.