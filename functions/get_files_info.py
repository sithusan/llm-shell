import os


def get_files_info(working_directory, directory="."):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

        is_valid_target_dir = (
            os.path.commonpath([working_directory_abs, target_dir])
            == working_directory_abs
        )

        # Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data
        if not is_valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(target_dir)

        result = []
        for content in contents:
            content_abs_path = os.path.normpath(os.path.join(target_dir, content))
            size = os.path.getsize(content_abs_path)
            result.append(
                f"- {content}: file_size={size} bytes, is_dir={os.path.isdir(content_abs_path)}"
            )

        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"
