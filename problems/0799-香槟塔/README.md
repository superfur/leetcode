# 799. 香槟塔

## 题目描述

<p>我们把玻璃杯摆成金字塔的形状，其中&nbsp;<strong>第一层</strong>&nbsp;有 <code>1</code> 个玻璃杯， <strong>第二层</strong>&nbsp;有 <code>2</code> 个，依次类推到第 100 层，每个玻璃杯将盛有香槟。</p>

<p>从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）</p>

<p>例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height: 241px; width: 350px;" /></p>

<p>现在当倾倒了非负整数杯香槟后，返回第 <code>i</code> 行 <code>j</code>&nbsp;个玻璃杯所盛放的香槟占玻璃杯容积的比例（ <code>i</code> 和 <code>j</code>&nbsp;都从0开始）。</p>

<p>&nbsp;</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.00000
<strong>解释:</strong> 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。

<strong>示例 2:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.50000
<strong>解释:</strong> 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。
</pre>

<p><meta charset="UTF-8" /></p>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> poured = 100000009, query_row = 33, query_glass = 17
<strong>输出:</strong> 1.00000
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;=&nbsp;poured &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= query_glass &lt;= query_row&nbsp;&lt; 100</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 示例

```
1
1
1
2
1
1
100000009
33
17
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        
    }
};
```

### Java

```java
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        
    }
}
```

### Python

```python
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
```

### C

```c
double champagneTower(int poured, int query_row, int query_glass) {
    
}
```

### C#

```csharp
public class Solution {
    public double ChampagneTower(int poured, int query_row, int query_glass) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
    
};
```

### TypeScript

```typescript
function champagneTower(poured: number, query_row: number, query_glass: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $poured
     * @param Integer $query_row
     * @param Integer $query_glass
     * @return Float
     */
    function champagneTower($poured, $query_row, $query_glass) {
        
    }
}
```

### Swift

```swift
class Solution {
    func champagneTower(_ poured: Int, _ query_row: Int, _ query_glass: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun champagneTower(poured: Int, query_row: Int, query_glass: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double champagneTower(int poured, int query_row, int query_glass) {
    
  }
}
```

### Go

```golang
func champagneTower(poured int, query_row int, query_glass int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} poured
# @param {Integer} query_row
# @param {Integer} query_glass
# @return {Float}
def champagne_tower(poured, query_row, query_glass)
    
end
```

### Scala

```scala
object Solution {
    def champagneTower(poured: Int, query_row: Int, query_glass: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (champagne-tower poured query_row query_glass)
  (-> exact-integer? exact-integer? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec champagne_tower(Poured :: integer(), Query_row :: integer(), Query_glass :: integer()) -> float().
champagne_tower(Poured, Query_row, Query_glass) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec champagne_tower(poured :: integer, query_row :: integer, query_glass :: integer) :: float
  def champagne_tower(poured, query_row, query_glass) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func champagneTower(poured: Int64, query_row: Int64, query_glass: Int64): Float64 {

    }
}
```

