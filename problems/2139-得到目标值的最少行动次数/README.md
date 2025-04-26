# 2139. 得到目标值的最少行动次数

## 题目描述

<p>你正在玩一个整数游戏。从整数 <code>1</code> 开始，期望得到整数 <code>target</code> 。</p>

<p>在一次行动中，你可以做下述两种操作之一：</p>

<ul>
	<li><strong>递增</strong>，将当前整数的值加 1（即， <code>x = x + 1</code>）。</li>
	<li><strong>加倍</strong>，使当前整数的值翻倍（即，<code>x = 2 * x</code>）。</li>
</ul>

<p>在整个游戏过程中，你可以使用 <strong>递增</strong> 操作 <strong>任意</strong> 次数。但是只能使用 <strong>加倍</strong> 操作 <strong>至多</strong> <code>maxDoubles</code> 次。</p>

<p>给你两个整数 <code>target</code> 和 <code>maxDoubles</code> ，返回从 1 开始得到<em> </em><code>target</code><em> </em>需要的最少行动次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = 5, maxDoubles = 0
<strong>输出：</strong>4
<strong>解释：</strong>一直递增 1 直到得到 target 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = 19, maxDoubles = 2
<strong>输出：</strong>7
<strong>解释：</strong>最初，x = 1 。
递增 3 次，x = 4 。
加倍 1 次，x = 8 。
递增 1 次，x = 9 。
加倍 1 次，x = 18 。
递增 1 次，x = 19 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = 10, maxDoubles = 4
<strong>输出：</strong>4
<strong>解释：</strong>
最初，x = 1 。 
递增 1 次，x = 2 。 
加倍 1 次，x = 4 。 
递增 1 次，x = 5 。 
加倍 1 次，x = 10 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= maxDoubles &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. Solve the opposite problem: start at the given score and move to 1.
2. It is better to use the move of the second type once we can to lose more scores fast.

## 示例

```
5
0
19
2
10
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMoves(int target, int maxDoubles) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMoves(int target, int maxDoubles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
```

### C

```c
int minMoves(int target, int maxDoubles) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMoves(int target, int maxDoubles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @param {number} maxDoubles
 * @return {number}
 */
var minMoves = function(target, maxDoubles) {
    
};
```

### TypeScript

```typescript
function minMoves(target: number, maxDoubles: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer $maxDoubles
     * @return Integer
     */
    function minMoves($target, $maxDoubles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMoves(_ target: Int, _ maxDoubles: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMoves(target: Int, maxDoubles: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMoves(int target, int maxDoubles) {
    
  }
}
```

### Go

```golang
func minMoves(target int, maxDoubles int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} target
# @param {Integer} max_doubles
# @return {Integer}
def min_moves(target, max_doubles)
    
end
```

### Scala

```scala
object Solution {
    def minMoves(target: Int, maxDoubles: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_moves(target: i32, max_doubles: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-moves target maxDoubles)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_moves(Target :: integer(), MaxDoubles :: integer()) -> integer().
min_moves(Target, MaxDoubles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_moves(target :: integer, max_doubles :: integer) :: integer
  def min_moves(target, max_doubles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMoves(target: Int64, maxDoubles: Int64): Int64 {

    }
}
```

