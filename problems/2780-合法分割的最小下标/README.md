# 2780. 合法分割的最小下标

## 题目描述

<p>如果在长度为 <code>m</code>&nbsp;的整数数组 <code>arr</code>&nbsp;中 <strong>超过一半</strong> 的元素值为&nbsp;<code>x</code>，那么我们称 <code>x</code>&nbsp;是 <strong>支配元素</strong>&nbsp;。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;，数据保证它含有一个 <strong>支配</strong> 元素。</p>

<p>你需要在下标 <code>i</code>&nbsp;处将&nbsp;<code>nums</code>&nbsp;分割成两个数组&nbsp;<code>nums[0, ..., i]</code> 和&nbsp;<code>nums[i + 1, ..., n - 1]</code>&nbsp;，如果一个分割满足以下条件，我们称它是&nbsp;<strong>合法</strong>&nbsp;的：</p>

<ul>
	<li><code>0 &lt;= i &lt; n - 1</code></li>
	<li><code>nums[0, ..., i]</code>&nbsp;和&nbsp;<code>nums[i + 1, ..., n - 1]</code>&nbsp;的支配元素相同。</li>
</ul>

<p>这里，&nbsp;<code>nums[i, ..., j]</code>&nbsp;表示 <code>nums</code>&nbsp;的一个子数组，它开始于下标&nbsp;<code>i</code>&nbsp;，结束于下标&nbsp;<code>j</code>&nbsp;，两个端点都包含在子数组内。特别地，如果&nbsp;<code>j &lt; i</code>&nbsp;，那么&nbsp;<code>nums[i, ..., j]</code>&nbsp;表示一个空数组。</p>

<p>请你返回一个 <strong>合法分割</strong>&nbsp;的 <strong>最小</strong>&nbsp;下标。如果合法分割不存在，返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,2,2]
<b>输出：</b>2
<b>解释：</b>我们将数组在下标 2 处分割，得到 [1,2,2] 和 [2] 。
数组 [1,2,2] 中，元素 2 是支配元素，因为它在数组中出现了 2 次，且 2 * 2 &gt; 3 。
数组 [2] 中，元素 2 是支配元素，因为它在数组中出现了 1 次，且 1 * 2 &gt; 1 。
两个数组 [1,2,2] 和 [2] 都有与 nums 一样的支配元素，所以这是一个合法分割。
下标 2 是合法分割中的最小下标。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,3,1,1,1,7,1,2,1]
<b>输出：</b>4
<b>解释：</b>我们将数组在下标 4 处分割，得到 [2,1,3,1,1] 和 [1,7,1,2,1] 。
数组 [2,1,3,1,1] 中，元素 1 是支配元素，因为它在数组中出现了 3 次，且 3 * 2 &gt; 5 。
数组 [1,7,1,2,1] 中，元素 1 是支配元素，因为它在数组中出现了 3 次，且 3 * 2 &gt; 5 。
两个数组 [2,1,3,1,1] 和 [1,7,1,2,1] 都有与 nums 一样的支配元素，所以这是一个合法分割。
下标 4 是所有合法分割中的最小下标。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [3,3,3,3,7,2,2]
<b>输出：</b>-1
<b>解释：</b>没有合法分割。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code>&nbsp;有且只有一个支配元素。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. Find the dominant element of nums by using a hashmap to maintain element frequency, we denote the dominant element as x and its frequency as f.
2. For each index in [0, n - 2], calculate f1, x’s frequency in the subarray [0, i] when looping the index. And f2, x’s frequency in the subarray [i + 1, n - 1] which is equal to f - f1. Then we can check whether x is dominant in both subarrays.

## 示例

```
[1,2,2,2]
[2,1,3,1,1,1,7,1,2,1]
[3,3,3,3,7,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumIndex(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumIndex(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumIndex(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumIndex = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumIndex(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumIndex($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumIndex(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumIndex(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumIndex(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumIndex(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_index(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumIndex(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-index nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_index(Nums :: [integer()]) -> integer().
minimum_index(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_index(nums :: [integer]) :: integer
  def minimum_index(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumIndex(nums: ArrayList<Int64>): Int64 {

    }
}
```

