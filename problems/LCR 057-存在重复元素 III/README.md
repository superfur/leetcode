# LCR 057. 存在重复元素 III

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和两个整数&nbsp;<code>k</code> 和 <code>t</code> 。请你判断是否存在 <b>两个不同下标</b> <code>i</code> 和 <code>j</code>，使得&nbsp;<code>abs(nums[i] - nums[j]) &lt;= t</code> ，同时又满足 <code>abs(i - j) &lt;= k</code><em> </em>。</p>

<p>如果存在则返回 <code>true</code>，不存在返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1], k<em> </em>= 3, t = 0
<strong>输出：</strong>true</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,1], k<em> </em>=<em> </em>1, t = 2
<strong>输出：</strong>true</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,9,1,5,9], k = 2, t = 3
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= t &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 220&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/contains-duplicate-iii/">https://leetcode-cn.com/problems/contains-duplicate-iii/</a></p>


## 难度

Medium

## 标签

- 数组
- 桶排序
- 有序集合
- 排序
- 滑动窗口

## 示例

```
[1,2,3,1]
3
0
[1,0,1,1]
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {

    }
};
```

### Java

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {

    }
}
```

### Python

```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
```

### Python3

```python3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
```

### C

```c


bool containsNearbyAlmostDuplicate(int* nums, int numsSize, int k, int t){

}
```

### C#

```csharp
public class Solution {
    public bool ContainsNearbyAlmostDuplicate(int[] nums, int k, int t) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} t
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, k, t) {

};
```

### TypeScript

```typescript
function containsNearbyAlmostDuplicate(nums: number[], k: number, t: number): boolean {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $t
     * @return Boolean
     */
    function containsNearbyAlmostDuplicate($nums, $k, $t) {

    }
}
```

### Swift

```swift
class Solution {
    func containsNearbyAlmostDuplicate(_ nums: [Int], _ k: Int, _ t: Int) -> Bool {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun containsNearbyAlmostDuplicate(nums: IntArray, k: Int, t: Int): Boolean {

    }
}
```

### Go

```golang
func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} t
# @return {Boolean}
def contains_nearby_almost_duplicate(nums, k, t)

end
```

### Scala

```scala
object Solution {
    def containsNearbyAlmostDuplicate(nums: Array[Int], k: Int, t: Int): Boolean = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn contains_nearby_almost_duplicate(nums: Vec<i32>, k: i32, t: i32) -> bool {

    }
}
```

### Racket

```racket
(define/contract (contains-nearby-almost-duplicate nums k t)
  (-> (listof exact-integer?) exact-integer? exact-integer? boolean?)

  )
```

### Erlang

```erlang
-spec contains_nearby_almost_duplicate(Nums :: [integer()], K :: integer(), T :: integer()) -> boolean().
contains_nearby_almost_duplicate(Nums, K, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec contains_nearby_almost_duplicate(nums :: [integer], k :: integer, t :: integer) :: boolean
  def contains_nearby_almost_duplicate(nums, k, t) do

  end
end
```

