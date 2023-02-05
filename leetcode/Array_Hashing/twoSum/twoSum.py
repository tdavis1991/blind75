def twoSum(self, nums: List[int], target: int) -> List[int]:
    if len(nums) == 2:
        return [0, 1]
    sums = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if nums[i] in sums:
            return [sums[nums[i]], i]
        sums[diff] = i