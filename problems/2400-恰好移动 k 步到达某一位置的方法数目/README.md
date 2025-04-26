# 2400. 恰好移动 k 步到达某一位置的方法数目

## 题目描述

<p>给你两个 <strong>正</strong> 整数 <code>startPos</code> 和 <code>endPos</code> 。最初，你站在 <strong>无限</strong> 数轴上位置 <code>startPos</code> 处。在一步移动中，你可以向左或者向右移动一个位置。</p>

<p>给你一个正整数 <code>k</code> ，返回从 <code>startPos</code> 出发、<strong>恰好</strong> 移动 <code>k</code> 步并到达 <code>endPos</code> 的 <strong>不同</strong> 方法数目。由于答案可能会很大，返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>如果所执行移动的顺序不完全相同，则认为两种方法不同。</p>

<p><strong>注意：</strong>数轴包含负整数<strong>。</strong></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>startPos = 1, endPos = 2, k = 3
<strong>输出：</strong>3
<strong>解释：</strong>存在 3 种从 1 到 2 且恰好移动 3 步的方法：
- 1 -&gt; 2 -&gt; 3 -&gt; 2.
- 1 -&gt; 2 -&gt; 1 -&gt; 2.
- 1 -&gt; 0 -&gt; 1 -&gt; 2.
可以证明不存在其他方法，所以返回 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>startPos = 2, endPos = 5, k = 10
<strong>输出：</strong>0
<strong>解释：</strong>不存在从 2 到 5 且恰好移动 10 步的方法。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= startPos, endPos, k &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. How many steps to the left and to the right do you need to make exactly?
2. Does the order of the steps matter?
3. Use combinatorics to find the number of ways to order the steps.

## 示例

```
1
2
3
2
5
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfWays(int startPos, int endPos, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfWays(int startPos, int endPos, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
```

### C

```c
int numberOfWays(int startPos, int endPos, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfWays(int startPos, int endPos, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} startPos
 * @param {number} endPos
 * @param {number} k
 * @return {number}
 */
var numberOfWays = function(startPos, endPos, k) {
    
};
```

### TypeScript

```typescript
function numberOfWays(startPos: number, endPos: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $startPos
     * @param Integer $endPos
     * @param Integer $k
     * @return Integer
     */
    function numberOfWays($startPos, $endPos, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWays(_ startPos: Int, _ endPos: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWays(startPos: Int, endPos: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWays(int startPos, int endPos, int k) {
    
  }
}
```

### Go

```golang
func numberOfWays(startPos int, endPos int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} start_pos
# @param {Integer} end_pos
# @param {Integer} k
# @return {Integer}
def number_of_ways(start_pos, end_pos, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWays(startPos: Int, endPos: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_ways(start_pos: i32, end_pos: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-ways startPos endPos k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_ways(StartPos :: integer(), EndPos :: integer(), K :: integer()) -> integer().
number_of_ways(StartPos, EndPos, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(start_pos :: integer, end_pos :: integer, k :: integer) :: integer
  def number_of_ways(start_pos, end_pos, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWays(startPos: Int64, endPos: Int64, k: Int64): Int64 {

    }
}
```

