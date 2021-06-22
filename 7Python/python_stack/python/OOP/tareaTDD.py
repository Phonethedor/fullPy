import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        if nums == None:
            return self
        else:
            for a in range(0,len(nums)):
                self.result += int(nums[a])
            return self
    def subtract(self, num, *nums):
        self.result -= num
        if nums == None:
            return self
        else:
            for a in range(0,len(nums)):
                self.result -= int(nums[a])
            return self

class MathTest(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()
    def testAdd(self):
        self.assertEqual(self.md.add(2,4,6,8,10).result, 2+4+6+8+10)
    def testSubstract(self):
        self.assertEqual(self.md.subtract(10,2,3,4).result, 2-3-4)

if __name__ == '__main__':
    unittest.main()