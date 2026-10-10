# Python Decorator Example

This example of decorator is because I was learning FastAPI and I was the decorator concept but it is not clear for me becasue I want to understand how decorator works in Python


### 1. We need to create a function to receive a function as parameter <br>
    def function_one(function_parameter): <br>
### 2. We create the second function with parameters about "sum function (a,b)"
    def function_second(a, b):
        print("Hello from second function decorator....")<br>
### 3. Inside this function we need to put the function_parameter with parameters a, b<br>
           function_parameter(a, b)<br>

### 4. Return the second function<br>
        return function_second


### 5. We call the decorator in this sum function
    @function_one
    def sum(a, b):
        #This is simple sum function<
        print(f"The result is: {a + b}")

### 6. Call the sum function
    sum(2, 6)


### All code
    def function_one(function_parameter):
        def function_second(a, b):
            print("Hello from second function decorator....")       
            function_parameter(a, b)

        return function_second



    @function_one
    def sum(a, b):
        #This is simple sum function
        print(f"The result is: {a + b}")

    sum(2, 6)
