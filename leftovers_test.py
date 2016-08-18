import unittest
import leftovers

class CourseTest(unittest.TestCase):
    def testCourseEquality(self):
        c1 = leftovers.Course("CS 1331")
        c2 = leftovers.Course("CS 1331")
        self.assertEqual(c1, c2)

    def testCourseInequality(self):
        c1 = leftovers.Course("CS 1331")
        c2 = leftovers.Course("CS 1332")
        self.assertNotEqual(c1, c2)

class LeftoversTest(unittest.TestCase):
    def testCourses(self):
        pass
