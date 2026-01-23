#chat gpt solution:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        # move non-zero elements forward
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # fill remaining with zero
        while write < len(nums):
            nums[write] = 0
            write += 1
# mysolution passing only 2 testcases
class Solution:
    def swap(self, nums, start, end):
        while start < end:
            nums[start], nums[start+1] = nums[start+1], nums[start]
            start += 1

    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        start = 0
        end = n - 1

        while start < end:
            if nums[end] != 0:
                end -= 1

            if nums[end] == 0:
                self.swap(nums, end, n - 1)

            if nums[start] != 0:
                start += 1

            if nums[start] == 0:
                self.swap(nums, start, n - 1)
