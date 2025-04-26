# 202. 快乐数

## 题目描述

<p>编写一个算法来判断一个数 <code>n</code> 是不是快乐数。</p>

<p><strong>「快乐数」</strong>&nbsp;定义为：</p>

<ul>
	<li>对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。</li>
	<li>然后重复这个过程直到这个数变为 1，也可能是 <strong>无限循环</strong> 但始终变不到 1。</li>
	<li>如果这个过程 <strong>结果为</strong>&nbsp;1，那么这个数就是快乐数。</li>
</ul>

<p>如果 <code>n</code> 是 <em>快乐数</em> 就返回 <code>true</code> ；不是，则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 19
<strong>输出：</strong>true
<strong>解释：
</strong>1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 数学
- 双指针

## 示例

```
19
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isHappy(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isHappy(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isHappy(self, n: int) -> bool:
        
```

### C

```c
bool isHappy(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsHappy(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    
};
```

### TypeScript

```typescript
function isHappy(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isHappy($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isHappy(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isHappy(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isHappy(int n) {
    
  }
}
```

### Go

```golang
func isHappy(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def is_happy(n)
    
end
```

### Scala

```scala
object Solution {
    def isHappy(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_happy(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-happy n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_happy(N :: integer()) -> boolean().
is_happy(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_happy(n :: integer) :: boolean
  def is_happy(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isHappy(n: Int64): Bool {

    }
}
```

