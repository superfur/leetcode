# 1525. 字符串的好分割数目

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，一个分割被称为 「好分割」&nbsp;当它满足：将&nbsp;<code>s</code>&nbsp;分割成 2 个字符串&nbsp;<code>p</code> 和&nbsp;<code>q</code>&nbsp;，它们连接起来等于&nbsp;<code>s</code>&nbsp;且 <code>p</code>&nbsp;和 <code>q</code>&nbsp;中不同字符的数目相同。</p>

<p>请你返回 <code>s</code>&nbsp;中好分割的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;aacaba&quot;
<strong>输出：</strong>2
<strong>解释：</strong>总共有 5 种分割字符串 <code>&quot;aacaba&quot;</code> 的方法，其中 2 种是好分割。
(&quot;a&quot;, &quot;acaba&quot;) 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
(&quot;aa&quot;, &quot;caba&quot;) 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
(&quot;aac&quot;, &quot;aba&quot;) 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
(&quot;aaca&quot;, &quot;ba&quot;) 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
(&quot;aacab&quot;, &quot;a&quot;) 左边字符串和右边字符串分别包含 3 个和 1 个不同的字符。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcd&quot;
<strong>输出：</strong>1
<strong>解释：</strong>好分割为将字符串分割成 (&quot;ab&quot;, &quot;cd&quot;) 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;aaaaa&quot;
<strong>输出：</strong>4
<strong>解释：</strong>所有分割都是好分割。</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;acbadbaada&quot;
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 哈希表
- 字符串
- 动态规划

## 提示

1. Use two HashMap to store the counts of distinct letters in the left and right substring divided by the current index.

## 示例

```
"aacaba"
"abcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSplits(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSplits(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSplits(self, s: str) -> int:
        
```

### C

```c
int numSplits(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSplits(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numSplits = function(s) {
    
};
```

### TypeScript

```typescript
function numSplits(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSplits($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSplits(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSplits(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSplits(String s) {
    
  }
}
```

### Go

```golang
func numSplits(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def num_splits(s)
    
end
```

### Scala

```scala
object Solution {
    def numSplits(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_splits(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-splits s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_splits(S :: unicode:unicode_binary()) -> integer().
num_splits(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_splits(s :: String.t) :: integer
  def num_splits(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSplits(s: String): Int64 {

    }
}
```

