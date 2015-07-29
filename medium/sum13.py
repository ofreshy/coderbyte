def sum13(nums):
    s = nums[0] if (nums and nums[0] != 13) else 0
    for i in xrange(1, len(nums)):
        if nums[i] != 13 and nums[i-1] != 13:
            s += nums[i]
    return s



print sum13([1, 13, 14])