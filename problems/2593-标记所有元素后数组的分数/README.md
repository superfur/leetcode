# 2593. 标记所有元素后数组的分数

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;，它包含若干正整数。</p>

<p>一开始分数&nbsp;<code>score = 0</code>&nbsp;，请你按照下面算法求出最后分数：</p>

<ul>
	<li>从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。</li>
	<li>将选中的整数加到&nbsp;<code>score</code>&nbsp;中。</li>
	<li>标记 <strong>被选中元素</strong>，如果有相邻元素，则同时标记&nbsp;<strong>与它相邻的两个元素</strong>&nbsp;。</li>
	<li>重复此过程直到数组中所有元素都被标记。</li>
</ul>

<p>请你返回执行上述算法后最后的分数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,3,4,5,2]
<b>输出：</b>7
<b>解释：</b>我们按照如下步骤标记元素：
- 1 是最小未标记元素，所以标记它和相邻两个元素：[<u><em><strong>2</strong></em></u>,<u><em><strong>1</strong></em></u>,<u><em><strong>3</strong></em></u>,4,5,2] 。
- 2 是最小未标记元素，所以标记它和左边相邻元素：[<u><em><strong>2</strong></em></u>,<u><em><strong>1</strong></em></u>,<u><em><strong>3</strong></em></u>,4,<u><em><strong>5</strong></em></u>,<u><em><strong>2</strong></em></u>] 。
- 4 是仅剩唯一未标记的元素，所以我们标记它：[<u><em><strong>2</strong></em></u>,<u><em><strong>1</strong></em></u>,<u><em><strong>3</strong></em></u>,<u><em><strong>4</strong></em></u>,<u><em><strong>5</strong></em></u>,<u><em><strong>2</strong></em></u>] 。
总得分为 1 + 2 + 4 = 7 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,5,1,3,2]
<b>输出：</b>5
<b>解释：</b>我们按照如下步骤标记元素：
- 1 是最小未标记元素，所以标记它和相邻两个元素：[2,3,<u><em><strong>5</strong></em></u>,<u><em><strong>1</strong></em></u>,<u><em><strong>3</strong></em></u>,2] 。
- 2 是最小未标记元素，由于有两个 2 ，我们选择最左边的一个 2 ，也就是下标为 0 处的 2 ，以及它右边相邻的元素：[<u><em><strong>2</strong></em></u>,<u><em><strong>3</strong></em></u>,<u><em><strong>5</strong></em></u>,<u><em><strong>1</strong></em></u>,<u><em><strong>3</strong></em></u>,2] 。
- 2 是仅剩唯一未标记的元素，所以我们标记它：[<u><em><strong>2</strong></em></u>,<u><em><strong>3</strong></em></u>,<u><em><strong>5</strong></em></u>,<u><em><strong>1</strong></em></u>,<u><em><strong>3</strong></em></u>,<u><em><strong>2</strong></em></u>] 。
总得分为 1 + 2 + 2 = 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序
- 模拟
- 堆（优先队列）

## 提示

1. Try simulating the process of marking the elements and their adjacent.
2. If there is an element that was already marked, then you skip it.

## 示例

```
[2,1,3,4,5,2]
[2,3,5,1,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long findScore(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long findScore(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findScore(self, nums: List[int]) -> int:
        
```

### C

```c
long long findScore(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long FindScore(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findScore = function(nums) {
    
};
```

### TypeScript

```typescript
function findScore(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findScore($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findScore(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findScore(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int findScore(List<int> nums) {
    
  }
}
```

### Go

```golang
func findScore(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_score(nums)
    
end
```

### Scala

```scala
object Solution {
    def findScore(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_score(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-score nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_score(Nums :: [integer()]) -> integer().
find_score(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_score(nums :: [integer]) :: integer
  def find_score(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findScore(nums: Array<Int64>): Int64 {

    }
}
```

