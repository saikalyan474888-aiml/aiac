"""A simple course management module."""


# Store each course ID with its name and credit count.
courses = {}


def add_course(course_id, name, credits):
    """Add a course to the course dictionary.

    Args:
        course_id (str): The unique ID of the course.
        name (str): The name of the course.
        credits (int): The number of credits for the course.

    Returns:
        dict: The course information that was added.
    """
    course = {"name": name, "credits": credits}
    courses[course_id] = course
    return course


def remove_course(course_id):
    """Remove a course from the course dictionary.

    Args:
        course_id (str): The ID of the course to remove.

    Returns:
        bool: True if removed, or False if the course did not exist.
    """
    if course_id in courses:
        del courses[course_id]
        return True

    return False


def get_course(course_id):
    """Return course information for a course ID.

    Args:
        course_id (str): The ID of the course to find.

    Returns:
        dict or None: Course information, or None if the ID does not exist.
    """
    return courses.get(course_id)