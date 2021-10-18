class solution:
    def twosums(self, nums, target):

        store = {}

        for i in range (len(nums)):
            if nums[i] in store:
                return [store[nums[i]] , i]
            else:
                store[target-nums[i]] = i

obj = solution()
result = obj.twosums([2,7,11,15] , 9)
print(result)  #leetcode question
