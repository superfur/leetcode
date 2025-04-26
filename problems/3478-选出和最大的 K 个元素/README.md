# 3478. 选出和最大的 K 个元素

## 题目描述

<p>给你两个整数数组，<code>nums1</code> 和 <code>nums2</code>，长度均为 <code>n</code>，以及一个正整数 <code>k</code> 。</p>

<p>对从 <code>0</code> 到 <code>n - 1</code> 每个下标 <code>i</code> ，执行下述操作：</p>

<ul>
	<li>找出所有满足 <code>nums1[j]</code> 小于 <code>nums1[i]</code> 的下标 <code>j</code> 。</li>
	<li>从这些下标对应的 <code>nums2[j]</code> 中选出 <strong>至多</strong> <code>k</code> 个，并 <strong>最大化</strong> 这些值的总和作为结果。</li>
</ul>

<p>返回一个长度为 <code>n</code> 的数组 <code>answer</code> ，其中 <code>answer[i]</code> 表示对应下标 <code>i</code> 的结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">[80,30,0,80,50]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>i = 0</code> ：满足 <code>nums1[j] &lt; nums1[0]</code> 的下标为 <code>[1, 2, 4]</code> ，选出其中值最大的两个，结果为 <code>50 + 30 = 80</code> 。</li>
	<li>对于 <code>i = 1</code> ：满足 <code>nums1[j] &lt; nums1[1]</code> 的下标为 <code>[2]</code> ，只能选择这个值，结果为 <code>30</code> 。</li>
	<li>对于 <code>i = 2</code> ：不存在满足 <code>nums1[j] &lt; nums1[2]</code> 的下标，结果为 <code>0</code> 。</li>
	<li>对于 <code>i = 3</code> ：满足 <code>nums1[j] &lt; nums1[3]</code> 的下标为 <code>[0, 1, 2, 4]</code> ，选出其中值最大的两个，结果为 <code>50 + 30 = 80</code> 。</li>
	<li>对于 <code>i = 4</code> ：满足 <code>nums1[j] &lt; nums1[4]</code> 的下标为 <code>[1, 2]</code> ，选出其中值最大的两个，结果为 <code>30 + 20 = 50</code> 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">[0,0,0,0]</span></p>

<p><strong>解释：</strong>由于 <code>nums1</code> 中的所有元素相等，不存在满足条件 <code>nums1[j] &lt; nums1[i]</code>，所有位置的结果都是 0 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序
- 堆（优先队列）

## 提示

1. Sort <code>nums1</code> and its corresponding <code>nums2</code> values together based on <code>nums1</code>.
2. Use a max heap to track the top <code>k</code> values of <code>nums2</code> as you process each element in the sorted order.

## 示例

```
[4,2,1,5,3]
[10,20,30,40,50]
2
[2,2,2,2]
[3,1,2,3]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] findMaxSum(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* findMaxSum(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] FindMaxSum(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[]}
 */
var findMaxSum = function(nums1, nums2, k) {
    
};
```

### TypeScript

```typescript
function findMaxSum(nums1: number[], nums2: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[]
     */
    function findMaxSum($nums1, $nums2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxSum(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxSum(nums1: IntArray, nums2: IntArray, k: Int): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findMaxSum(List<int> nums1, List<int> nums2, int k) {
    
  }
}
```

### Go

```golang
func findMaxSum(nums1 []int, nums2 []int, k int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[]}
def find_max_sum(nums1, nums2, k)
    
end
```

### Scala

```scala
object Solution {
    def findMaxSum(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_sum(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-sum nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_max_sum(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> [integer()].
find_max_sum(Nums1, Nums2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_sum(nums1 :: [integer], nums2 :: [integer], k :: integer) :: [integer]
  def find_max_sum(nums1, nums2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxSum(nums1: Array<Int64>, nums2: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

