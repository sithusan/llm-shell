import os


def get_target(working_directory, target):
    working_directory_abs = os.path.abspath(working_directory)

    return os.path.normpath(os.path.join(working_directory_abs, target))


def is_valid_target(working_directory, target):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, target))

    return (
        os.path.commonpath([working_directory_abs, target_file])
        == working_directory_abs
    )
