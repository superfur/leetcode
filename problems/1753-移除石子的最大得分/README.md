# 1753. 移除石子的最大得分

## 题目描述

<p>你正在玩一个单人游戏，面前放置着大小分别为 <code>a</code>​​​​​​、<code>b</code> 和 <code>c</code>​​​​​​ 的 <strong>三堆</strong> 石子。</p>

<p>每回合你都要从两个 <strong>不同的非空堆</strong> 中取出一颗石子，并在得分上加 <code>1</code> 分。当存在 <strong>两个或更多</strong> 的空堆时，游戏停止。</p>

<p>给你三个整数 <code>a</code> 、<code>b</code> 和 <code>c</code> ，返回可以得到的 <strong>最大分数</strong> 。</p>
 

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>a = 2, b = 4, c = 6
<strong>输出：</strong>6
<strong>解释：</strong>石子起始状态是 (2, 4, 6) ，最优的一组操作是：
- 从第一和第三堆取，石子状态现在是 (1, 4, 5)
- 从第一和第三堆取，石子状态现在是 (0, 4, 4)
- 从第二和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：6 分 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = 4, b = 4, c = 6
<strong>输出：</strong>7
<strong>解释：</strong>石子起始状态是 (4, 4, 6) ，最优的一组操作是：
- 从第一和第二堆取，石子状态现在是 (3, 3, 6)
- 从第一和第三堆取，石子状态现在是 (2, 3, 5)
- 从第一和第三堆取，石子状态现在是 (1, 3, 4)
- 从第一和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：7 分 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>a = 1, b = 8, c = 8
<strong>输出：</strong>8
<strong>解释：</strong>最优的一组操作是连续从第二和第三堆取 8 回合，直到将它们取空。
注意，由于第二和第三堆已经空了，游戏结束，不能继续从第一堆中取石子。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= a, b, c <= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 堆（优先队列）

## 提示

1. It's optimal to always remove one stone from the biggest 2 piles
2. Note that the limits are small enough for simulation

## 示例

```
2
4
6
4
4
6
1
8
8
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumScore(int a, int b, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumScore(int a, int b, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
```

### C

```c
int maximumScore(int a, int b, int c) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumScore(int a, int b, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var maximumScore = function(a, b, c) {
    
};
```

### TypeScript

```typescript
function maximumScore(a: number, b: number, c: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function maximumScore($a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ a: Int, _ b: Int, _ c: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(a: Int, b: Int, c: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumScore(int a, int b, int c) {
    
  }
}
```

### Go

```golang
func maximumScore(a int, b int, c int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def maximum_score(a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def maximumScore(a: Int, b: Int, c: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(a: i32, b: i32, c: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-score a b c)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_score(A :: integer(), B :: integer(), C :: integer()) -> integer().
maximum_score(A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_score(a :: integer, b :: integer, c :: integer) :: integer
  def maximum_score(a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumScore(a: Int64, b: Int64, c: Int64): Int64 {

    }
}
```

