# LCP 14. 切分数组

## 题目描述

<p>给定一个整数数组 <code>nums</code> ，小李想将 <code>nums</code> 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>nums = [2,3,3,2,3,3]</code></p>

<p>输出：<code>2</code></p>

<p>解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>nums = [2,3,5,7]</code></p>

<p>输出：<code>4</code></p>

<p>解释：只有一种可行的切割：[2], [3], [5], [7]</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10^6</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 数论

## 示例

```
[2,3,3,2,3,3]
[2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int splitArray(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int splitArray(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def splitArray(self, nums: List[int]) -> int:
```

### C

```c


int splitArray(int* nums, int numsSize){

}

```

### C#

```csharp
public class Solution {
    public int SplitArray(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var splitArray = function(nums) {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function splitArray($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func splitArray(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitArray(nums: IntArray): Int {

    }
}
```

### Go

```golang
func splitArray(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def split_array(nums)

end
```

### Scala

```scala
object Solution {
    def splitArray(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_array(nums: Vec<i32>) -> i32 {

    }
}
```

