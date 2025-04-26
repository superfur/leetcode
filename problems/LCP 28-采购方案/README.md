# LCP 28. 采购方案

## 题目描述

小力将 N 个零件的报价存于数组 `nums`。小力预算为 `target`，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`


**示例 1：**
>输入：`nums = [2,5,3,5], target = 6`
>
>输出：`1`
>
>解释：预算内仅能购买 nums[0] 与 nums[2]。

**示例 2：**
>输入：`nums = [2,2,1,9], target = 10`
>
>输出：`4`
>
>解释：符合预算的采购方案如下：
>nums[0] + nums[1] = 4
>nums[0] + nums[2] = 3
>nums[1] + nums[2] = 3
>nums[2] + nums[3] = 10

**提示：**
- `2 <= nums.length <= 10^5`
- `1 <= nums[i], target <= 10^5`


## 难度

Easy

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 示例

```
[2,5,3,5]
6
[2,2,1,9]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {

    }
};
```

### Java

```java
class Solution {
    public int purchasePlans(int[] nums, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
```

### C

```c


int purchasePlans(int* nums, int numsSize, int target){

}
```

### C#

```csharp
public class Solution {
    public int PurchasePlans(int[] nums, int target) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var purchasePlans = function(nums, target) {

};
```

### TypeScript

```typescript
function purchasePlans(nums: number[], target: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function purchasePlans($nums, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func purchasePlans(_ nums: [Int], _ target: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun purchasePlans(nums: IntArray, target: Int): Int {

    }
}
```

### Go

```golang
func purchasePlans(nums []int, target int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def purchase_plans(nums, target)

end
```

### Scala

```scala
object Solution {
    def purchasePlans(nums: Array[Int], target: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn purchase_plans(nums: Vec<i32>, target: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (purchase-plans nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

