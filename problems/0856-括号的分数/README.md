# 856. 括号的分数

## 题目描述

<p>给定一个平衡括号字符串&nbsp;<code>S</code>，按下述规则计算该字符串的分数：</p>

<ul>
	<li><code>()</code> 得 1 分。</li>
	<li><code>AB</code> 得&nbsp;<code>A + B</code>&nbsp;分，其中 A 和 B 是平衡括号字符串。</li>
	<li><code>(A)</code> 得&nbsp;<code>2 * A</code>&nbsp;分，其中 A 是平衡括号字符串。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入： </strong>&quot;()&quot;
<strong>输出： </strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入： </strong>&quot;(())&quot;
<strong>输出： </strong>2
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre><strong>输入： </strong>&quot;()()&quot;
<strong>输出： </strong>2
</pre>

<p><strong>示例&nbsp;4：</strong></p>

<pre><strong>输入： </strong>&quot;(()(()))&quot;
<strong>输出： </strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>S</code>&nbsp;是平衡括号字符串，且只含有&nbsp;<code>(</code>&nbsp;和&nbsp;<code>)</code>&nbsp;。</li>
	<li><code>2 &lt;= S.length &lt;= 50</code></li>
</ol>


## 难度

Medium

## 标签

- 栈
- 字符串

## 示例

```
"()"
"(())"
"()()"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int scoreOfParentheses(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int scoreOfParentheses(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
```

### C

```c
int scoreOfParentheses(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int ScoreOfParentheses(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var scoreOfParentheses = function(s) {
    
};
```

### TypeScript

```typescript
function scoreOfParentheses(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function scoreOfParentheses($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func scoreOfParentheses(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun scoreOfParentheses(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int scoreOfParentheses(String s) {
    
  }
}
```

### Go

```golang
func scoreOfParentheses(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def score_of_parentheses(s)
    
end
```

### Scala

```scala
object Solution {
    def scoreOfParentheses(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (score-of-parentheses s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec score_of_parentheses(S :: unicode:unicode_binary()) -> integer().
score_of_parentheses(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec score_of_parentheses(s :: String.t) :: integer
  def score_of_parentheses(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func scoreOfParentheses(s: String): Int64 {

    }
}
```

