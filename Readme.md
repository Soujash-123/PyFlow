# PyFlow

PyFlow is a web-based tool that generates flowcharts from Python code. It parses Python code, creates an abstract syntax tree (AST), and visualizes the control flow using flowchart diagrams.


## Overview

PyFlow simplifies the process of understanding and visualizing the control flow of Python code. It offers an intuitive interface where users can input their Python code, and PyFlow automatically generates a flowchart representing the code's control flow structure. This visualization aids in comprehension, debugging, and code documentation.

## How it Works

PyFlow utilizes the PyFlowchart library, a Python package built on top of NetworkX and Matplotlib. The PyFlowchart library provides functionality to parse Python code into an AST and generate a flowchart representation of the code's control flow.

When a user inputs Python code into PyFlow's interface and clicks the "Generate" button, PyFlow sends the code to the backend. The backend then uses the PyFlowchart library to parse the code, create an AST, and generate a flowchart. The resulting flowchart is displayed to the user in the interface.

## Demo

Check out the live demo [here](https://pyflow.onrender.com).

## Usage

To use PyFlow locally:

1. Clone this repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd pyflow`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Open your web browser and go to `http://localhost:5000`

## Example

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Factorial of 5 is:", result)
