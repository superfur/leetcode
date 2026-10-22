/**
 * 134. 加油站
 * 贪心一趟扫描：
 * - total 累加所有 gas[i] - cost[i]，total < 0 说明总油量不够绕一圈，直接 -1；
 * - tank 是从当前候选起点出发的油箱余量，一旦变负，说明从候选起点到 i 的任何一站
 *   出发都走不到 i + 1，于是候选起点改成 i + 1，tank 清零。
 * 扫完后 total >= 0，则最后的候选起点就是唯一解。
 */
function canCompleteCircuit(gas: number[], cost: number[]): number {
    let total = 0;
    let tank = 0;
    let start = 0;
    for (let i = 0; i < gas.length; i++) {
        const diff = gas[i] - cost[i];
        total += diff;
        tank += diff;
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }
    return total >= 0 ? start : -1;
}

export default canCompleteCircuit;
