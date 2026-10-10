# Python Decorator Example

I’m learning FastAPI and kept running into decorators (like @app.get("/")), but I didn’t fully understand how they work. I built this small example to understand how decorators work in Python.

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

### 1. We need to create a function to receive a function as parameter 
    def function_one(function_parameter): 
### 2. We create the second function with parameters about "sum function (a,b)"
    def function_second(a, b):
        print("Hello from second function decorator....")
### 3. Inside this function we need to put the function_parameter with parameters a, b
           function_parameter(a, b)

### 4. Return the second function
        return function_second

### 5. We call the decorator in this sum function
    @function_one
    def add (a, b):
        #This is simple add function
        print(f"The result is: {a + b}")

### 6. Call the sum function
    add(2, 6)

@app.get("/") is a decorator that registers your function as the response for that route.

