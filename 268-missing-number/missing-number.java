class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int summ = (n * (n+1))/2;
        int act_sum = 0;

        for( int i = 0; i < n; i++){
            act_sum += nums[i];
        }

        return(summ - act_sum);
    }
}