class UserInterface:
# pseudocode
# ask the user for its choice of operation
def basic_math_operations(self):
    print("I have here the basic math operations which are the Addition, Subtraction, Multiplication, and Division")
    selection = input("Pick a basic math operation among these four (+|-|*|/): ")
    return selection

# ask the user for two variables to solve
def var1(self):
    var1 = float(input("Enter your first variable number: "))
    return var1

def var2(self):
    var2 = float(input("Enter your second variable number: "))
    return var2

# print the result of the inputs.
# once again, ask the user if want to try again or not