"""Create a dated pytest output directory."""

import time
import os

from tests.helper import list_files

timestr = time.strftime("%Y_%m_%d_")

num_directories = len(
    [dirname for dirname in list_files("tests/test_output") if timestr in dirname]
)

TEST_OUTPUT = f"tests/test_output/{timestr}{num_directories+1}"
os.makedirs(TEST_OUTPUT)

