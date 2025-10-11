class Solution {
    public int maxOperations(int[] nums, int k) {
        int a = 0;
        int b = nums.length -1;
        Arrays.sort(nums);
        int count = 0;
        while (a < b){
            if ((nums[a] + nums[b]) == k){
                count +=1;
                a +=1;
                b -= 1;
            }
            else if( ((nums[a] + nums[b]) > k)){
                b-=1;
            }
            else{
                a+=1;
            }
        }
            return (count);
    }
}