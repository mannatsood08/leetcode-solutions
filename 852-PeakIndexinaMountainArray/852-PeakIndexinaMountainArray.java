// Last updated: 6/24/2025, 1:02:02 AM
class Solution {
    public int peakIndexInMountainArray(int[] nums) {
        int start=0;
        int end=nums.length-1;
        while(start<end){
            int middle=start+(end-start)/2;
            if(nums[middle]>nums[middle+1])
            end=middle;
            else
            start=middle+1;
        }
        return start;

    }
}