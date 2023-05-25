class SimpleAppCalculator:
    # pseudocode
    # recognize the two input numbers and solve for  the choice of operation
    # define the operations
    # addition
    def __add__(self, var1, var2):
        sum = var1 + var2
        return sum

    # subtraction
    def __subtract__(self, var1, var2):
        difference = var1 - var2
        return difference

    # multiplication
    def __multiply__(self, var1, var2):
        product = var1 * var2
        return product

    # division
    def __divide__(self, var1, var2):
        quotient = var1 / var2
        return quotient