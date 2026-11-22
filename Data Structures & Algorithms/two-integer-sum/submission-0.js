class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
  const result = [];
  const numsVisited = {};

  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];

    if (numsVisited[complement] !== undefined) {
      result.push(numsVisited[complement]);
      result.push(i);
    }
    numsVisited[nums[i]] = i;
  }
  return result;
    }
}
