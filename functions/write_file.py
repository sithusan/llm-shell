import os
from functions.helpers import get_target
from functions.helpers import is_valid_target
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        target_file = get_target(working_directory=working_directory, target=file_path)

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target(working_directory=working_directory, target=file_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        file = open(target_file, "w")
        wrote = file.write(content)

        return f'Successfully wrote to "{file_path}" ({wrote} characters written)'

    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the given content to the file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file that want to write the contents",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
