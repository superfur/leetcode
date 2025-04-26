# 2766. 重新放置石块

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，表示一些石块的初始位置。再给你两个长度<strong>&nbsp;相等</strong>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>moveFrom</code> 和&nbsp;<code>moveTo</code>&nbsp;。</p>

<p>在&nbsp;<code>moveFrom.length</code>&nbsp;次操作内，你将改变石块的位置。在第&nbsp;<code>i</code>&nbsp;次操作中，你将位置在&nbsp;<code>moveFrom[i]</code>&nbsp;的所有石块移到位置&nbsp;<code>moveTo[i]</code>&nbsp;。</p>

<p>完成这些操作后，请你按升序返回所有 <strong>有</strong>&nbsp;石块的位置。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>如果一个位置至少有一个石块，我们称这个位置 <strong>有</strong>&nbsp;石块。</li>
	<li>一个位置可能会有多个石块。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]
<b>输出：</b>[5,6,8,9]
<b>解释：</b>一开始，石块在位置 1,6,7,8 。
第 i = 0 步操作中，我们将位置 1 处的石块移到位置 2 处，位置 2,6,7,8 有石块。
第 i = 1 步操作中，我们将位置 7 处的石块移到位置 9 处，位置 2,6,8,9 有石块。
第 i = 2 步操作中，我们将位置 2 处的石块移到位置 5 处，位置 5,6,8,9 有石块。
最后，至少有一个石块的位置为 [5,6,8,9] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2]
<b>输出：</b>[2]
<b>解释：</b>一开始，石块在位置 [1,1,3,3] 。
第 i = 0 步操作中，我们将位置 1 处的石块移到位置 2 处，有石块的位置为 [2,2,3,3] 。
第 i = 1 步操作中，我们将位置 3 处的石块移到位置 2 处，有石块的位置为 [2,2,2,2] 。
由于 2 是唯一有石块的位置，我们返回 [2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= moveFrom.length &lt;= 10<sup>5</sup></code></li>
	<li><code>moveFrom.length == moveTo.length</code></li>
	<li><code>1 &lt;= nums[i], moveFrom[i], moveTo[i] &lt;= 10<sup>9</sup></code></li>
	<li>测试数据保证在进行第&nbsp;<code>i</code>&nbsp;步操作时，<code>moveFrom[i]</code>&nbsp;处至少有一个石块。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序
- 模拟

## 提示

1. Can we solve this problem using a set or map?
2. Sequentially process pairs from moveFrom[i] and moveTo[i]. In each step, remove the occurrence of moveFrom[i] and add moveTo[i] into the set.

## 示例

```
[1,6,7,8]
[1,7,2]
[2,9,5]
[1,1,3,3]
[1,3]
[2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> relocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
        
    }
}
```

### Python

```python
class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* relocateMarbles(int* nums, int numsSize, int* moveFrom, int moveFromSize, int* moveTo, int moveToSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> RelocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} moveFrom
 * @param {number[]} moveTo
 * @return {number[]}
 */
var relocateMarbles = function(nums, moveFrom, moveTo) {
    
};
```

### TypeScript

```typescript
function relocateMarbles(nums: number[], moveFrom: number[], moveTo: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $moveFrom
     * @param Integer[] $moveTo
     * @return Integer[]
     */
    function relocateMarbles($nums, $moveFrom, $moveTo) {
        
    }
}
```

### Swift

```swift
class Solution {
    func relocateMarbles(_ nums: [Int], _ moveFrom: [Int], _ moveTo: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun relocateMarbles(nums: IntArray, moveFrom: IntArray, moveTo: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> relocateMarbles(List<int> nums, List<int> moveFrom, List<int> moveTo) {
    
  }
}
```

### Go

```golang
func relocateMarbles(nums []int, moveFrom []int, moveTo []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} move_from
# @param {Integer[]} move_to
# @return {Integer[]}
def relocate_marbles(nums, move_from, move_to)
    
end
```

### Scala

```scala
object Solution {
    def relocateMarbles(nums: Array[Int], moveFrom: Array[Int], moveTo: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn relocate_marbles(nums: Vec<i32>, move_from: Vec<i32>, move_to: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (relocate-marbles nums moveFrom moveTo)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec relocate_marbles(Nums :: [integer()], MoveFrom :: [integer()], MoveTo :: [integer()]) -> [integer()].
relocate_marbles(Nums, MoveFrom, MoveTo) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec relocate_marbles(nums :: [integer], move_from :: [integer], move_to :: [integer]) :: [integer]
  def relocate_marbles(nums, move_from, move_to) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func relocateMarbles(nums: Array<Int64>, moveFrom: Array<Int64>, moveTo: Array<Int64>): ArrayList<Int64> {

    }
}
```

