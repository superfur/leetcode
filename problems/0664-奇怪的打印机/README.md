# 664. 奇怪的打印机

## 题目描述

<p>有台奇怪的打印机有以下两个特殊要求：</p>

<ul>
	<li>打印机每次只能打印由 <strong>同一个字符</strong> 组成的序列。</li>
	<li>每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。</li>
</ul>

<p>给你一个字符串 <code>s</code> ，你的任务是计算这个打印机打印它需要的最少打印次数。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aaabbb"
<strong>输出：</strong>2
<strong>解释：</strong>首先打印 "aaa" 然后打印 "bbb"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aba"
<strong>输出：</strong>2
<strong>解释：</strong>首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 示例

```
"aaabbb"
"aba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int strangePrinter(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int strangePrinter(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def strangePrinter(self, s: str) -> int:
        
```

### C

```c
int strangePrinter(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int StrangePrinter(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var strangePrinter = function(s) {
    
};
```

### TypeScript

```typescript
function strangePrinter(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function strangePrinter($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func strangePrinter(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun strangePrinter(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int strangePrinter(String s) {
    
  }
}
```

### Go

```golang
func strangePrinter(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def strange_printer(s)
    
end
```

### Scala

```scala
object Solution {
    def strangePrinter(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn strange_printer(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (strange-printer s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec strange_printer(S :: unicode:unicode_binary()) -> integer().
strange_printer(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec strange_printer(s :: String.t) :: integer
  def strange_printer(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func strangePrinter(s: String): Int64 {

    }
}
```

