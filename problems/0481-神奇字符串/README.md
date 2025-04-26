# 481. 神奇字符串

## 题目描述

<p>神奇字符串 <code>s</code> 仅由 <code>'1'</code> 和 <code>'2'</code> 组成，并需要遵守下面的规则：</p>

<ul>
	<li>神奇字符串 s 的神奇之处在于，串联字符串中 <code>'1'</code> 和 <code>'2'</code> 的连续出现次数可以生成该字符串。</li>
</ul>

<p><code>s</code> 的前几个元素是 <code>s = "1221121221221121122……"</code> 。如果将 <code>s</code> 中连续的若干 <code>1</code> 和 <code>2</code> 进行分组，可以得到 <code>"1 22 11 2 1 22 1 22 11 2 11 22 ......"</code> 。每组中 <code>1</code> 或者 <code>2</code> 的出现次数分别是 <code>"1 2 2 1 1 2 1 2 2 1 2 2 ......"</code> 。上面的出现次数正是 <code>s</code> 自身。</p>

<p>给你一个整数 <code>n</code> ，返回在神奇字符串 <code>s</code> 的前 <code>n</code> 个数字中 <code>1</code> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 6
<strong>输出：</strong>3
<strong>解释：</strong>神奇字符串 s 的前 6 个元素是 “<code>122112</code>”，它包含三个 1，因此返回 3 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 示例

```
6
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int magicalString(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int magicalString(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def magicalString(self, n: int) -> int:
        
```

### C

```c
int magicalString(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MagicalString(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var magicalString = function(n) {
    
};
```

### TypeScript

```typescript
function magicalString(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function magicalString($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func magicalString(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun magicalString(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int magicalString(int n) {
    
  }
}
```

### Go

```golang
func magicalString(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def magical_string(n)
    
end
```

### Scala

```scala
object Solution {
    def magicalString(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn magical_string(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (magical-string n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec magical_string(N :: integer()) -> integer().
magical_string(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec magical_string(n :: integer) :: integer
  def magical_string(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func magicalString(n: Int64): Int64 {

    }
}
```

