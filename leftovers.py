from typing import Iterable, Union

class Course(object):
    """
    Represents a course that a student might take.
    """
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: 'Course'):
        return (isinstance(self, Course) and 
                isinstance(other, Course) and self.name == other.name)

class Requirement(object):
    def __init__(self, 
            items: Iterable[Union['Requirement', Course]],
            num: int):
        """
        A requirement represents something that must be completed.

        `num` represents the number of the children that must be completed for
        the requirement to be satisfied.
        """
        self.courses = {c for c in items if isinstance(c, Course)}
        self.children = {r for r in items if isinstance(r, Requirement)}
        self.completed = set()  # completed courses
        self.num = num

    @property
    def satisfied(self):
        if len(self.completed) < self.num:
            return False
        if not self.completed < self.courses: 
            return False
        for child in self.children:
            if not child.satisfied:
                return False
        return True

