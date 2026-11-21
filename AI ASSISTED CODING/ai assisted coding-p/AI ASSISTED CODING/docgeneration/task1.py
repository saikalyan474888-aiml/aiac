"""Problem 1: Documentation styles for a mathematical utility function.

Each function below finds and returns the largest value in a list of numbers.
The three versions demonstrate different documentation styles.
"""


def find_max_with_docstring(numbers):
	"""Return the largest number in a list.

	This version uses a clear Python docstring to explain the function.
	"""
	return max(numbers)


def find_max_with_comments(numbers):
	# The max() function compares all values and returns the largest one.
	return max(numbers)


def find_max_google_style(numbers):
	"""Return the largest number in a list of numbers.

	Args:
		numbers: A list or other iterable containing numeric values.

	Returns:
		The largest value found in numbers.

	Raises:
		ValueError: If numbers is empty.
	"""
	return max(numbers)


# Critical comparison of documentation styles
#
# 1. Docstrings
#    Advantages: They are stored with the function, easy to read, and shown
#    by help() and many code editors.
#    Disadvantages: A short docstring may not provide enough detail for
#    parameters, return values, and possible errors.
#    Suitable use: Small functions and simple programs.
#
# 2. Inline comments
#    Advantages: They explain a particular line or step directly beside it.
#    Disadvantages: Too many comments can make code difficult to read, and
#    comments can become incorrect if the code changes.
#    Suitable use: Explaining a complex calculation or an unusual decision.
#
# 3. Google-style documentation
#    Advantages: It gives a consistent structure for arguments, return values,
#    and errors, so it works well with documentation tools.
#    Disadvantages: It takes more time to write and can be excessive for a
#    very small function.
#    Suitable use: Public functions and larger projects or libraries.
#
# Recommendation
# Google-style documentation is the most effective choice for a mathematical
# utilities library. A library may be used by many programmers, so clearly
# documenting inputs, outputs, and errors helps users understand the function
# without reading its implementation. It is also consistent and can be used
# by automatic documentation tools. Inline comments can still be added when a
# mathematical step needs extra explanation.