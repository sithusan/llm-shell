from functions.get_file_contents import get_file_content

if __name__ == "__main__":
    result = get_file_content("calculator", "lorem.txt")
    print("Result for the lorem.txt")
    print(result)

    print()

    result = get_file_content("calculator", "main.py")
    print("Result for subdirectory")
    print(result)

    print()

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for the calculator.py")
    print(result)

    print()

    result = get_file_content("calculator", "/bin/cat")
    print("Result for the outside of the working directory")
    print(result)

    print()

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for the outside of the working directory")
    print(result)

    print()
