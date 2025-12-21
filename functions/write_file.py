import os
from functions.helpers import get_target
from functions.helpers import is_valid_target


def write_file(working_directory, file_path, content):
    try:
        target_file = get_target(
            working_directory=working_directory, target=file_path
        )

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target(working_directory=working_directory, target=file_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(file_path, exist_ok=True)

        file = open(target_file, "w")
        wrote = file.write(content)

        return f'Successfully wrote to "{file_path}" ({wrote} characters written)'

    except Exception as e:
        return f"Error: {e}"
