# 2449. 使数组相似的最少操作次数

## 题目描述

<p>给你两个正整数数组&nbsp;<code>nums</code> 和&nbsp;<code>target</code>&nbsp;，两个数组长度相等。</p>

<p>在一次操作中，你可以选择两个 <strong>不同</strong>&nbsp;的下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，其中&nbsp;<code>0 &lt;= i, j &lt; nums.length</code>&nbsp;，并且：</p>

<ul>
	<li>令&nbsp;<code>nums[i] = nums[i] + 2</code>&nbsp;且</li>
	<li>令&nbsp;<code>nums[j] = nums[j] - 2</code>&nbsp;。</li>
</ul>

<p>如果两个数组中每个元素出现的频率相等，我们称两个数组是 <strong>相似</strong>&nbsp;的。</p>

<p>请你返回将 <code>nums</code>&nbsp;变得与 <code>target</code>&nbsp;相似的最少操作次数。测试数据保证 <code>nums</code>&nbsp;一定能变得与 <code>target</code>&nbsp;相似。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [8,12,6], target = [2,14,10]
<b>输出：</b>2
<b>解释：</b>可以用两步操作将 nums 变得与 target 相似：
- 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。
- 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。
2 次操作是最少需要的操作次数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,5], target = [4,1,3]
<b>输出：</b>1
<b>解释：</b>一步操作可以使 nums 变得与 target 相似：
- 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,1,1,1,1], target = [1,1,1,1,1]
<b>输出：</b>0
<b>解释：</b>数组 nums 已经与 target 相似。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], target[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>nums</code>&nbsp;一定可以变得与&nbsp;<code>target</code> 相似。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Solve for even and odd numbers separately.
2. Greedily match smallest even element from nums to smallest even element from target, then similarly next smallest element and so on.
3. Similarly, match odd elements too.

## 示例

```
[8,12,6]
[2,14,10]
[1,2,5]
[4,1,3]
[1,1,1,1,1]
[1,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long makeSimilar(vector<int>& nums, vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public long makeSimilar(int[] nums, int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeSimilar(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
```

### C

```c
long long makeSimilar(int* nums, int numsSize, int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MakeSimilar(int[] nums, int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} target
 * @return {number}
 */
var makeSimilar = function(nums, target) {
    
};
```

### TypeScript

```typescript
function makeSimilar(nums: number[], target: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $target
     * @return Integer
     */
    function makeSimilar($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeSimilar(_ nums: [Int], _ target: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeSimilar(nums: IntArray, target: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeSimilar(List<int> nums, List<int> target) {
    
  }
}
```

### Go

```golang
func makeSimilar(nums []int, target []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def make_similar(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def makeSimilar(nums: Array[Int], target: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_similar(nums: Vec<i32>, target: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (make-similar nums target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec make_similar(Nums :: [integer()], Target :: [integer()]) -> integer().
make_similar(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_similar(nums :: [integer], target :: [integer]) :: integer
  def make_similar(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeSimilar(nums: Array<Int64>, target: Array<Int64>): Int64 {

    }
}
```

