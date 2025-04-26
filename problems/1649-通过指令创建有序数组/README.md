# 1649. 通过指令创建有序数组

## 题目描述

<p>给你一个整数数组 <code>instructions</code> ，你需要根据 <code>instructions</code> 中的元素创建一个有序数组。一开始你有一个空的数组 <code>nums</code> ，你需要 <strong>从左到右</strong> 遍历 <code>instructions</code> 中的元素，将它们依次插入 <code>nums</code> 数组中。每一次插入操作的 <strong>代价</strong> 是以下两者的 <strong>较小值</strong> ：</p>

<ul>
	<li><code>nums</code> 中 <strong>严格小于 </strong> <code>instructions[i]</code> 的数字数目。</li>
	<li><code>nums</code> 中 <strong>严格大于 </strong> <code>instructions[i]</code> 的数字数目。</li>
</ul>

<p>比方说，如果要将 <code>3</code> 插入到 <code>nums = [1,2,3,5]</code> ，那么插入操作的 <strong>代价</strong> 为 <code>min(2, 1)</code> (元素 <code>1</code> 和  <code>2</code> 小于 <code>3</code> ，元素 <code>5</code> 大于 <code>3</code> ），插入后 <code>nums</code> 变成 <code>[1,2,3,3,5]</code> 。</p>

<p>请你返回将 <code>instructions</code> 中所有元素依次插入 <code>nums</code> 后的 <strong>总最小代价 </strong>。由于答案会很大，请将它对 <code>10<sup>9</sup> + 7</code> <b>取余</b> 后返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>instructions = [1,5,6,2]
<b>输出：</b>1
<b>解释：</b>一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
总代价为 0 + 0 + 0 + 1 = 1 。</pre>

<p><strong>示例 2:</strong></p>

<pre><b>输入：</b>instructions = [1,2,3,6,5,4]
<b>输出：</b>3
<b>解释：</b>一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>instructions = [1,3,3,3,2,4,2,1,2]
<b>输出：</b>4
<b>解释：</b>一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= instructions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= instructions[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 分治
- 有序集合
- 归并排序

## 提示

1. This problem is closely related to finding the number of inversions in an array
2. if i know the position in which i will insert the i-th element in I can find the minimum cost to insert it

## 示例

```
[1,5,6,2]
[1,2,3,6,5,4]
[1,3,3,3,2,4,2,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        
    }
};
```

### Java

```java
class Solution {
    public int createSortedArray(int[] instructions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
```

### C

```c
int createSortedArray(int* instructions, int instructionsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CreateSortedArray(int[] instructions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} instructions
 * @return {number}
 */
var createSortedArray = function(instructions) {
    
};
```

### TypeScript

```typescript
function createSortedArray(instructions: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $instructions
     * @return Integer
     */
    function createSortedArray($instructions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func createSortedArray(_ instructions: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun createSortedArray(instructions: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int createSortedArray(List<int> instructions) {
    
  }
}
```

### Go

```golang
func createSortedArray(instructions []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} instructions
# @return {Integer}
def create_sorted_array(instructions)
    
end
```

### Scala

```scala
object Solution {
    def createSortedArray(instructions: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn create_sorted_array(instructions: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (create-sorted-array instructions)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec create_sorted_array(Instructions :: [integer()]) -> integer().
create_sorted_array(Instructions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec create_sorted_array(instructions :: [integer]) :: integer
  def create_sorted_array(instructions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func createSortedArray(instructions: Array<Int64>): Int64 {

    }
}
```

