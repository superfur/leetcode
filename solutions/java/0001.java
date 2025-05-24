// /**
//  * 两数之和
//  * @param nums 整数数组
//  * @param target 目标值
//  * @returns 两个数的索引
//  */
// function twoSum(nums: number[], target: number): number[] {
//   const map = new Map<number, number>();

//   for (let i = 0; i < nums.length; i++) {
//     const complement = target - nums[i];
//     if (map.has(complement)) {
//       return [map.get(complement)!, i];
//     }
//     map.set(nums[i], i);
//   }

//   return [];
// }

// export default twoSum;
