"""Example test function."""

from computer_vision import __version__

from tests.helper import add_timestamp

from tests.output import TEST_OUTPUT

def test_version():
    """Test the package version."""
    assert __version__ == '0.1.0'

def test_file():
    """Generate a time stamped test output file."""
    # create timestamped output filename
    output_filename = add_timestamp(f"{TEST_OUTPUT}/test.txt")
    # write output file to the test_output directory
    with open(output_filename,"w+") as f:
        f.write("example")
