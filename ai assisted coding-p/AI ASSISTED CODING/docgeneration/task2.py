"""Problem 2: Documentation styles for a simple login function."""


def login_with_docstring(user, password, credentials):
	"""Check whether a user's password matches the stored password.

	The credentials dictionary should map usernames to passwords.
	"""
	return credentials.get(user) == password


def login_with_comments(user, password, credentials):
	# Look up the user's stored password and compare it with the given one.
	return credentials.get(user) == password


def login_with_google_style(user, password, credentials):
	"""Check whether the supplied login details are correct.

	Args:
		user: The username to check.
		password: The password supplied by the user.
		credentials: A dictionary mapping usernames to stored passwords.

	Returns:
		True if the username exists and its password matches; otherwise False.
	"""
	return credentials.get(user) == password


# Critical comparison of documentation styles
# project. Consistent
# sections also make it easier to learn many functions quickly. Inline comments
# can still be used for any confusing line inside the function.
#    displayed by help() or a code editor.
#    Disadvantages: A short docstring may leave out details about parameters
#    and return values.
#    Suitable use: Small functions and beginner-level programs.
#
# 2. Inline comments
#    Advantages: They explain a specific line exactly where it appears.
#    Disadvantages: They do not provide a standard place for describing every
#    parameter, return value, or possible error. They can also become outdated.
#    Suitable use: Explaining a short, complex, or unusual line of code.
#
# 3. Google-style documentation
#    Advantages: It organizes parameters and return values in a consistent
#    format, making the function easier to understand and search.
#    Disadvantages: It takes more effort to write and may be too detailed for
#    a very small private function.
#    Suitable use: Shared functions, team projects, and public APIs.
#
# Recommendation
# Google-style documentation is the most helpful for new developers joining a
# project. It gives them a predictable structure for understanding inputs and
# outputs without needing to study the implementation first. Consistent
# sections also make it easier to learn many functions quickly. Inline comments
# can still be used for any confusing line inside the function.