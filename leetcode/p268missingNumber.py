class Solution:
    def missingNumber(nums):
        # My initial idea
        # nums.sort()
        # for index, num in enumerate(nums):
        #     if index != num:
        #         return index

        # return len(nums)

        return (sum(range(len(nums) + 1))) - sum(nums)


# My Idea

# So since we know the numbers have to be in range [0, len(nums)],
# I thought that if first sort nums then we can compare it with the index.
# If each of the sorted elements == index, then that is NOT the missing number.
# If they are not equal, then that index is missing so we return it.
# The last case is if len(nums) is the missing number. However, because we use .sort this is O(nlogn)


# Better Solution

# A better solution is to find the sum of integers from 0 to the length of nums (inclusive).
# We compare this with the sum of nums and by finding the difference, we get the integer
# that is not in the array. This is faster b/c we do not have to use .sort which makes this
# O(nlogn).
