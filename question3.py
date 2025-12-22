nums = [5,7,7,8,8,8,10]
target = 6

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def Binary(nums, target, searchLeft):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if searchLeft:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = Binary(nums, target, True)
        right = Binary(nums, target, False)
        
        return [left, right]