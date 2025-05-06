function threeSum(nums) {
    if(!nums.length) return;
    let result =[]
    nums = nums.sort((a,b)=> a-b)
    for(let i=0; i<nums.length-2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        let j=i+1;
        let k=nums.length-1;

        while(j<k) {
            let sum = nums[j]+nums[k];            
            if(-nums[i] == sum) {
                result.push([nums[i],nums[j],nums[k]]);
                j++;
                k--;

                while (j < nums.length && nums[j] === nums[j - 1]) j++;
                while (k > j && nums[k] === nums[k + 1]) k--;
            }
            else if(-nums[i] < sum) k--;
            else j++;
        }
    }
    return result;
};

console.log(threeSum([-1,0,1,2,-1,-4]))