function mySqrt(x: number): number {
    if (x < 2) return x;
    let left = 1, right = Math.floor(x / 2);
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const sq = mid * mid;
        if (sq === x) return mid;
        else if (sq < x) left = mid + 1;
        else right = mid - 1;
    }
    return right;
}

export default mySqrt;
