from functions.get_files_info import get_files_info

if __name__ == "__main__":
    result = get_files_info("calculator", ".")
    print("Result for the current directory")
    print(result)

    print()

    result = get_files_info("calculator", "pkg")
    print("Result for subdirectory")
    print(result)

    print()

    result = get_files_info("calculator", "/bin")
    print("Result for the outside of the working directory")
    print(result)

    print()

    result = get_files_info("calculator", "../")
    print("Result for the outside of the directory")
    print(result)
