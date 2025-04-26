# 2350. 不可能得到的最短骰子序列

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>rolls</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你扔一个&nbsp;<code>k</code>&nbsp;面的骰子 <code>n</code>&nbsp;次，骰子的每个面分别是&nbsp;<code>1</code>&nbsp;到&nbsp;<code>k</code>&nbsp;，其中第&nbsp;<code>i</code>&nbsp;次扔得到的数字是&nbsp;<code>rolls[i]</code>&nbsp;。</p>

<p>请你返回 <strong>无法</strong>&nbsp;从 <code>rolls</code>&nbsp;中得到的 <strong>最短</strong>&nbsp;骰子子序列的长度。</p>

<p>扔一个 <code>k</code>&nbsp;面的骰子 <code>len</code>&nbsp;次得到的是一个长度为 <code>len</code>&nbsp;的 <strong>骰子子序列</strong>&nbsp;。</p>

<p><strong>注意</strong>&nbsp;，子序列只需要保持在原数组中的顺序，不需要连续。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>rolls = [4,2,1,2,3,3,2,4,1], k = 4
<b>输出：</b>3
<b>解释：</b>所有长度为 1 的骰子子序列 [1] ，[2] ，[3] ，[4] 都可以从原数组中得到。
所有长度为 2 的骰子子序列 [1, 1] ，[1, 2] ，... ，[4, 4] 都可以从原数组中得到。
子序列 [1, 4, 2] 无法从原数组中得到，所以我们返回 3 。
还有别的子序列也无法从原数组中得到。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>rolls = [1,1,2,2], k = 2
<b>输出：</b>2
<b>解释：</b>所有长度为 1 的子序列 [1] ，[2] 都可以从原数组中得到。
子序列 [2, 1] 无法从原数组中得到，所以我们返回 2 。
还有别的子序列也无法从原数组中得到，但 [2, 1] 是最短的子序列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>rolls = [1,1,3,2,2,2,3,3], k = 4
<b>输出：</b>1
<b>解释：</b>子序列 [4] 无法从原数组中得到，所以我们返回 1 。
还有别的子序列也无法从原数组中得到，但 [4] 是最短的子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == rolls.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= rolls[i] &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. How can you find the minimum index such that all sequences of length 1 can be formed from the start until that index?
2. Starting from the previous minimum index, what is the next index such that all sequences of length 2 can be formed?
3. Can you extend the idea to sequences of length 3 and more?

## 示例

```
[4,2,1,2,3,3,2,4,1]
4
[1,1,2,2]
2
[1,1,3,2,2,2,3,3]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestSequence(vector<int>& rolls, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestSequence(int[] rolls, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        
```

### C

```c
int shortestSequence(int* rolls, int rollsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestSequence(int[] rolls, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rolls
 * @param {number} k
 * @return {number}
 */
var shortestSequence = function(rolls, k) {
    
};
```

### TypeScript

```typescript
function shortestSequence(rolls: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rolls
     * @param Integer $k
     * @return Integer
     */
    function shortestSequence($rolls, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestSequence(_ rolls: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestSequence(rolls: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestSequence(List<int> rolls, int k) {
    
  }
}
```

### Go

```golang
func shortestSequence(rolls []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rolls
# @param {Integer} k
# @return {Integer}
def shortest_sequence(rolls, k)
    
end
```

### Scala

```scala
object Solution {
    def shortestSequence(rolls: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_sequence(rolls: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-sequence rolls k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_sequence(Rolls :: [integer()], K :: integer()) -> integer().
shortest_sequence(Rolls, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_sequence(rolls :: [integer], k :: integer) :: integer
  def shortest_sequence(rolls, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestSequence(rolls: Array<Int64>, k: Int64): Int64 {

    }
}
```

