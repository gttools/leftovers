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
    def setUp(self):
        self.cs1331 = leftovers.Course("CS1331")
        self.cs1301 = leftovers.Course("CS1301")
        self.cs1332 = leftovers.Course("CS1332")

    def testNoRequirementsNotMet(self):
        reqs = leftovers.Requirement([self.cs1301, self.cs1331], 2)
        self.assertFalse(reqs.satisfied)

    def testSingleRequirementMet(self):
        reqs = leftovers.Requirement([self.cs1301], 1)
        reqs.complete(self.cs1301)
        self.assertTrue(reqs.satisfied)

    def testSomeReqsNotMet(self):
        reqs = leftovers.Requirement([self.cs1301, self.cs1331], 2)
        reqs.complete(self.cs1301)
        self.assertFalse(reqs.satisfied)

    def testRequirementsMet(self):
        reqs = leftovers.Requirement([self.cs1301, self.cs1331], 2)
        reqs.complete(self.cs1301)
        reqs.complete(self.cs1331)
        self.assertTrue(reqs.satisfied)
    
    def testNestedRequirementsMet(self):
        reqs = leftovers.Requirement([self.cs1301, self.cs1331], 2)
        bigreq = leftovers.Requirement([reqs, self.cs1332], 2)
        bigreq.complete(self.cs1301)
        bigreq.complete(self.cs1331)
        bigreq.complete(self.cs1332)
        self.assertTrue(bigreq.satisfied)
