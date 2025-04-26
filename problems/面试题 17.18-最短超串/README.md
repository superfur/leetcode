# 面试题 17.18. 最短超串

## 题目描述

<p>假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。</p>

<p>返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
big = <code>[7,5,9,0,2,1,3,<strong>5,7,9,1</strong>,1,5,8,8,9,7]
small = [1,5,9]</code>
<strong>输出：</strong>[7,10]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
big = <code>[1,2,3]
small = [4]</code>
<strong>输出：</strong>[]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>big.length&nbsp;&lt;= 100000</code></li>
	<li><code>1 &lt;= small.length&nbsp;&lt;= 100000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. 从蛮力解法开始。
2. 一种蛮力解决方案是对于每个起始位置不断向前移动，直到你找到一个包含所有目标字符的子序列为止。
3. 另一种对蛮力方法的考虑是，我们取每个起始索引，在目标字符串中寻找每个元素的下一个出现位置。所有这些出现位置的最大值标志着子序列的尾部（该子序列包含所有目标字符）。这个算法的时间复杂度是多少？怎样才能使它更快呢？
4. 考虑一下前面解释的蛮力解法。瓶颈在于我们反复查询某个特定字符的下一个出现位置。有办法优化该过程么？你应该能在O(1)时间内完成。
5. 你能从每个索引中预先计算一个特定字符的出现位置吗？尝试使用一个多维数组。
6. 在得到了预计算的解法之后，考虑一下如何降低空间复杂度。你应该能够将其降低到O(SB)的时间和O(B)的空间（其中B是较大数组的大小，S是较小数组的大小）。
7. 另一种考虑方法是：假设你有一个每个元素所在索引的列表。你能找到包含所有元素的第一个子序列吗？你能找到第二个吗？
8. 考虑使用堆。

## 示例

```
[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
[1, 5, 9]
[1, 2, 1, 2, 1, 2]
[1, 2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> shortestSeq(vector<int>& big, vector<int>& small) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] shortestSeq(int[] big, int[] small) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestSeq(self, big, small):
        """
        :type big: List[int]
        :type small: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestSeq(int* big, int bigSize, int* small, int smallSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ShortestSeq(int[] big, int[] small) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} big
 * @param {number[]} small
 * @return {number[]}
 */
var shortestSeq = function(big, small) {
    
};
```

### TypeScript

```typescript
function shortestSeq(big: number[], small: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $big
     * @param Integer[] $small
     * @return Integer[]
     */
    function shortestSeq($big, $small) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestSeq(_ big: [Int], _ small: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestSeq(big: IntArray, small: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> shortestSeq(List<int> big, List<int> small) {
    
  }
}
```

### Go

```golang
func shortestSeq(big []int, small []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} big
# @param {Integer[]} small
# @return {Integer[]}
def shortest_seq(big, small)
    
end
```

### Scala

```scala
object Solution {
    def shortestSeq(big: Array[Int], small: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_seq(big: Vec<i32>, small: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-seq big small)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec shortest_seq(Big :: [integer()], Small :: [integer()]) -> [integer()].
shortest_seq(Big, Small) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_seq(big :: [integer], small :: [integer]) :: [integer]
  def shortest_seq(big, small) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestSeq(big: Array<Int64>, small: Array<Int64>): Array<Int64> {

    }
}
```

