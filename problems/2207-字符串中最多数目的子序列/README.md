# 2207. 字符串中最多数目的子序列

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>text</code>&nbsp;和另一个下标从 <strong>0</strong>&nbsp;开始且长度为 <code>2</code>&nbsp;的字符串&nbsp;<code>pattern</code>&nbsp;，两者都只包含小写英文字母。</p>

<p>你可以在 <code>text</code>&nbsp;中任意位置插入 <strong>一个</strong> 字符，这个插入的字符必须是&nbsp;<code>pattern[0]</code>&nbsp;<b>或者</b>&nbsp;<code>pattern[1]</code>&nbsp;。注意，这个字符可以插入在 <code>text</code>&nbsp;开头或者结尾的位置。</p>

<p>请你返回插入一个字符后，<code>text</code>&nbsp;中最多包含多少个等于 <code>pattern</code>&nbsp;的 <strong>子序列</strong>&nbsp;。</p>

<p><strong>子序列</strong> 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>text = "abdcdbc", pattern = "ac"
<b>输出：</b>4
<strong>解释：</strong>
如果我们在 text[1] 和 text[2] 之间添加 pattern[0] = 'a' ，那么我们得到 "ab<em><strong>a</strong></em>dcdbc" 。那么 "ac" 作为子序列出现 4 次。
其他得到 4 个 "ac" 子序列的方案还有 "<em><strong>a</strong></em>abdcdbc" 和 "abd<em><strong>a</strong></em>cdbc" 。
但是，"abdc<em><strong>a</strong></em>dbc" ，"abd<em><strong>c</strong></em>cdbc" 和 "abdcdbc<em><strong>c</strong></em>" 这些字符串虽然是可行的插入方案，但是只出现了 3 次 "ac" 子序列，所以不是最优解。
可以证明插入一个字符后，无法得到超过 4 个 "ac" 子序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>text = "aabb", pattern = "ab"
<b>输出：</b>6
<strong>解释：</strong>
可以得到 6 个 "ab" 子序列的部分方案为 "<em><strong>a</strong></em>aabb" ，"aa<em><strong>a</strong></em>bb" 和 "aab<em><strong>b</strong></em>b" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>5</sup></code></li>
	<li><code>pattern.length == 2</code></li>
	<li><code>text</code> 和&nbsp;<code>pattern</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 前缀和

## 提示

1. Find the optimal position to add pattern[0] so that the number of subsequences is maximized. Similarly, find the optimal position to add pattern[1].
2. For each of the above cases, count the number of times the pattern occurs as a subsequence in text. The larger count is the required answer.

## 示例

```
"abdcdbc"
"ac"
"aabb"
"ab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumSubsequenceCount(string text, string pattern) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumSubsequenceCount(String text, String pattern) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
```

### C

```c
long long maximumSubsequenceCount(char* text, char* pattern) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumSubsequenceCount(string text, string pattern) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @param {string} pattern
 * @return {number}
 */
var maximumSubsequenceCount = function(text, pattern) {
    
};
```

### TypeScript

```typescript
function maximumSubsequenceCount(text: string, pattern: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @param String $pattern
     * @return Integer
     */
    function maximumSubsequenceCount($text, $pattern) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSubsequenceCount(_ text: String, _ pattern: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSubsequenceCount(text: String, pattern: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSubsequenceCount(String text, String pattern) {
    
  }
}
```

### Go

```golang
func maximumSubsequenceCount(text string, pattern string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} text
# @param {String} pattern
# @return {Integer}
def maximum_subsequence_count(text, pattern)
    
end
```

### Scala

```scala
object Solution {
    def maximumSubsequenceCount(text: String, pattern: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_subsequence_count(text: String, pattern: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-subsequence-count text pattern)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_subsequence_count(Text :: unicode:unicode_binary(), Pattern :: unicode:unicode_binary()) -> integer().
maximum_subsequence_count(Text, Pattern) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_subsequence_count(text :: String.t, pattern :: String.t) :: integer
  def maximum_subsequence_count(text, pattern) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSubsequenceCount(text: String, pattern: String): Int64 {

    }
}
```

