def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except OSError:
        return "Error: Invalid file path."


class Print:
    """Small output helper with concrete write and flush operations."""

    def __init__(self, stream=None):
        import sys

        self.stream = stream or sys.stdout

    def write(self, message=""):
        """Write a message and return the number of characters written."""
        return self.stream.write(str(message))

    def flush(self):
        """Flush the underlying output stream."""
        return self.stream.flush()


printer = Print()
printer.write(read_file("nonexistent.txt"))
printer.write("\n")