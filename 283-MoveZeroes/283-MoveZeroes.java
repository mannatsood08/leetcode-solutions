// Last updated: 7/4/2025, 4:58:14 PM
class Solution {
    static {
        for(int i = 0; i < 1000; i++){
            moveZeroes(new int[] {0,0});
        }
    }
    public static void moveZeroes(int[] arr) {
        int count = 0;

        for(int i=0; i<arr.length; i++){
            if(arr[i] != 0){
                int temp = arr[i];
                arr[i] = 0;
                arr[count++] = temp;
               
            }
        }
    }
}