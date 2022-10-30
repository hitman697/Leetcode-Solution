class Sol(obj):
    def search(self, nums, need):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > need:
                right = mid-1
            elif nums[mid] < need:
                left = mid+1
            else:
                return mid
        return -1
