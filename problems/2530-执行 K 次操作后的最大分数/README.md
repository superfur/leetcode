# 2530. 执行 K 次操作后的最大分数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>k</code> 。你的 <strong>起始分数</strong> 为 <code>0</code> 。</p>

<p>在一步 <strong>操作</strong> 中：</p>

<ol>
	<li>选出一个满足 <code>0 &lt;= i &lt; nums.length</code> 的下标 <code>i</code> ，</li>
	<li>将你的 <strong>分数</strong> 增加 <code>nums[i]</code> ，并且</li>
	<li>将 <code>nums[i]</code> 替换为 <code>ceil(nums[i] / 3)</code> 。</li>
</ol>

<p>返回在 <strong>恰好</strong> 执行 <code>k</code> 次操作后，你可能获得的最大分数。</p>

<p>向上取整函数 <code>ceil(val)</code> 的结果是大于或等于 <code>val</code> 的最小整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,10,10,10,10], k = 5
<strong>输出：</strong>50
<strong>解释：</strong>对数组中每个元素执行一次操作。最后分数是 10 + 10 + 10 + 10 + 10 = 50 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,10,3,3,3], k = 3
<strong>输出：</strong>17
<strong>解释：</strong>可以执行下述操作：
第 1 步操作：选中 i = 1 ，nums 变为 [1,<em><strong>4</strong></em>,3,3,3] 。分数增加 10 。
第 2 步操作：选中 i = 1 ，nums 变为 [1,<em><strong>2</strong></em>,3,3,3] 。分数增加 4 。
第 3 步操作：选中 i = 2 ，nums 变为 [1,2,<em><strong>1</strong></em>,3,3] 。分数增加 3 。
最后分数是 10 + 4 + 3 = 17 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, k &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. It is always optimal to select the greatest element in the array.
2. Use a heap to query for the maximum in O(log n) time.

## 示例

```
[10,10,10,10,10]
5
[1,10,3,3,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxKelements(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long maxKelements(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxKelements(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxKelements = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxKelements(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxKelements($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxKelements(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxKelements(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxKelements(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxKelements(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_kelements(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxKelements(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-kelements nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_kelements(Nums :: [integer()], K :: integer()) -> integer().
max_kelements(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_kelements(nums :: [integer], k :: integer) :: integer
  def max_kelements(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxKelements(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

