class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    const mySet = new Set();
    for (let x of nums) {
    if (mySet.has(x)) {
      return true;
    }
    mySet.add(x);
  }
  return false;

    }
}
