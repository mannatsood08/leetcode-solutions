// Last updated: 7/5/2025, 9:46:07 PM
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // handle k > n
        int[] temp = new int[k];

        // Step 1: Copy last k elements to temp
        for (int i = 0; i < k; i++) {
            temp[i] = nums[n - k + i];
        }

        // Step 2: Shift the first (n - k) elements to the right
        for (int i = n - 1; i >= k; i--) {
            nums[i] = nums[i - k];
        }

        // Step 3: Copy temp to the beginning
        for (int i = 0; i < k; i++) {
            nums[i] = temp[i];
        }
    }
}
