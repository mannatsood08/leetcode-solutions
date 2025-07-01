// Last updated: 7/1/2025, 12:48:08 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        int write=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=nums[write]){
            write++;
            nums[write]=nums[i];
            }
        }
        return write+1;
    }
}