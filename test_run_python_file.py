from functions.run_python_file import run_python_file

if __name__ == "__main__":
    result = run_python_file("calculator", "main.py")
    print("Result for running calculator main with default")
    print(result)

    print()

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for running calculator main with correct usage")
    print(result)

    print()

    result = run_python_file("calculator", "tests.py")
    print("Result for running calculator's tests")
    print(result)

    print()

    result = run_python_file("calculator", "../main.py")
    print("Result for running outside of the working directory")
    print(result)

    print()

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running non existent file")
    print(result)

    print()

    result = run_python_file("calculator", "lorem.txt")
    print("Result for running non python file")
    print(result)

    print()
