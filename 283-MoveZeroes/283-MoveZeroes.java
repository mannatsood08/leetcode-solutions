// Last updated: 7/4/2025, 4:56:53 PM
class Solution {
    public void moveZeroes(int[] nums) {
        int c = 0; // Pointer to place next non-zero element
        
        // Step 1: Move all non-zero elements to the front
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[c] = nums[i];
                c++;
            }
        }
        
        // Step 2: Fill remaining positions with 0
        for (int i = c; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
