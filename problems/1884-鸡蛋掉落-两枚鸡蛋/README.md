# 1884. 鸡蛋掉落-两枚鸡蛋

## 题目描述

<p>给你 <strong>2&nbsp;枚相同 </strong>的鸡蛋，和一栋从第 <code>1</code>&nbsp;层到第 <code>n</code> 层共有 <code>n</code> 层楼的建筑。</p>

<p>已知存在楼层 <code>f</code> ，满足&nbsp;<code>0 &lt;= f &lt;= n</code> ，任何从 <strong>高于 </strong><code>f</code> 的楼层落下的鸡蛋都<strong> 会碎 </strong>，从 <strong><code>f</code> 楼层或比它低 </strong>的楼层落下的鸡蛋都 <strong>不会碎 </strong>。</p>

<p>每次操作，你可以取一枚<strong> 没有碎</strong> 的鸡蛋并把它从任一楼层 <code>x</code> 扔下（满足&nbsp;<code>1 &lt;= x &lt;= n</code>）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中<strong> 重复使用 </strong>这枚鸡蛋。</p>

<p>请你计算并返回要确定 <code>f</code> <strong>确切的值 </strong>的 <strong>最小操作次数</strong> 是多少？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>2
<strong>解释：</strong>我们可以将第一枚鸡蛋从 1 楼扔下，然后将第二枚从 2 楼扔下。
如果第一枚鸡蛋碎了，可知 f = 0；
如果第二枚鸡蛋碎了，但第一枚没碎，可知 f = 1；
否则，当两个鸡蛋都没碎时，可知 f = 2。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 100
<strong>输出：</strong>14
<strong>解释：
</strong>一种最优的策略是：
- 将第一枚鸡蛋从 9 楼扔下。如果碎了，那么 f 在 0 和 8 之间。将第二枚从 1 楼扔下，然后每扔一次上一层楼，在 8 次内找到 f 。总操作次数 = 1 + 8 = 9 。
- 如果第一枚鸡蛋没有碎，那么再把第一枚鸡蛋从 22 层扔下。如果碎了，那么 f 在 9 和 21 之间。将第二枚鸡蛋从 10 楼扔下，然后每扔一次上一层楼，在 12 次内找到 f 。总操作次数 = 2 + 12 = 14 。
- 如果第一枚鸡蛋没有再次碎掉，则按照类似的方法从 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99 和 100 楼分别扔下第一枚鸡蛋。
不管结果如何，最多需要扔 14 次来确定 f 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划

## 提示

1. Is it really optimal to always drop the egg on the middle floor for each move?
2. Can we create states based on the number of unbroken eggs and floors to build our solution?

## 示例

```
2
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int twoEggDrop(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int twoEggDrop(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def twoEggDrop(self, n: int) -> int:
        
```

### C

```c
int twoEggDrop(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int TwoEggDrop(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var twoEggDrop = function(n) {
    
};
```

### TypeScript

```typescript
function twoEggDrop(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function twoEggDrop($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func twoEggDrop(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun twoEggDrop(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int twoEggDrop(int n) {
    
  }
}
```

### Go

```golang
func twoEggDrop(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def two_egg_drop(n)
    
end
```

### Scala

```scala
object Solution {
    def twoEggDrop(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn two_egg_drop(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (two-egg-drop n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec two_egg_drop(N :: integer()) -> integer().
two_egg_drop(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec two_egg_drop(n :: integer) :: integer
  def two_egg_drop(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func twoEggDrop(n: Int64): Int64 {

    }
}
```

