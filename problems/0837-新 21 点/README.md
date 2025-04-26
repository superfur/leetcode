# 837. 新 21 点

## 题目描述

<p>爱丽丝参与一个大致基于纸牌游戏 <strong>“21点”</strong> 规则的游戏，描述如下：</p>

<p>爱丽丝以 <code>0</code> 分开始，并在她的得分少于 <code>k</code> 分时抽取数字。 抽取时，她从 <code>[1, maxPts]</code> 的范围中随机获得一个整数作为分数进行累计，其中 <code>maxPts</code> 是一个整数。 每次抽取都是独立的，其结果具有相同的概率。</p>

<p>当爱丽丝获得 <code>k</code> 分 <strong>或更多分</strong> 时，她就停止抽取数字。</p>

<p>爱丽丝的分数不超过 <code>n</code> 的概率是多少？</p>

<p>与实际答案误差不超过&nbsp;<code>10<sup>-5</sup></code> 的答案将被视为正确答案。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10, k = 1, maxPts = 10
<strong>输出：</strong>1.00000
<strong>解释：</strong>爱丽丝得到一张牌，然后停止。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 6, k = 1, maxPts = 10
<strong>输出：</strong>0.60000
<strong>解释：</strong>爱丽丝得到一张牌，然后停止。 在 10 种可能性中的 6 种情况下，她的得分不超过 6 分。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 21, k = 17, maxPts = 10
<strong>输出：</strong>0.73278
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= maxPts &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 滑动窗口
- 概率与统计

## 示例

```
10
1
10
6
1
10
21
17
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        
    }
};
```

### Java

```java
class Solution {
    public double new21Game(int n, int k, int maxPts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
```

### C

```c
double new21Game(int n, int k, int maxPts) {
    
}
```

### C#

```csharp
public class Solution {
    public double New21Game(int n, int k, int maxPts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} maxPts
 * @return {number}
 */
var new21Game = function(n, k, maxPts) {
    
};
```

### TypeScript

```typescript
function new21Game(n: number, k: number, maxPts: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $maxPts
     * @return Float
     */
    function new21Game($n, $k, $maxPts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func new21Game(_ n: Int, _ k: Int, _ maxPts: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun new21Game(n: Int, k: Int, maxPts: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double new21Game(int n, int k, int maxPts) {
    
  }
}
```

### Go

```golang
func new21Game(n int, k int, maxPts int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @param {Integer} max_pts
# @return {Float}
def new21_game(n, k, max_pts)
    
end
```

### Scala

```scala
object Solution {
    def new21Game(n: Int, k: Int, maxPts: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (new21-game n k maxPts)
  (-> exact-integer? exact-integer? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec new21_game(N :: integer(), K :: integer(), MaxPts :: integer()) -> float().
new21_game(N, K, MaxPts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec new21_game(n :: integer, k :: integer, max_pts :: integer) :: float
  def new21_game(n, k, max_pts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func new21Game(n: Int64, k: Int64, maxPts: Int64): Float64 {

    }
}
```

