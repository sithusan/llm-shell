import os
from functions.helpers import get_target
from functions.helpers import is_valid_target
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        target_dir = get_target(working_directory=working_directory, target=directory)

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target(working_directory=working_directory, target=target_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        result = []
        for filename in os.listdir(target_dir):
            filename_abs = os.path.normpath(os.path.join(target_dir, filename))
            size = os.path.getsize(filename_abs)
            result.append(
                f"- {filename}: file_size={size} bytes, is_dir={os.path.isdir(filename_abs)}"
            )

        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
