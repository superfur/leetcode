# LCR 068. 搜索插入位置

## 题目描述

<p>给定一个排序的整数数组 <code>nums</code>&nbsp;和一个整数目标值<code> target</code> ，请在数组中找到&nbsp;<code>target&nbsp;</code>，并返回其下标。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。</p>

<p>请必须使用时间复杂度为 <code>O(log n)</code> 的算法。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 5
<strong>输出:</strong> 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 2
<strong>输出:</strong> 1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 7
<strong>输出:</strong> 4
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 0
<strong>输出:</strong> 0
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入:</strong> nums = [1], target = 0
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 为<strong>无重复元素</strong>的<strong>升序</strong>排列数组</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 35&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/search-insert-position/">https://leetcode-cn.com/problems/search-insert-position/</a></p>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 示例

```
[1,3,5,6]
5
[1,3,5,6]
2
[1,3,5,6]
7
[1,3,5,6]
0
[1]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

    }
};
```

### Java

```java
class Solution {
    public int searchInsert(int[] nums, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
```

### C

```c


int searchInsert(int* nums, int numsSize, int target){

}
```

### C#

```csharp
public class Solution {
    public int SearchInsert(int[] nums, int target) {

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
var searchInsert = function(nums, target) {

};
```

### TypeScript

```typescript
function searchInsert(nums: number[], target: number): number {

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
    function searchInsert($nums, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {

    }
}
```

### Go

```golang
func searchInsert(nums []int, target int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)

end
```

### Scala

```scala
object Solution {
    def searchInsert(nums: Array[Int], target: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (search-insert nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec search_insert(Nums :: [integer()], Target :: integer()) -> integer().
search_insert(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec search_insert(nums :: [integer], target :: integer) :: integer
  def search_insert(nums, target) do

  end
end
```

