def removeElement(self, nums: List[int], val: int) -> int:
        new_i = 0
        for num in nums:
            if num != val:
                nums[new_i] = num
                new_i += 1
        return new_i
