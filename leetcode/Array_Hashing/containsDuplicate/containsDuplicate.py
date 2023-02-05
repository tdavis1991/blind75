def containsDuplicate(self, nums: List[int]) -> bool:
    if len(nums) <= 1:
        return False
    dupe = set()
    for num in nums:
        if num in dupe:
            return True
        else:
            dupe.add(num)
    return False