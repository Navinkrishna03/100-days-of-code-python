
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

Operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def Calculator():
    previous_result = 0
    Should_Accumulate = True
    while Should_Accumulate:
        n1 = float(input("What's the first number: "))
        operator = input(
            "+\n"
            "-\n"
            "*\n"
            "/\n"
            "Pick an operation: ")
        n2 = float(input("Next number: "))
        result = Operations[operator](n1, n2)
        previous_result+=result
        yes_or_new = input(f"Type 'y' to continue with {result}: or type 'n' to start a new calculation: ")
        if yes_or_new == "y":
            operator = input(
                "+\n"
                "-\n"
                "*\n"
                "/\n"
                "Pick an operation: ")
            n2 = float(input("Enter second number: "))
            result = Operations[operator](previous_result, n2)
            yes_or_new = input(f"Type 'y' to continue with {result}: or type 'n' to start a new calculation: ")
        else:
            Should_Accumulate = False
            print("\n" * 20)
            Calculator()

Calculator()