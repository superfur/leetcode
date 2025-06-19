func maxArea(height []int) int {
    left := 0
    right := len(height) - 1
    maxWater := 0

    for left < right {
        width := right - left
        h := min(height[left], height[right])
        currentWater := width * h
        maxWater = max(maxWater, currentWater)

        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }

    return maxWater
}