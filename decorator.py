# This is an example of python decorator

# 1. We need to create a function to receive a function as parameter 
def function_one(function_parameter):

    # 2. We create the second function with parameters about "add function (a,b)"
    def function_second(a, b):
        print("Hello from second function decorator....")

        # 3. Inside this function we need to put the function_parameter with parameters a, b
        function_parameter(a, b)

    # 4. Return the second function
    return function_second


# 5. We call the decorator in this add function
@function_one
def add(a, b):
    #This is simple add function
    print(f"The result is: {a + b}")


# 6. Call the add function
add(2, 6)