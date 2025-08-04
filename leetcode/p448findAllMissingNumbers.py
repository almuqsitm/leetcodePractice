class Solution:
    def findDisappearedNumbers(nums):
        my_set = set(nums)

        res = []

        for i in range(1, len(nums) + 1):
            if i not in my_set:
                res.append(i)

        return res


# My Idea

# Initially I wanted to loop from 1-n and then get all the numbers not in that range in the list.
# However, since there are duplicates, a set would make this slightly faster.
# Then we check if each number in range 1-n (inclusive) exists in the set and
# append the result array if it does not. This gives an O(n) solution.
