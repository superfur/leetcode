# 1713. 得到子序列的最少操作次数

## 题目描述

<p>给你一个数组 <code>target</code> ，包含若干 <strong>互不相同</strong> 的整数，以及另一个整数数组 <code>arr</code> ，<code>arr</code> <strong>可能</strong> 包含重复元素。</p>

<p>每一次操作中，你可以在 <code>arr</code> 的任意位置插入任一整数。比方说，如果 <code>arr = [1,4,1,2]</code> ，那么你可以在中间添加 <code>3</code> 得到 <code>[1,4,<strong>3</strong>,1,2]</code> 。你可以在数组最开始或最后面添加整数。</p>

<p>请你返回 <strong>最少</strong> 操作次数，使得<em> </em><code>target</code><em> </em>成为 <code>arr</code> 的一个子序列。</p>

<p>一个数组的 <strong>子序列</strong> 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，<code>[2,7,4]</code> 是 <code>[4,<strong>2</strong>,3,<strong>7</strong>,2,1,<strong>4</strong>]</code> 的子序列（加粗元素），但 <code>[2,4,2]</code> 不是子序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>target = [5,1,3], <code>arr</code> = [9,4,2,3,4]
<b>输出：</b>2
<b>解释：</b>你可以添加 5 和 1 ，使得 arr 变为 [<strong>5</strong>,9,4,<strong>1</strong>,2,3,4] ，target 为 arr 的子序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>target = [6,4,8,1,3,2], <code>arr</code> = [4,7,6,2,3,8,6,1]
<b>输出：</b>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length, arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= target[i], arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>target</code> 不包含任何重复元素。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 哈希表
- 二分查找

## 提示

1. The problem can be reduced to computing Longest Common Subsequence between both arrays.
2. Since one of the arrays has distinct elements, we can consider that these elements describe an arrangement of numbers, and we can replace each element in the other array with the index it appeared at in the first array.
3. Then the problem is converted to finding Longest Increasing Subsequence in the second array, which can be done in O(n log n).

## 示例

```
[5,1,3]
[9,4,2,3,4]
[6,4,8,1,3,2]
[4,7,6,2,3,8,6,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& target, vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[] target, int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
```

### C

```c
int minOperations(int* target, int targetSize, int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[] target, int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {number}
 */
var minOperations = function(target, arr) {
    
};
```

### TypeScript

```typescript
function minOperations(target: number[], arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $target
     * @param Integer[] $arr
     * @return Integer
     */
    function minOperations($target, $arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ target: [Int], _ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(target: IntArray, arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> target, List<int> arr) {
    
  }
}
```

### Go

```golang
func minOperations(target []int, arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} target
# @param {Integer[]} arr
# @return {Integer}
def min_operations(target, arr)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(target: Array[Int], arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(target: Vec<i32>, arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations target arr)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Target :: [integer()], Arr :: [integer()]) -> integer().
min_operations(Target, Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(target :: [integer], arr :: [integer]) :: integer
  def min_operations(target, arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(target: Array<Int64>, arr: Array<Int64>): Int64 {

    }
}
```

