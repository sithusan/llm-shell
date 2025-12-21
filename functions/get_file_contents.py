import os
import config


def get_file_content(working_directory, file_path):

    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

        is_valid_target_file = (
            os.path.commonpath([working_directory_abs, target_file])
            == working_directory_abs
        )

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target_file:
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
