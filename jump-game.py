class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Take current variable to keep the current maximum jump...
        current = nums[0]
        # Traverse all the elements through loop...
        for i in range(1,len(nums)):
            # If the current index 'i' is less than current maximum jump 'curr'...
            # It means there is no way to jump to current index...
            # so we should return false...
            if current == 0:
                return False
            current -= 1
            # Update the current maximum jump...
            current = max(current, nums[i])       # It’s possible to reach the end of the array...
        return True