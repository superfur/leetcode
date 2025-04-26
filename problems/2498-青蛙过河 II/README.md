# 2498. 青蛙过河 II

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>stones</code>&nbsp;，数组中的元素&nbsp;<strong>严格递增</strong>&nbsp;，表示一条河中石头的位置。</p>

<p>一只青蛙一开始在第一块石头上，它想到达最后一块石头，然后回到第一块石头。同时每块石头 <strong>至多</strong> 到达 <strong>一次。</strong></p>

<p>一次跳跃的 <strong>长度</strong>&nbsp;是青蛙跳跃前和跳跃后所在两块石头之间的距离。</p>

<ul>
	<li>更正式的，如果青蛙从&nbsp;<code>stones[i]</code>&nbsp;跳到&nbsp;<code>stones[j]</code>&nbsp;，跳跃的长度为&nbsp;<code>|stones[i] - stones[j]|</code>&nbsp;。</li>
</ul>

<p>一条路径的 <b>代价</b>&nbsp;是这条路径里的&nbsp;<b>最大跳跃长度</b>&nbsp;。</p>

<p>请你返回这只青蛙的 <strong>最小代价</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/14/example-1.png" style="width: 600px; height: 219px;" /></p>

<pre>
<b>输入：</b>stones = [0,2,5,6,7]
<b>输出：</b>5
<b>解释：</b>上图展示了一条最优路径。
这条路径的代价是 5 ，是这条路径中的最大跳跃长度。
无法得到一条代价小于 5 的路径，我们返回 5 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/14/example-2.png" style="width: 500px; height: 171px;" /></p>

<pre>
<b>输入：</b>stones = [0,3,9]
<b>输出：</b>9
<b>解释：</b>
青蛙可以直接跳到最后一块石头，然后跳回第一块石头。
在这条路径中，每次跳跃长度都是 9 。所以路径代价是 max(9, 9) = 9 。
这是可行路径中的最小代价。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= stones.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= stones[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>stones[0] == 0</code></li>
	<li><code>stones</code>&nbsp;中的元素严格递增。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找

## 提示

1. One of the optimal strategies will be to jump to every stone.
2. Skipping just one stone in every forward jump and jumping to those skipped stones in backward jump can minimize the maximum jump.

## 示例

```
[0,2,5,6,7]
[0,3,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxJump(vector<int>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxJump(int[] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
```

### C

```c
int maxJump(int* stones, int stonesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxJump(int[] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var maxJump = function(stones) {
    
};
```

### TypeScript

```typescript
function maxJump(stones: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function maxJump($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxJump(_ stones: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxJump(stones: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxJump(List<int> stones) {
    
  }
}
```

### Go

```golang
func maxJump(stones []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def max_jump(stones)
    
end
```

### Scala

```scala
object Solution {
    def maxJump(stones: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_jump(stones: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-jump stones)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_jump(Stones :: [integer()]) -> integer().
max_jump(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_jump(stones :: [integer]) :: integer
  def max_jump(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxJump(stones: Array<Int64>): Int64 {

    }
}
```

