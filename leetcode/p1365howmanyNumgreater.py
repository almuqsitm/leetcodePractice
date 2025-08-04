class Solution:
    def smallerNumbersThanCurrent(nums):
        # res = [0] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         elif nums[j] < nums[i]:
        #             res[i] += 1

        # return res

        temp = sorted(nums)  # 1 2 2 3 8
        dic = {}

        for index, num in enumerate(temp):
            if num not in dic:
                dic[num] = index
        res = []

        for i in nums:
            res.append(dic[i])

        return res


# Explanation

# My initial solution works but that is the brute force method result in O(n^2).
# To make this better, we can use a hashmap for when we need to create an array of elements smaller than current.
# Before that we need a sorted array so that the first index of each element is how many numbers are smaller than the current.
# By using a hashmap, the lookup is O(1) resulting in an O(nlogn) solution due to using sorted.
