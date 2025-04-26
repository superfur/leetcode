# 3092. 最高频率的 ID

## 题目描述

<p>你需要在一个集合里动态记录 ID 的出现频率。给你两个长度都为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code> 和&nbsp;<code>freq</code>&nbsp;，<code>nums</code>&nbsp;中每一个元素表示一个 ID ，对应的 <code>freq</code>&nbsp;中的元素表示这个 ID 在集合中此次操作后需要增加或者减少的数目。</p>

<ul>
	<li><strong>增加 ID 的数目：</strong>如果&nbsp;<code>freq[i]</code>&nbsp;是正数，那么&nbsp;<code>freq[i]</code>&nbsp;个 ID 为&nbsp;<code>nums[i]</code>&nbsp;的元素在第 <code>i</code>&nbsp;步操作后会添加到集合中。</li>
	<li><strong>减少 ID 的数目：</strong>如果&nbsp;<code>freq[i]</code>&nbsp;是负数，那么&nbsp;<code>-freq[i]</code>&nbsp;个 ID 为&nbsp;<code>nums[i]</code>&nbsp;的元素在第 <code>i</code>&nbsp;步操作后会从集合中删除。</li>
</ul>

<p>请你返回一个长度为 <code>n</code>&nbsp;的数组 <code>ans</code>&nbsp;，其中&nbsp;<code>ans[i]</code>&nbsp;表示第 <code>i</code>&nbsp;步操作后出现频率最高的 ID <strong>数目</strong>&nbsp;，如果在某次操作后集合为空，那么 <code>ans[i]</code>&nbsp;为 0 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,3,2,1], freq = [3,2,-3,1]</span></p>

<p><span class="example-io"><b>输出：</b>[3,3,2,2]</span></p>

<p><strong>解释：</strong></p>

<p>第 0 步操作后，有 3 个 ID 为 2 的元素，所以&nbsp;<code>ans[0] = 3</code>&nbsp;。<br />
第 1 步操作后，有 3 个 ID 为 2 的元素和 2 个 ID 为 3 的元素，所以&nbsp;<code>ans[1] = 3</code>&nbsp;。<br />
第 2 步操作后，有 2 个 ID 为 3 的元素，所以&nbsp;<code>ans[2] = 2</code>&nbsp;。<br />
第 3 步操作后，有 2 个 ID 为 3 的元素和 1 个 ID 为 1 的元素，所以&nbsp;<code>ans[3] = 2</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [5,5,3], freq = [2,-2,1]</span></p>

<p><span class="example-io"><b>输出：</b>[2,0,1]</span></p>

<p><strong>解释：</strong></p>

<p>第 0 步操作后，有 2 个 ID 为 5 的元素，所以&nbsp;<code>ans[0] = 2</code>&nbsp;。<br />
第 1 步操作后，集合中没有任何元素，所以&nbsp;<code>ans[1] = 0</code>&nbsp;。<br />
第 2 步操作后，有 1 个 ID 为 3 的元素，所以&nbsp;<code>ans[2] = 1</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == freq.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= freq[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>freq[i] != 0</code></li>
	<li>输入保证任何操作后，集合中的元素出现次数不会为负数。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 有序集合
- 堆（优先队列）

## 提示

1. Use an ordered set for maintaining the occurrences of each ID.
2. After step <code>i</code> find the occurrences of <code>nums[i]</code>.
3. Change the occurrences of <code>nums[i]</code> in the ordered set.

## 示例

```
[2,3,2,1]
[3,2,-3,1]
[5,5,3]
[2,-2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> mostFrequentIDs(vector<int>& nums, vector<int>& freq) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* mostFrequentIDs(int* nums, int numsSize, int* freq, int freqSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] MostFrequentIDs(int[] nums, int[] freq) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} freq
 * @return {number[]}
 */
var mostFrequentIDs = function(nums, freq) {
    
};
```

### TypeScript

```typescript
function mostFrequentIDs(nums: number[], freq: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $freq
     * @return Integer[]
     */
    function mostFrequentIDs($nums, $freq) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostFrequentIDs(_ nums: [Int], _ freq: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostFrequentIDs(nums: IntArray, freq: IntArray): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> mostFrequentIDs(List<int> nums, List<int> freq) {
    
  }
}
```

### Go

```golang
func mostFrequentIDs(nums []int, freq []int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} freq
# @return {Integer[]}
def most_frequent_i_ds(nums, freq)
    
end
```

### Scala

```scala
object Solution {
    def mostFrequentIDs(nums: Array[Int], freq: Array[Int]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_frequent_i_ds(nums: Vec<i32>, freq: Vec<i32>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (most-frequent-i-ds nums freq)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec most_frequent_i_ds(Nums :: [integer()], Freq :: [integer()]) -> [integer()].
most_frequent_i_ds(Nums, Freq) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_frequent_i_ds(nums :: [integer], freq :: [integer]) :: [integer]
  def most_frequent_i_ds(nums, freq) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostFrequentIDs(nums: Array<Int64>, freq: Array<Int64>): Array<Int64> {

    }
}
```

