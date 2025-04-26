# 1040. 移动石子直到连续 II

## 题目描述

<p>在 X 轴上有一些不同位置的石子。给定一个整数数组&nbsp;<code>stones</code>&nbsp;表示石子的位置。</p>

<p>如果一个石子在最小或最大的位置，称其为&nbsp;<strong>端点石子</strong>。每个回合，你可以将一颗 <strong>端点石子</strong> 拿起并移动到一个未占用的位置，使得该石子不再是一颗 <strong>端点石子</strong>。</p>

<ul>
	<li>值得注意的是，如果石子像&nbsp;<code>stones = [1,2,5]</code>&nbsp;这样，你将 <strong>无法 </strong>移动位于位置 <code>5</code> 的端点石子，因为无论将它移动到任何位置（例如 <code>0</code> 或 <code>3</code>），该石子都仍然会是端点石子。</li>
</ul>

<p>当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。</p>

<p>以长度为 2 的数组形式返回答案，其中：</p>

<ul>
	<li><code>answer[0]</code>&nbsp;是你可以移动的最小次数</li>
	<li><code>answer[1]</code>&nbsp;是你可以移动的最大次数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[7,4,9]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>
我们可以移动一次，4 -&gt; 8，游戏结束。
或者，我们可以移动两次 9 -&gt; 5，4 -&gt; 6，游戏结束。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>[6,5,4,3,10]
<strong>输出：</strong>[2,3]
<strong>解释：</strong>
我们可以移动 3 -&gt; 8，接着是 10 -&gt; 7，游戏结束。
或者，我们可以移动 3 -&gt; 7, 4 -&gt; 8, 5 -&gt; 9，游戏结束。
注意，我们无法进行 10 -&gt; 2 这样的移动来结束游戏，因为这是不合要求的移动。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= stones.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= stones[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>stones</code>&nbsp;的值各不相同。</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 数学
- 排序
- 滑动窗口

## 提示

1. For the minimum, how many stones are already in place?
For the maximum, we have to lose either the gap A[1] - A[0] or A[N-1] - A[N-2]  (where N = A.length), but every other space can be occupied.

## 示例

```
[7,4,9]
[6,5,4,3,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numMovesStonesII(vector<int>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] numMovesStonesII(int[] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numMovesStonesII(int* stones, int stonesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] NumMovesStonesII(int[] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @return {number[]}
 */
var numMovesStonesII = function(stones) {
    
};
```

### TypeScript

```typescript
function numMovesStonesII(stones: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer[]
     */
    function numMovesStonesII($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numMovesStonesII(_ stones: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numMovesStonesII(stones: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numMovesStonesII(List<int> stones) {
    
  }
}
```

### Go

```golang
func numMovesStonesII(stones []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer[]}
def num_moves_stones_ii(stones)
    
end
```

### Scala

```scala
object Solution {
    def numMovesStonesII(stones: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_moves_stones_ii(stones: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (num-moves-stones-ii stones)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec num_moves_stones_ii(Stones :: [integer()]) -> [integer()].
num_moves_stones_ii(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_moves_stones_ii(stones :: [integer]) :: [integer]
  def num_moves_stones_ii(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numMovesStonesII(stones: Array<Int64>): Array<Int64> {

    }
}
```

