# 887. 鸡蛋掉落

## 题目描述

<p>给你 <code>k</code> 枚相同的鸡蛋，并可以使用一栋从第 <code>1</code> 层到第 <code>n</code> 层共有 <code>n</code> 层楼的建筑。</p>

<p>已知存在楼层 <code>f</code> ，满足 <code>0 <= f <= n</code> ，任何从<strong> 高于</strong> <code>f</code> 的楼层落下的鸡蛋都会碎，从 <code>f</code> 楼层或比它低的楼层落下的鸡蛋都不会破。</p>

<p>每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 <code>x</code> 扔下（满足 <code>1 <= x <= n</code>）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 <strong>重复使用</strong> 这枚鸡蛋。</p>

<p>请你计算并返回要确定 <code>f</code> <strong>确切的值</strong> 的 <strong>最小操作次数</strong> 是多少？</p>
 

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 1, n = 2
<strong>输出：</strong>2
<strong>解释：</strong>
鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
如果它没碎，那么肯定能得出 f = 2 。 
因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 2, n = 6
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>k = 3, n = 14
<strong>输出：</strong>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k <= 100</code></li>
	<li><code>1 <= n <= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 二分查找
- 动态规划

## 示例

```
1
2
2
6
3
14
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int superEggDrop(int k, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int superEggDrop(int k, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
```

### C

```c
int superEggDrop(int k, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int SuperEggDrop(int k, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var superEggDrop = function(k, n) {
    
};
```

### TypeScript

```typescript
function superEggDrop(k: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function superEggDrop($k, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func superEggDrop(_ k: Int, _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun superEggDrop(k: Int, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int superEggDrop(int k, int n) {
    
  }
}
```

### Go

```golang
func superEggDrop(k int, n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def super_egg_drop(k, n)
    
end
```

### Scala

```scala
object Solution {
    def superEggDrop(k: Int, n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn super_egg_drop(k: i32, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (super-egg-drop k n)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec super_egg_drop(K :: integer(), N :: integer()) -> integer().
super_egg_drop(K, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec super_egg_drop(k :: integer, n :: integer) :: integer
  def super_egg_drop(k, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func superEggDrop(k: Int64, n: Int64): Int64 {

    }
}
```

