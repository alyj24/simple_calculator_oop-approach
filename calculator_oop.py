print("Assignment 7".center(45, "="))
print("\033[95m~" * 45)
print("\033[94mCMPE-103-MODULE-4-APPLYING-THE CONCEPT-OF-OOP")
print("\033[95m~" * 45)

# redo the creation of a simple app calculator program with the concept of OOP.

# pseudocode
# create the class of user interface
# create another class for the calculator

# greetings
print("\033[93mGreat Day, a precious well-being!")

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
        if selection == "+":
           sum = program.__add__(var1, var2)
           interaction.sum(sum)

        elif selection == "-":
           difference = program.__subtract__(var1, var2)
           interaction.difference(difference)

        elif selection == "*":
            product = program.__multiply__(var1, var2)
            interaction.product(product)

        elif selection == "/":
            quotient = program.__divide__(var1, var2)
            interaction.quotient(quotient)
        else:
             print("\033[93mOh no! There must be a problem in your input to be invalid.")

        while True:
             option = interaction.retry()
             if option == "yes, indeed":
                return simple_app_calculator()

             elif option == "already satisfied":
                   print("\033[95mThank you so much!")

             else:
                   exit()

    except ValueError:
        print("\033[92mOops! Take a look back for a second, there must be a problem.")

simple_app_calculator()