# 2119. 反转两次的数字

## 题目描述

<p><strong>反转</strong> 一个整数意味着倒置它的所有位。</p>

<ul>
	<li>例如，反转 <code>2021</code> 得到 <code>1202</code> 。反转 <code>12300</code> 得到 <code>321</code> ，<strong>不保留前导零</strong> 。</li>
</ul>

<p>给你一个整数 <code>num</code> ，<strong>反转</strong> <code>num</code> 得到 <code>reversed1</code> ，<strong>接着反转</strong> <code>reversed1</code> 得到 <code>reversed2</code> 。如果 <code>reversed2</code> 等于 <code>num</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 526
<strong>输出：</strong>true
<strong>解释：</strong>反转 num 得到 625 ，接着反转 625 得到 526 ，等于 num 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = 1800
<strong>输出：</strong>false
<strong>解释：</strong>反转 num 得到 81 ，接着反转 81 得到 18 ，不等于 num 。 </pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = 0
<strong>输出：</strong>true
<strong>解释：</strong>反转 num 得到 0 ，接着反转 0 得到 0 ，等于 num 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Other than the number 0 itself, any number that ends with 0 would lose some digits permanently when reversed.

## 示例

```
526
1800
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isSameAfterReversals(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isSameAfterReversals(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
```

### C

```c
bool isSameAfterReversals(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsSameAfterReversals(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {boolean}
 */
var isSameAfterReversals = function(num) {
    
};
```

### TypeScript

```typescript
function isSameAfterReversals(num: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function isSameAfterReversals($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isSameAfterReversals(_ num: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isSameAfterReversals(num: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isSameAfterReversals(int num) {
    
  }
}
```

### Go

```golang
func isSameAfterReversals(num int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Boolean}
def is_same_after_reversals(num)
    
end
```

### Scala

```scala
object Solution {
    def isSameAfterReversals(num: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_same_after_reversals(num: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-same-after-reversals num)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_same_after_reversals(Num :: integer()) -> boolean().
is_same_after_reversals(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_same_after_reversals(num :: integer) :: boolean
  def is_same_after_reversals(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isSameAfterReversals(num: Int64): Bool {

    }
}
```

