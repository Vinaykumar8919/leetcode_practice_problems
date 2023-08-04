
// time o(n) space o(n)
class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> set = new HashSet();
        for(int num : nums) {
            set.add(num);
        }
        int i=1;
        while(set.contains(i)) {
            i++;
        }
        return i;

        
    }
}

// time o(n) space o(1)
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        for(int i=0; i<n; i++) {
            if(nums[i]>n || nums[i]<=0) {
                nums[i]=n+1;
            }
        }

        for(int i=0; i<n; i++) {
            int id = Math.abs(nums[i]);
            if(id>n) 
                continue;
            id--;
            if(nums[id]>0) 
                nums[id]=-nums[id];
        }
        int i;
        for(i=0; i<n; i++) {
            if(nums[i]>0) {
                return i+1;
            }
        }
        return n+1;
        
    }
}
