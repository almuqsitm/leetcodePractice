def containsDuplicate(nums):
    my_set = list(set(nums))
    if len(my_set) == len(nums):
        return False
    else:
        return True


# My Idea

# Since we want to find whether there are any duplicates, we could use a set so that
# we only get 1 occurence of each element in nums. If the length of this set is
# equivalent to the length of the original list nums, then that means
# there were no duplicates. In that case we return False.
# Rest of cases we return True --> contains duplicates.
