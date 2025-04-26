# 2729. 判断一个数是否迷人

## 题目描述

<p>给你一个三位数整数 <code>n</code>&nbsp;。</p>

<p>如果经过以下修改得到的数字 <strong>恰好</strong>&nbsp;包含数字 <code>1</code>&nbsp;到 <code>9</code>&nbsp;各一次且不包含任何 <code>0</code>&nbsp;，那么我们称数字 <code>n</code>&nbsp;是 <strong>迷人的</strong>&nbsp;：</p>

<ul>
	<li>将&nbsp;<code>n</code>&nbsp;与数字&nbsp;<code>2 * n</code> 和&nbsp;<code>3 * n</code>&nbsp;<strong>连接</strong>&nbsp;。</li>
</ul>

<p>如果 <code>n</code>&nbsp;是迷人的，返回&nbsp;<code>true</code>，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p><strong>连接</strong>&nbsp;两个数字表示把它们首尾相接连在一起。比方说&nbsp;<code>121</code> 和&nbsp;<code>371</code>&nbsp;连接得到&nbsp;<code>121371</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 192
<b>输出：</b>true
<b>解释：</b>我们将数字 n = 192 ，2 * n = 384 和 3 * n = 576 连接，得到 192384576 。这个数字包含 1 到 9 恰好各一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 100
<b>输出：</b>false
<b>解释：</b>我们将数字 n = 100 ，2 * n = 200 和 3 * n = 300 连接，得到 100200300 。这个数字不符合上述条件。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>100 &lt;= n &lt;= 999</code></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 数学

## 提示

1. Consider changing the number to the way it is described in the statement.
2. Check if the resulting number contains all the digits from 1 to 9 exactly once.

## 示例

```
192
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isFascinating(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isFascinating(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isFascinating(self, n: int) -> bool:
        
```

### C

```c
bool isFascinating(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsFascinating(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isFascinating = function(n) {
    
};
```

### TypeScript

```typescript
function isFascinating(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isFascinating($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isFascinating(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isFascinating(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isFascinating(int n) {
    
  }
}
```

### Go

```golang
func isFascinating(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def is_fascinating(n)
    
end
```

### Scala

```scala
object Solution {
    def isFascinating(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_fascinating(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-fascinating n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_fascinating(N :: integer()) -> boolean().
is_fascinating(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_fascinating(n :: integer) :: boolean
  def is_fascinating(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isFascinating(n: Int64): Bool {

    }
}
```

