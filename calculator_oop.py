print("Assignment 7".center(45, "="))
print("~" * 45)
print("CMPE-103-MODULE-4-APPLYING-THE CONCEPT-OF-OOP")
print("~" * 45)

# redo the creation of a simple app calculator program with the concept of OOP.

# pseudocode
# create the class of user interface
# create another class for the calculator

# greetings
print("Great Day, a precious well-being!")

# import the python files from the module created
from user_module import UserInterface
from calculator_app import SimpleAppCalculator

program = SimpleAppCalculator()
interaction = UserInterface()

# implement the program
def simple_app_calculator():
    # use try and except function
    try:
        selection = interaction.basic_math_operations()
        var1 = interaction.var1()
        var2 = interaction.var2()
    # execute the recognized chosen operation
