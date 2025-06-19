function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    // 计算当前容器的水量
    const width = right - left;
    const h = Math.min(height[left], height[right]);
    const currentWater = width * h;

    // 更新最大水量
    maxWater = Math.max(maxWater, currentWater);

    // 移动较短的线，因为较长的线可能与其他线形成更大的容器
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
}
