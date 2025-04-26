# 2543. 判断一个点是否可以到达

## 题目描述

<p>给你一个无穷大的网格图。一开始你在&nbsp;<code>(1, 1)</code>&nbsp;，你需要通过有限步移动到达点&nbsp;<code>(targetX, targetY)</code>&nbsp;。</p>

<p><b>每一步</b>&nbsp;，你可以从点&nbsp;<code>(x, y)</code>&nbsp;移动到以下点之一：</p>

<ul>
	<li><code>(x, y - x)</code></li>
	<li><code>(x - y, y)</code></li>
	<li><code>(2 * x, y)</code></li>
	<li><code>(x, 2 * y)</code></li>
</ul>

<p>给你两个整数&nbsp;<code>targetX</code> 和&nbsp;<code>targetY</code>&nbsp;，分别表示你最后需要到达点的 X 和 Y 坐标。如果你可以从&nbsp;<code>(1, 1)</code>&nbsp;出发到达这个点，请你返回<code>true</code> ，否则返回<em>&nbsp;</em><code>false</code><em>&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>targetX = 6, targetY = 9
<b>输出：</b>false
<b>解释：</b>没法从 (1,1) 出发到达 (6,9) ，所以返回 false 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>targetX = 4, targetY = 7
<b>输出：</b>true
<b>解释：</b>你可以按照以下路径到达：(1,1) -&gt; (1,2) -&gt; (1,4) -&gt; (1,8) -&gt; (1,7) -&gt; (2,7) -&gt; (4,7) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= targetX, targetY&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 数论

## 提示

1. Let’s go in reverse order, from (targetX, targetY) to (1, 1). So, now we can move from (x, y) to (x+y, y), (x, y+x), (x/2, y) if x is even, and (x, y/2) if y is even.
2. When is it optimal to use the third and fourth operations?
3. Think how GCD of (x, y) is affected if we apply the first two operations.
4. How can we check if we can reach (1, 1) using the GCD value calculate above?

## 示例

```
6
9
4
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isReachable(int targetX, int targetY) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isReachable(int targetX, int targetY) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isReachable(self, targetX, targetY):
        """
        :type targetX: int
        :type targetY: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        
```

### C

```c
bool isReachable(int targetX, int targetY) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsReachable(int targetX, int targetY) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} targetX
 * @param {number} targetY
 * @return {boolean}
 */
var isReachable = function(targetX, targetY) {
    
};
```

### TypeScript

```typescript
function isReachable(targetX: number, targetY: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $targetX
     * @param Integer $targetY
     * @return Boolean
     */
    function isReachable($targetX, $targetY) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isReachable(_ targetX: Int, _ targetY: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isReachable(targetX: Int, targetY: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isReachable(int targetX, int targetY) {
    
  }
}
```

### Go

```golang
func isReachable(targetX int, targetY int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} target_x
# @param {Integer} target_y
# @return {Boolean}
def is_reachable(target_x, target_y)
    
end
```

### Scala

```scala
object Solution {
    def isReachable(targetX: Int, targetY: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_reachable(target_x: i32, target_y: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-reachable targetX targetY)
  (-> exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_reachable(TargetX :: integer(), TargetY :: integer()) -> boolean().
is_reachable(TargetX, TargetY) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_reachable(target_x :: integer, target_y :: integer) :: boolean
  def is_reachable(target_x, target_y) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isReachable(targetX: Int64, targetY: Int64): Bool {

    }
}
```

