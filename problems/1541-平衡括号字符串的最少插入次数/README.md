# 1541. 平衡括号字符串的最少插入次数

## 题目描述

<p>给你一个括号字符串&nbsp;<code>s</code>&nbsp;，它只包含字符&nbsp;<code>&#39;(&#39;</code> 和&nbsp;<code>&#39;)&#39;</code>&nbsp;。一个括号字符串被称为平衡的当它满足：</p>

<ul>
	<li>任何左括号&nbsp;<code>&#39;(&#39;</code>&nbsp;必须对应两个连续的右括号&nbsp;<code>&#39;))&#39;</code>&nbsp;。</li>
	<li>左括号&nbsp;<code>&#39;(&#39;</code>&nbsp;必须在对应的连续两个右括号&nbsp;<code>&#39;))&#39;</code>&nbsp;之前。</li>
</ul>

<p>比方说&nbsp;<code>&quot;())&quot;</code>，&nbsp;<code>&quot;())(())))&quot;</code> 和&nbsp;<code>&quot;(())())))&quot;</code>&nbsp;都是平衡的，&nbsp;<code>&quot;)()&quot;</code>，&nbsp;<code>&quot;()))&quot;</code> 和&nbsp;<code>&quot;(()))&quot;</code>&nbsp;都是不平衡的。</p>

<p>你可以在任意位置插入字符 &#39;(&#39; 和 &#39;)&#39; 使字符串平衡。</p>

<p>请你返回让 <code>s</code>&nbsp;平衡的最少插入次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;(()))&quot;
<strong>输出：</strong>1
<strong>解释：</strong>第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 &#39;)&#39; 使字符串变成平衡字符串 &quot;(())))&quot; 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;())&quot;
<strong>输出：</strong>0
<strong>解释：</strong>字符串已经平衡了。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;))())(&quot;
<strong>输出：</strong>3
<strong>解释：</strong>添加 &#39;(&#39; 去匹配最开头的 &#39;))&#39; ，然后添加 &#39;))&#39; 去匹配最后一个 &#39;(&#39; 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;((((((&quot;
<strong>输出：</strong>12
<strong>解释：</strong>添加 12 个 &#39;)&#39; 得到平衡字符串。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>s = &quot;)))))))&quot;
<strong>输出：</strong>5
<strong>解释：</strong>在字符串开头添加 4 个 &#39;(&#39; 并在结尾添加 1 个 &#39;)&#39; ，字符串变成平衡字符串 &quot;(((())))))))&quot; 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s</code>&nbsp;只包含&nbsp;<code>&#39;(&#39;</code> 和&nbsp;<code>&#39;)&#39;</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串

## 提示

1. Use a stack to keep opening brackets. If you face single closing ')' add 1 to the answer and consider it as '))'.
2. If you have '))' with empty stack, add 1 to the answer, If after finishing you have x opening remaining in the stack, add 2x to the answer.

## 示例

```
"(()))"
"())"
"))())("
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minInsertions(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minInsertions(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minInsertions(self, s: str) -> int:
        
```

### C

```c
int minInsertions(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinInsertions(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    
};
```

### TypeScript

```typescript
function minInsertions(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minInsertions($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minInsertions(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minInsertions(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minInsertions(String s) {
    
  }
}
```

### Go

```golang
func minInsertions(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_insertions(s)
    
end
```

### Scala

```scala
object Solution {
    def minInsertions(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-insertions s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_insertions(S :: unicode:unicode_binary()) -> integer().
min_insertions(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_insertions(s :: String.t) :: integer
  def min_insertions(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minInsertions(s: String): Int64 {

    }
}
```

