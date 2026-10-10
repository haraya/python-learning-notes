# This is an example of python decorator

# 1. We need to create a function to receive a function as parameter 
def function_one(function_parameter):

    # 2. We create the second function with parameters about "sum function (a,b)"
    def function_second(a, b):
        
        # 3. Inside this function we need to put the function_parameter with parameters a, b
        function_parameter(a, b)

    # 4. Return the second function
    return function_second


#This is simple sum function
def sum(a, b):
    print(f"The result is: {a + b}")


sum(2, 6)