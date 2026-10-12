# Python Decorator Example

I’m learning FastAPI and kept running into decorators (like @app.get("/")), but I didn’t fully understand how they work. I built this small example to understand how decorators work in Python.

    A decorator is a function that receives another function, adds some behavior around it, and returns a new function.


### All the code
    def function_one(function_parameter):
        def function_second(a, b):
            print("Hello from second function decorator....")       
            function_parameter(a, b)

        return function_second

    @function_one
    def add(a, b):
        #This is simple add function
        print(f"The result is: {a + b}")

    add(2, 6)

#### Output:
    Hello from second function decorator....
    The result is: 8

### Step by step
#### 1. We need to create a function to receive another function as parameter 
    def function_one(function_parameter): 
#### 2. We create the second function with parameters about "add function (a,b)"
    def function_second(a, b):
        print("Hello from second function decorator....")
#### 3. Inside this function we need to put the function_parameter with parameters a, b
        function_parameter(a, b)

#### 4. Return the second function
        return function_second

#### 5. We call the decorator in this sum function
    @function_one
    def add (a, b):
        #This is simple add function
        print(f"The result is: {a + b}")

#### 6. Call the sum function
    add(2, 6)


### Connection with FastAPI
In FastAPI, @app.get("/") is also a decorator: 
it registers the function below it as the handler for GET /. That one receives an argument ("/"), which adds one more level (a function that returns a decorator). <br>
That's the next thing I want to explore.

