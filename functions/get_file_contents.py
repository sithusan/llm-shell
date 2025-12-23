import os
import config
from functions.helpers import get_target
from functions.helpers import is_valid_target
from google.genai import types


def get_file_content(working_directory, file_path):

    try:
        target_file = get_target(working_directory=working_directory, target=file_path)

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target(working_directory=working_directory, target=file_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file = open(target_file, "r")
        content = file.read(config.MAX_CHARS)

        # truncated file is too large
        if file.read(config.MAX_CHARS + 1):
            content += (
                f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
            )

        return content

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of the given file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file that want to get the contents",
            ),
        },
        required=["file_path"],
    ),
)
