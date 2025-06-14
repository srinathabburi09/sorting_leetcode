from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: If the list has 1 or 0 elements, it's already sorted
        if len(nums) <= 1:
            return nums

        # Find the middle index
        mid = len(nums) // 2

        # Recursively sort both halves
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        # Merge the sorted halves
        return self.merge(left_half, right_half)

    def merge(self, left_half: List[int], right_half: List[int]) -> List[int]:
        sorted_arr = []
        i, j = 0, 0

        # Merge elements from both halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sorted_arr.append(left_half[i])
                i += 1
            else:
                sorted_arr.append(right_half[j])
                j += 1

        # Add remaining elements from left or right
        sorted_arr.extend(left_half[i:])  # Adds remaining elements from left
        sorted_arr.extend(right_half[j:])  # Adds remaining elements from right

        return sorted_arr
