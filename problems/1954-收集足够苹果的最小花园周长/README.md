# 1954. 收集足够苹果的最小花园周长

## 题目描述

<p>给你一个用无限二维网格表示的花园，<strong>每一个</strong>&nbsp;整数坐标处都有一棵苹果树。整数坐标&nbsp;<code>(i, j)</code>&nbsp;处的苹果树有 <code>|i| + |j|</code>&nbsp;个苹果。</p>

<p>你将会买下正中心坐标是 <code>(0, 0)</code>&nbsp;的一块 <strong>正方形土地</strong>&nbsp;，且每条边都与两条坐标轴之一平行。</p>

<p>给你一个整数&nbsp;<code>neededApples</code>&nbsp;，请你返回土地的&nbsp;<strong>最小周长</strong>&nbsp;，使得&nbsp;<strong>至少</strong>&nbsp;有<strong>&nbsp;</strong><code>neededApples</code>&nbsp;个苹果在土地&nbsp;<strong>里面或者边缘上</strong>。</p>

<p><code>|x|</code>&nbsp;的值定义为：</p>

<ul>
	<li>如果&nbsp;<code>x &gt;= 0</code>&nbsp;，那么值为&nbsp;<code>x</code></li>
	<li>如果&nbsp;<code>x &lt;&nbsp;0</code>&nbsp;，那么值为&nbsp;<code>-x</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode-cn.com/1627790803-qcBKFw-image.png" style="width: 442px; height: 449px;" />
<pre>
<b>输入：</b>neededApples = 1
<b>输出：</b>8
<b>解释：</b>边长长度为 1 的正方形不包含任何苹果。
但是边长为 2 的正方形包含 12 个苹果（如上图所示）。
周长为 2 * 4 = 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>neededApples = 13
<b>输出：</b>16
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>neededApples = 1000000000
<b>输出：</b>5040
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= neededApples &lt;= 10<sup>15</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 二分查找

## 提示

1. Find a formula for the number of apples inside a square with a side length L.
2. Iterate over the possible lengths of the square until enough apples are collected.

## 示例

```
1
13
1000000000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumPerimeter(long long neededApples) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumPerimeter(long neededApples) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        
```

### C

```c
long long minimumPerimeter(long long neededApples) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumPerimeter(long neededApples) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} neededApples
 * @return {number}
 */
var minimumPerimeter = function(neededApples) {
    
};
```

### TypeScript

```typescript
function minimumPerimeter(neededApples: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $neededApples
     * @return Integer
     */
    function minimumPerimeter($neededApples) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumPerimeter(_ neededApples: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumPerimeter(neededApples: Long): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumPerimeter(int neededApples) {
    
  }
}
```

### Go

```golang
func minimumPerimeter(neededApples int64) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} needed_apples
# @return {Integer}
def minimum_perimeter(needed_apples)
    
end
```

### Scala

```scala
object Solution {
    def minimumPerimeter(neededApples: Long): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_perimeter(needed_apples: i64) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-perimeter neededApples)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_perimeter(NeededApples :: integer()) -> integer().
minimum_perimeter(NeededApples) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_perimeter(needed_apples :: integer) :: integer
  def minimum_perimeter(needed_apples) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumPerimeter(neededApples: Int64): Int64 {

    }
}
```

