from typing import Iterable, Union

class NoChildException(Exception):
    pass

class Course(object):
    """
    Represents a course that a student might take.
    """
    def __init__(self, name: str, hours: int=3):
        self.name = name
        self.hours = hours

    def __eq__(self, other: 'Course') -> bool:
        return (isinstance(self, Course) and 
                isinstance(other, Course) and self.name == other.name)

    def __hash__(self):
        return hash(self.name)

class Requirement(object):
    def __init__(self, 
            items: Iterable[Union['Requirement', Course]],
            num: int,
            additional_hours: int=0):
        """
        A requirement represents something that must be completed.

        `num` represents the number of children that must be completed for
        the requirement to be satisfied.
        """
        self.courses = frozenset(c for c in items if isinstance(c, Course))
        self.children = [r for r in items if isinstance(r, Requirement)]
        self.completed = set()  # completed courses
        self.num = num
        self.additional_hours = additional_hours

    @property
    def satisfied(self) -> bool:
        return (len(self.completed & self.courses) + 
                sum(1 for x in self.children if x.satisfied)) >= self.num

    def complete(self, course: Course):
        if course in self.courses:
            self.completed.add(course)
        else:
            for child in self.children:
                try:
                    child.complete(course)
                    break
                except NoChildException:
                    pass
            else:
                raise NoChildException

