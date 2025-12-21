from functions.write_file import write_file

if __name__ == "__main__":
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for the writing lorem.txt")
    print(result)

    print()

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing morelorem.txt")
    print(result)

    print()

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for the outside of the directory")
    print(result)

    print()
