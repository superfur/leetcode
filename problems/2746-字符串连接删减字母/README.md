# 2746. 字符串连接删减字母

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>words</code>&nbsp;，它包含 <code>n</code>&nbsp;个字符串。</p>

<p>定义 <strong>连接</strong>&nbsp;操作&nbsp;<code>join(x, y)</code>&nbsp;表示将字符串&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;连在一起，得到&nbsp;<code>xy</code>&nbsp;。如果&nbsp;<code>x</code>&nbsp;的最后一个字符与&nbsp;<code>y</code>&nbsp;的第一个字符相等，连接后两个字符中的一个会被&nbsp;<strong>删除</strong>&nbsp;。</p>

<p>比方说&nbsp;<code>join("ab", "ba") = "aba"</code>&nbsp;，&nbsp;<code>join("ab", "cde") = "abcde"</code>&nbsp;。</p>

<p>你需要执行&nbsp;<code>n - 1</code>&nbsp;次&nbsp;<strong>连接</strong>&nbsp;操作。令&nbsp;<code>str<sub>0</sub> = words[0]</code>&nbsp;，从&nbsp;<code>i = 1</code> 直到&nbsp;<code>i = n - 1</code>&nbsp;，对于第&nbsp;<code>i</code>&nbsp;个操作，你可以执行以下操作之一：</p>

<ul>
	<li>令&nbsp;<code>str<sub>i</sub> = join(str<sub>i - 1</sub>, words[i])</code></li>
	<li>令&nbsp;<code>str<sub>i</sub> = join(words[i], str<sub>i - 1</sub>)</code></li>
</ul>

<p>你的任务是使&nbsp;<code>str<sub>n - 1</sub></code>&nbsp;的长度<strong>&nbsp;最小&nbsp;</strong>。</p>

<p>请你返回一个整数，表示&nbsp;<code>str<sub>n - 1</sub></code>&nbsp;的最小长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["aa","ab","bc"]
<b>输出：</b>4
<strong>解释：</strong>这个例子中，我们按以下顺序执行连接操作，得到 <code>str<sub>2</sub></code> 的最小长度：
<code>str<sub>0</sub> = "aa"</code>
<code>str<sub>1</sub> = join(str<sub>0</sub>, "ab") = "aab"
</code><code>str<sub>2</sub> = join(str<sub>1</sub>, "bc") = "aabc"</code> 
<code>str<sub>2</sub></code> 的最小长度为 4 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["ab","b"]
<b>输出：</b>2
<b>解释：</b>这个例子中，str<sub>0</sub> = "ab"，可以得到两个不同的 str<sub>1</sub>：
join(str<sub>0</sub>, "b") = "ab" 或者 join("b", str<sub>0</sub>) = "bab" 。
第一个字符串 "ab" 的长度最短，所以答案为 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>words = ["aaa","c","aba"]
<b>输出：</b>6
<b>解释：</b>这个例子中，我们按以下顺序执行连接操作，得到 <code>str<sub>2</sub>&nbsp;的最小长度：</code>
<code>str<sub>0</sub> = "</code>aaa"
<code>str<sub>1</sub> = join(str<sub>0</sub>, "c") = "aaac"</code>
<code>str<sub>2</sub> = join("aba", str<sub>1</sub>) = "abaaac"</code>
<code>str<sub>2</sub></code> 的最小长度为 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>words[i]</code>&nbsp;中只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 动态规划

## 提示

1. Use dynamic programming with memoization.
2. Notice that the first and last characters of a string are sufficient to determine the length of its concatenation with any other string.
3. Define dp[i][first][last] as the shortest concatenation length of the first i words starting with a character first and ending with a character last. Convert characters to their ASCII codes if your programming language cannot implicitly convert them to array indices.

## 示例

```
["aa","ab","bc"]
["ab","b"]
["aaa","c","aba"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeConcatenatedLength(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeConcatenatedLength(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeConcatenatedLength(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        
```

### C

```c
int minimizeConcatenatedLength(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeConcatenatedLength(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var minimizeConcatenatedLength = function(words) {
    
};
```

### TypeScript

```typescript
function minimizeConcatenatedLength(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function minimizeConcatenatedLength($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeConcatenatedLength(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeConcatenatedLength(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeConcatenatedLength(List<String> words) {
    
  }
}
```

### Go

```golang
func minimizeConcatenatedLength(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def minimize_concatenated_length(words)
    
end
```

### Scala

```scala
object Solution {
    def minimizeConcatenatedLength(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_concatenated_length(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-concatenated-length words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_concatenated_length(Words :: [unicode:unicode_binary()]) -> integer().
minimize_concatenated_length(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_concatenated_length(words :: [String.t]) :: integer
  def minimize_concatenated_length(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeConcatenatedLength(words: Array<String>): Int64 {

    }
}
```

