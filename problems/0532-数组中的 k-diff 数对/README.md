# 532. 数组中的 k-diff 数对

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 和一个整数&nbsp;<code>k</code>，请你在数组中找出<strong> 不同的&nbsp;</strong>k-diff 数对，并返回不同的 <strong>k-diff 数对</strong> 的数目。</p>

<p><strong>k-diff</strong>&nbsp;数对定义为一个整数对 <code>(nums[i], nums[j])</code><strong> </strong>，并满足下述全部条件：</p>

<ul>
	<li><code>0 &lt;= i, j &lt; nums.length</code></li>
	<li><code>i != j</code></li>
	<li><code>|nums[i] - nums[j]| == k</code></li>
</ul>

<p><strong>注意</strong>，<code>|val|</code> 表示 <code>val</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3, 1, 4, 1, 5], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1, 2, 3, 4, 5], k = 1
<strong>输出：</strong>4
<strong>解释：</strong>数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1, 3, 1, 5, 4], k = 0
<strong>输出：</strong>1
<strong>解释：</strong>数组中只有一个 0-diff 数对，(1, 1) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 二分查找
- 排序

## 示例

```
[3,1,4,1,5]
2
[1,2,3,4,5]
1
[1,3,1,5,4]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findPairs(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int findPairs(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindPairs(int[] nums, int k) {
        
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
var findPairs = function(nums, k) {
    
};
```

### TypeScript

```typescript
function findPairs(nums: number[], k: number): number {
    
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
    function findPairs($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPairs(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPairs(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findPairs(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func findPairs(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_pairs(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def findPairs(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_pairs(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_pairs(Nums :: [integer()], K :: integer()) -> integer().
find_pairs(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_pairs(nums :: [integer], k :: integer) :: integer
  def find_pairs(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPairs(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

