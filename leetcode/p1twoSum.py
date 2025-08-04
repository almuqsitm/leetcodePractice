class Solution:
    def twoSum(nums, target):
        # [2, 4, 5, 8]
        my_dict = {}

        for index, val in enumerate(nums):
            if (target - val) in my_dict:
                return index, my_dict[target - val]
            my_dict[val] = index


# Explanation

# So this can obviously be done with 2 for loops but that is O(n^2).
# To get an O(n) solution we can use a hashmap to check if target - val exists,
# if so then we got two numbers that sum to target --> current val and the val existent in
# hashmap.
