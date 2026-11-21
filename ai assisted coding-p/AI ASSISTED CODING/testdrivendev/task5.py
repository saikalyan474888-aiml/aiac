def run_tests():
	# Required test cases
	assert validate_and_format_date("10/15/2023") == "2023-10-15"
	assert validate_and_format_date("02/30/2023") == "Invalid Date"
	assert validate_and_format_date("01/01/2024") == "2024-01-01"

	# Edge-case tests
	assert validate_and_format_date("02/29/2024") == "2024-02-29"
	assert validate_and_format_date("13/15/2023") == "Invalid Date"
	assert validate_and_format_date("04/31/2023") == "Invalid Date"
	assert validate_and_format_date("2023-10-15") == "Invalid Date"


from datetime import datetime


def validate_and_format_date(date_str):
	# Check that the input has exactly the MM/DD/YYYY format.
	if (
		not isinstance(date_str, str)
		or len(date_str) != 10
		or date_str[2] != "/"
		or date_str[5] != "/"
		or not date_str[:2].isdigit()
		or not date_str[3:5].isdigit()
		or not date_str[6:].isdigit()
	):
		return "Invalid Date"

	try:
		# datetime checks whether the month, day, and year are valid.
		valid_date = datetime.strptime(date_str, "%m/%d/%Y")
		return valid_date.strftime("%Y-%m-%d")
	except ValueError:
		return "Invalid Date"


run_tests()
print("All Task 5 tests passed!")