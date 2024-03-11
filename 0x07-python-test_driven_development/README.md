# Python Test-Driven Development

## Introduction

This project is all about Test-Driven Development (TDD) in Python. TDD is a software development approach in which tests are written before the actual code. It allows developers to ensure their code is working as expected and helps prevent bugs.

## Getting Started

1. **Install Python**: Make sure you have Python installed on your machine. You can download it from the official Python website.

2. **Set Up a Virtual Environment**: It's a good practice to create a virtual environment for your project. You can do this using the `venv` module in Python:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Required Packages**: Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Writing Tests

In TDD, we start by writing tests. We use Python's built-in `unittest` module to write our tests. Here's an example of what a test case might look like:

```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

# Running Tests

To run the tests, navigate to the project directory and run the following command:

```bash
python -m unittest discover
```
