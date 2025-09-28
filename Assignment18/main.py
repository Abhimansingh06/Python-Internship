from fastapi import FastAPI, Request, HTTPException
from typing import List

app = FastAPI()

# This is the filename where we will store each calculation (like a basic database)
FILE_NAME = "history.txt"

@app.post("/calculate/")
async def calculate(request: Request):
    # Extract JSON data from the request body
    data = await request.json()

    # Extract input values: two numbers and the operation to perform
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")

    # Initialize result variable to store the outcome of the operation
    result = None

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2

        
    with open("history.txt", "r") as fp:
        fp.write(f"{request.num1} {request.operation} {request.num2} = {result}\n")

    return result 


@app.get("/history/")
def get_history():
    try:
        with open("history.txt", "r") as f:
            history = f.readlines()
        return {"history" : history}
    except FileNotFoundError:
        return {"history" : []}

    # TODO: Read the "history.txt" file and return all records as a list
    # Each record should be converted into a dictionary with keys: num1, num2, operation, result

    """
    Example output:
    [
        {"num1": 10.0, "num2": 5.0, "operation": "add", "result": 15.0},
        {"num1": 20.0, "num2": 4.0, "operation": "divide", "result": 5.0}
    ]
    """

    return calculation_history  # List of all past calculations