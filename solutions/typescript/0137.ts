/**
 * 137. 只出现一次的数字 II
 * 逐位统计：出现三次的数，每一位上的 1 的个数一定是 3 的倍数，
 * 所以把所有数在第 i 位上的 1 加起来对 3 取模，余数就是答案在第 i 位的值。
 * JS 的位运算本身就是 32 位有符号整数：x >> i 是算术右移，1 << 31 是负数，
 * 所以负数和符号位不需要额外处理。时间 O(32n)，空间 O(1)。
 */
function singleNumber(nums: number[]): number {
    let result = 0;
    for (let i = 0; i < 32; i++) {
        let ones = 0;
        for (const x of nums) {
            ones += (x >> i) & 1;
        }
        if (ones % 3 !== 0) {
            result |= 1 << i;
        }
    }
    return result;
}

export default singleNumber;
