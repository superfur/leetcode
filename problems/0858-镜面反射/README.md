# 858. 镜面反射

## 题目描述

<p>有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为&nbsp;<code>0</code>，&nbsp;<code>1</code>，以及&nbsp;<code>2</code>。</p>

<p>正方形房间的墙壁长度为&nbsp;<code>p</code>，一束激光从西南角射出，首先会与东墙相遇，入射点到接收器 <code>0</code> 的距离为 <code>q</code> 。</p>

<p>返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。</p>
&nbsp;

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/18/reflection.png" style="width: 218px; height: 217px;" />
<pre>
<strong>输入：</strong>p = 2, q = 1
<strong>输出：</strong>2
<strong>解释：</strong>这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>p = 3, q = 1
<strong>输入：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= q &lt;= p &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数学
- 数论

## 示例

```
2
1
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int mirrorReflection(int p, int q) {
        
    }
};
```

### Java

```java
class Solution {
    public int mirrorReflection(int p, int q) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
```

### C

```c
int mirrorReflection(int p, int q) {
    
}
```

### C#

```csharp
public class Solution {
    public int MirrorReflection(int p, int q) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} p
 * @param {number} q
 * @return {number}
 */
var mirrorReflection = function(p, q) {
    
};
```

### TypeScript

```typescript
function mirrorReflection(p: number, q: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $p
     * @param Integer $q
     * @return Integer
     */
    function mirrorReflection($p, $q) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mirrorReflection(_ p: Int, _ q: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mirrorReflection(p: Int, q: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int mirrorReflection(int p, int q) {
    
  }
}
```

### Go

```golang
func mirrorReflection(p int, q int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} p
# @param {Integer} q
# @return {Integer}
def mirror_reflection(p, q)
    
end
```

### Scala

```scala
object Solution {
    def mirrorReflection(p: Int, q: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn mirror_reflection(p: i32, q: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (mirror-reflection p q)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec mirror_reflection(P :: integer(), Q :: integer()) -> integer().
mirror_reflection(P, Q) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec mirror_reflection(p :: integer, q :: integer) :: integer
  def mirror_reflection(p, q) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mirrorReflection(p: Int64, q: Int64): Int64 {

    }
}
```

