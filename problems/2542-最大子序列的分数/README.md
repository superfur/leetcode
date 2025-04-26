# 2542. 最大子序列的分数

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，两者长度都是&nbsp;<code>n</code>&nbsp;，再给你一个正整数&nbsp;<code>k</code>&nbsp;。你必须从&nbsp;<code>nums1</code>&nbsp;中选一个长度为 <code>k</code>&nbsp;的 <strong>子序列</strong>&nbsp;对应的下标。</p>

<p>对于选择的下标&nbsp;<code>i<sub>0</sub></code>&nbsp;，<code>i<sub>1</sub></code>&nbsp;，...，&nbsp;<code>i<sub>k - 1</sub></code>&nbsp;，你的&nbsp;<strong>分数</strong>&nbsp;定义如下：</p>

<ul>
	<li><code>nums1</code>&nbsp;中下标对应元素求和，乘以&nbsp;<code>nums2</code>&nbsp;中下标对应元素的&nbsp;<strong>最小值</strong>&nbsp;。</li>
	<li>用公式表示：&nbsp;<code>(nums1[i<sub>0</sub>] + nums1[i<sub>1</sub>] +...+ nums1[i<sub>k - 1</sub>]) * min(nums2[i<sub>0</sub>] , nums2[i<sub>1</sub>], ... ,nums2[i<sub>k - 1</sub>])</code>&nbsp;。</li>
</ul>

<p>请你返回 <strong>最大</strong>&nbsp;可能的分数。</p>

<p>一个数组的 <strong>子序列</strong>&nbsp;下标是集合&nbsp;<code>{0, 1, ..., n-1}</code>&nbsp;中删除若干元素得到的剩余集合，也可以不删除任何元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
<b>输出：</b>12
<b>解释：</b>
四个可能的子序列分数为：
- 选择下标 0 ，1 和 2 ，得到分数 (1+3+3) * min(2,1,3) = 7 。
- 选择下标 0 ，1 和 3 ，得到分数 (1+3+2) * min(2,1,4) = 6 。
- 选择下标 0 ，2 和 3 ，得到分数 (1+3+2) * min(2,3,4) = 12 。
- 选择下标 1 ，2 和 3 ，得到分数 (3+3+2) * min(1,3,4) = 8 。
所以最大分数为 12 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
<b>输出：</b>30
<b>解释：</b>
选择下标 2 最优：nums1[2] * nums2[2] = 3 * 10 = 30 是最大可能分数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[j] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. How can we use sorting here?
2. Try sorting the two arrays based on second array.
3. Loop through nums2 and compute the max product given the minimum is nums2[i]. Update the answer accordingly.

## 示例

```
[1,3,3,2]
[2,1,3,4]
3
[4,2,3,1,1]
[7,5,10,9,6]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
```

### C

```c
long long maxScore(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxScore(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var maxScore = function(nums1, nums2, k) {
    
};
```

### TypeScript

```typescript
function maxScore(nums1: number[], nums2: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function maxScore($nums1, $nums2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(nums1: IntArray, nums2: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(List<int> nums1, List<int> nums2, int k) {
    
  }
}
```

### Go

```golang
func maxScore(nums1 []int, nums2 []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def max_score(nums1, nums2, k)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
max_score(Nums1, Nums2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def max_score(nums1, nums2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(nums1: Array<Int64>, nums2: Array<Int64>, k: Int64): Int64 {

    }
}
```

