// Last updated: 6/24/2025, 7:13:38 PM
class Solution {
    public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;

    int write = 0;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] != nums[write]) {
            write++;
            nums[write] = nums[i];
        }
    }
    return write + 1;
}

    }
