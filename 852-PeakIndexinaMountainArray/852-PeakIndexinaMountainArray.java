// Last updated: 6/24/2025, 12:41:44 AM
class Solution {
    public int peakIndexInMountainArray(int[] nums) {
      for(int i=1;i<nums.length-1;i++){
        if(nums[i]>nums[i-1]&&nums[i]>nums[i+1])
        return i;
      } 
      return -1; 
    }
}