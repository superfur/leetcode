# 面试题 16.26. 计算器

## 题目描述

<p>给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。</p>

<p>表达式仅包含非负整数，<code>+</code>， <code>-</code> ，<code>*</code>，<code>/</code> 四种运算符和空格&nbsp;<code>&nbsp;</code>。 整数除法仅保留整数部分。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>"3+2*2"
<strong>输出：</strong>7
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>" 3/2 "
<strong>输出：</strong>1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>" 3+5 / 2 "
<strong>输出：</strong>5
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>你可以假设所给定的表达式都是有效的。</li>
	<li>请<strong>不要</strong>使用内置的库函数 <code>eval</code>。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数学
- 字符串

## 提示

1. 我们可以从左到右处理表达式吗？为什么会失败？
2. 乘法和除法是优先级较高的运算。在3*4 + 5*9/2 + 3这样的表达式中，乘法和除法部分需要组合在一起。
3. 把它想成当你遇到乘法或除法时，跳至一个单独的“进程”来计算该结果。
4. 你还可以维护两个栈，一个用于操作符，另一个用于数字。每次看到一个数字，就把它压入栈。那么操作符呢？什么时候从栈中取出操作符并将它们与数字进行计算？

## 示例

```
"3+2*2"
" 3/2 "
" 3+5 / 2 "
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int calculate(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int calculate(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def calculate(self, s: str) -> int:
        
```

### C

```c
int calculate(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int Calculate(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    
};
```

### TypeScript

```typescript
function calculate(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func calculate(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun calculate(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int calculate(String s) {
    
  }
}
```

### Go

```golang
func calculate(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def calculate(s)
    
end
```

### Scala

```scala
object Solution {
    def calculate(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn calculate(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (calculate s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec calculate(S :: unicode:unicode_binary()) -> integer().
calculate(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec calculate(s :: String.t) :: integer
  def calculate(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func calculate(s: String): Int64 {

    }
}
```

