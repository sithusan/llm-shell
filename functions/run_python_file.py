import os
import subprocess
from functions.helpers import get_target
from functions.helpers import is_valid_target
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        target_file = get_target(working_directory=working_directory, target=file_path)

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target(working_directory=working_directory, target=file_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        command = ["python", target_file]

        if args is not None:
            command.extend(args)

        completedProcess = subprocess.run(
            command, cwd=working_directory, capture_output=True, text=True, timeout=30
        )

        result = []

        if completedProcess.returncode != 0:
            result.append(f"Process exited with code {completedProcess.returncode}")

        if len(completedProcess.stdout) == 0 and len(completedProcess.stderr) == 0:
            result.append("No output produced")

        if len(completedProcess.stdout) > 0:
            result.append(f"STDOUT: {completedProcess.stdout}")

        if len(completedProcess.stderr) > 0:
            result.append(f"STDERR: {completedProcess.stderr}")

        return "\n".join(result)

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the given python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the python file that want to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="The arg that needs to run the python file",
                ),
                description="The args that need to run the python file",
            ),
        },
        required=["file_path"],
    ),
)
