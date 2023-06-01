"""A series of helper functions."""

from typing import List
import subprocess
import time


def add_timestamp(input_str: str) -> str:
    """Add a timestamp to the end of a string.

    :input_str: The string to add the stamp to

    :Returns: The string with the timestamp added to the end.
    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    if "." in input_str:
        output_str = input_str.replace(".", f"_{timestr}.")
    else:
        output_str = f"{input_str}_{timestr}"
    return output_str


def list_files(dirname: str) -> List[str]:
    """List all files in a directory.

    :dirname: The name of the directory.

    :Returns: The filenames of the contents of the directory
             as a python list.
    """
    cmdline_output = subprocess.check_output(["ls", dirname])
    dir_contents = cmdline_output.decode("utf-8").split()
    return dir_contents

