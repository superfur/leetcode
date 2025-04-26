# 3021. Alice 和 Bob 玩鲜花游戏

## 题目描述

<p>Alice 和 Bob 在一个长满鲜花的环形草地玩一个回合制游戏。环形的草地上有一些鲜花，Alice 到&nbsp;Bob 之间顺时针有 <code>x</code>&nbsp;朵鲜花，逆时针有 <code>y</code>&nbsp;朵鲜花。</p>

<p>游戏过程如下：</p>

<ol>
	<li>Alice 先行动。</li>
	<li>每一次行动中，当前玩家必须选择顺时针或者逆时针，然后在这个方向上摘一朵鲜花。</li>
	<li>一次行动结束后，如果所有鲜花都被摘完了，那么 <strong>当前</strong>&nbsp;玩家抓住对手并赢得游戏的胜利。</li>
</ol>

<p>给你两个整数&nbsp;<code>n</code>&nbsp;和&nbsp;<code>m</code>&nbsp;，你的任务是求出满足以下条件的所有&nbsp;<code>(x, y)</code>&nbsp;对：</p>

<ul>
	<li>按照上述规则，Alice 必须赢得游戏。</li>
	<li>Alice 顺时针方向上的鲜花数目&nbsp;<code>x</code>&nbsp;必须在区间&nbsp;<code>[1,n]</code>&nbsp;之间。</li>
	<li>Alice 逆时针方向上的鲜花数目 <code>y</code>&nbsp;必须在区间&nbsp;<code>[1,m]</code>&nbsp;之间。</li>
</ul>

<p>请你返回满足题目描述的数对&nbsp;<code>(x, y)</code>&nbsp;的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 3, m = 2
<b>输出：</b>3
<b>解释：</b>以下数对满足题目要求：(1,2) ，(3,2) ，(2,1) 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 1, m = 1
<b>输出：</b>0
<b>解释：</b>没有数对满足题目要求。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. (x, y) is valid if and only if they have different parities.

## 示例

```
3
2
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long flowerGame(int n, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public long flowerGame(int n, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        
```

### C

```c
long long flowerGame(int n, int m) {
    
}
```

### C#

```csharp
public class Solution {
    public long FlowerGame(int n, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var flowerGame = function(n, m) {
    
};
```

### TypeScript

```typescript
function flowerGame(n: number, m: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function flowerGame($n, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func flowerGame(_ n: Int, _ m: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun flowerGame(n: Int, m: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int flowerGame(int n, int m) {
    
  }
}
```

### Go

```golang
func flowerGame(n int, m int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def flower_game(n, m)
    
end
```

### Scala

```scala
object Solution {
    def flowerGame(n: Int, m: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn flower_game(n: i32, m: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (flower-game n m)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec flower_game(N :: integer(), M :: integer()) -> integer().
flower_game(N, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec flower_game(n :: integer, m :: integer) :: integer
  def flower_game(n, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func flowerGame(n: Int64, m: Int64): Int64 {

    }
}
```

