# 220. 存在重复元素 III

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和两个整数 <code>indexDiff</code> 和 <code>valueDiff</code> 。</p>

<p>找出满足下述条件的下标对 <code>(i, j)</code>：</p>

<ul>
	<li><code>i != j</code>,</li>
	<li><code>abs(i - j) &lt;= indexDiff</code></li>
	<li><code>abs(nums[i] - nums[j]) &lt;= valueDiff</code></li>
</ul>

<p>如果存在，返回 <code>true</code><em> ；</em>否则，返回<em> </em><code>false</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
<strong>输出：</strong>true
<strong>解释：</strong>可以找出 (i, j) = (0, 3) 。
满足下述 3 个条件：
i != j --&gt; 0 != 3
abs(i - j) &lt;= indexDiff --&gt; abs(0 - 3) &lt;= 3
abs(nums[i] - nums[j]) &lt;= valueDiff --&gt; abs(1 - 1) &lt;= 0
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
<strong>输出：</strong>false
<strong>解释：</strong>尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= indexDiff &lt;= nums.length</code></li>
	<li><code>0 &lt;= valueDiff &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 桶排序
- 有序集合
- 排序
- 滑动窗口

## 提示

1. Time complexity O(n logk)  - This will give an indication that sorting is involved for k elements.
2. Use already existing state to evaluate next state  -  Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.

## 示例

```
[1,2,3,1]
3
0
[1,5,9,1,5,9]
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        
    }
}
```

### Python

```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
```

### C

```c
bool containsNearbyAlmostDuplicate(int* nums, int numsSize, int indexDiff, int valueDiff) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ContainsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
    
};
```

### TypeScript

```typescript
function containsNearbyAlmostDuplicate(nums: number[], indexDiff: number, valueDiff: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $indexDiff
     * @param Integer $valueDiff
     * @return Boolean
     */
    function containsNearbyAlmostDuplicate($nums, $indexDiff, $valueDiff) {
        
    }
}
```

### Swift

```swift
class Solution {
    func containsNearbyAlmostDuplicate(_ nums: [Int], _ indexDiff: Int, _ valueDiff: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun containsNearbyAlmostDuplicate(nums: IntArray, indexDiff: Int, valueDiff: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool containsNearbyAlmostDuplicate(List<int> nums, int indexDiff, int valueDiff) {
    
  }
}
```

### Go

```golang
func containsNearbyAlmostDuplicate(nums []int, indexDiff int, valueDiff int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} index_diff
# @param {Integer} value_diff
# @return {Boolean}
def contains_nearby_almost_duplicate(nums, index_diff, value_diff)
    
end
```

### Scala

```scala
object Solution {
    def containsNearbyAlmostDuplicate(nums: Array[Int], indexDiff: Int, valueDiff: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn contains_nearby_almost_duplicate(nums: Vec<i32>, index_diff: i32, value_diff: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (contains-nearby-almost-duplicate nums indexDiff valueDiff)
  (-> (listof exact-integer?) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec contains_nearby_almost_duplicate(Nums :: [integer()], IndexDiff :: integer(), ValueDiff :: integer()) -> boolean().
contains_nearby_almost_duplicate(Nums, IndexDiff, ValueDiff) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec contains_nearby_almost_duplicate(nums :: [integer], index_diff :: integer, value_diff :: integer) :: boolean
  def contains_nearby_almost_duplicate(nums, index_diff, value_diff) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func containsNearbyAlmostDuplicate(nums: Array<Int64>, indexDiff: Int64, valueDiff: Int64): Bool {

    }
}
```

