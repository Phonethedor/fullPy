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

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

test = MathDojo()
print(test.add(2).result)
print(test.add(3,1).result)
print(test.add(1,1,1).result)

print(test.subtract(1,1,1).result)
print(test.subtract(3,1).result)
print(test.subtract(2).result)