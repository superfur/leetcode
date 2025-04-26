# 2514. 统计同位异构字符串数目

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它包含一个或者多个单词。单词之间用单个空格&nbsp;<code>' '</code>&nbsp;隔开。</p>

<p>如果字符串 <code>t</code>&nbsp;中第 <code>i</code>&nbsp;个单词是 <code>s</code>&nbsp;中第 <code>i</code>&nbsp;个单词的一个&nbsp;<strong>排列</strong>&nbsp;，那么我们称字符串&nbsp;<code>t</code>&nbsp;是字符串&nbsp;<code>s</code>&nbsp;的同位异构字符串。</p>

<ul>
	<li>比方说，<code>"acb dfe"</code>&nbsp;是&nbsp;<code>"abc def"</code>&nbsp;的同位异构字符串，但是&nbsp;<code>"def cab"</code>&nbsp;和&nbsp;<code>"adc bef"</code>&nbsp;不是。</li>
</ul>

<p>请你返回<em>&nbsp;</em><code>s</code>&nbsp;的同位异构字符串的数目，由于答案可能很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong> 后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "too hot"
<b>输出：</b>18
<b>解释：</b>输入字符串的一些同位异构字符串为 "too hot" ，"oot hot" ，"oto toh" ，"too toh" 以及 "too oht" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "aa"
<b>输出：</b>1
<strong>解释：</strong>输入字符串只有一个同位异构字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 只包含小写英文字母和空格&nbsp;<code>' '</code>&nbsp;。</li>
	<li>相邻单词之间由单个空格隔开。</li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 数学
- 字符串
- 组合数学
- 计数

## 提示

1. For each word, can you count the number of permutations possible if all characters are distinct?
2. How to reduce overcounting when letters are repeated?
3. The product of the counts of distinct permutations of all words will give the final answer.

## 示例

```
"too hot"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countAnagrams(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countAnagrams(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countAnagrams(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countAnagrams(self, s: str) -> int:
        
```

### C

```c
int countAnagrams(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountAnagrams(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countAnagrams = function(s) {
    
};
```

### TypeScript

```typescript
function countAnagrams(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countAnagrams($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countAnagrams(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countAnagrams(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countAnagrams(String s) {
    
  }
}
```

### Go

```golang
func countAnagrams(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_anagrams(s)
    
end
```

### Scala

```scala
object Solution {
    def countAnagrams(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_anagrams(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-anagrams s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_anagrams(S :: unicode:unicode_binary()) -> integer().
count_anagrams(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_anagrams(s :: String.t) :: integer
  def count_anagrams(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countAnagrams(s: String): Int64 {

    }
}
```

