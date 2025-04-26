# 1952. 三除数

## 题目描述

<p>给你一个整数 <code>n</code> 。如果 <code>n</code> <strong>恰好有三个正除数</strong> ，返回 <code>true</code><em> </em>；否则，返回<em> </em><code>false</code> 。</p>

<p>如果存在整数 <code>k</code> ，满足 <code>n = k * m</code> ，那么整数 <code>m</code> 就是 <code>n</code> 的一个 <strong>除数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>false
<strong>解释：</strong>2 只有两个除数：1 和 2 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>true
<strong>解释：</strong>4 有三个除数：1、2 和 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 枚举
- 数论

## 提示

1. You can count the number of divisors and just check that they are 3
2. Beware of the case of n equal 1 as some solutions might fail in it

## 示例

```
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isThree(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isThree(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isThree(self, n: int) -> bool:
        
```

### C

```c
bool isThree(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsThree(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isThree = function(n) {
    
};
```

### TypeScript

```typescript
function isThree(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isThree($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isThree(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isThree(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isThree(int n) {
    
  }
}
```

### Go

```golang
func isThree(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def is_three(n)
    
end
```

### Scala

```scala
object Solution {
    def isThree(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_three(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-three n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_three(N :: integer()) -> boolean().
is_three(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_three(n :: integer) :: boolean
  def is_three(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isThree(n: Int64): Bool {

    }
}
```

