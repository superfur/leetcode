# 2953. 统计完全子字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>word</code>&nbsp;和一个整数 <code>k</code>&nbsp;。</p>

<p>如果&nbsp;<code>word</code>&nbsp;的一个子字符串 <code>s</code>&nbsp;满足以下条件，我们称它是 <strong>完全字符串：</strong></p>

<ul>
	<li><code>s</code>&nbsp;中每个字符 <strong>恰好</strong>&nbsp;出现 <code>k</code>&nbsp;次。</li>
	<li>相邻字符在字母表中的顺序 <strong>至多</strong>&nbsp;相差&nbsp;<code>2</code>&nbsp;。也就是说，<code>s</code>&nbsp;中两个相邻字符&nbsp;<code>c1</code> 和&nbsp;<code>c2</code>&nbsp;，它们在字母表中的位置相差<strong>&nbsp;至多</strong>&nbsp;为 <code>2</code> 。</li>
</ul>

<p>请你返回 <code>word</code>&nbsp;中 <strong>完全</strong>&nbsp;子字符串的数目。</p>

<p><strong>子字符串</strong>&nbsp;指的是一个字符串中一段连续 <strong>非空</strong>&nbsp;的字符序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>word = "igigee", k = 2
<b>输出：</b>3
<b>解释：</b>完全子字符串需要满足每个字符恰好出现 2 次，且相邻字符相差至多为 2 ：<em><strong>igig</strong></em>ee, igig<strong style="font-style: italic;">ee</strong>, <em><strong>igigee</strong>&nbsp;。</em>
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>word = "aaabbbccc", k = 3
<b>输出：</b>6
<b>解释：</b>完全子字符串需要满足每个字符恰好出现 3 次，且相邻字符相差至多为 2 ：<em><strong>aaa</strong></em>bbbccc, aaa<em><strong>bbb</strong></em>ccc, aaabbb<em><strong>ccc</strong></em>, <em><strong>aaabbb</strong></em>ccc, aaa<em><strong>bbbccc</strong></em>, <em><strong>aaabbbccc </strong></em>。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
	<li><code>1 &lt;= k &lt;= word.length</code></li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. There are at most 26 different lengths of the complete substrings: <code>k *1, k * 2, … k * 26</code>.****
2. For each length, we can use sliding window to count the frequency of each letter in the window.
3. We still need to check for all characters in the window that <code>abs(word[i] - word[i - 1]) <= 2</code>. We do this by maintaining the values of <code>abs(word[i] - word[i - 1])</code> in the sliding window dynamically in an ordered multiset or priority queue, so that we know the maximum value at each iteration.

## 示例

```
"igigee"
2
"aaabbbccc"
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCompleteSubstrings(string word, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCompleteSubstrings(String word, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        
```

### C

```c
int countCompleteSubstrings(char* word, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCompleteSubstrings(string word, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var countCompleteSubstrings = function(word, k) {
    
};
```

### TypeScript

```typescript
function countCompleteSubstrings(word: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function countCompleteSubstrings($word, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCompleteSubstrings(_ word: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCompleteSubstrings(word: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCompleteSubstrings(String word, int k) {
    
  }
}
```

### Go

```golang
func countCompleteSubstrings(word string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_complete_substrings(word, k)
    
end
```

### Scala

```scala
object Solution {
    def countCompleteSubstrings(word: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_complete_substrings(word: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-complete-substrings word k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_complete_substrings(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
count_complete_substrings(Word, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_complete_substrings(word :: String.t, k :: integer) :: integer
  def count_complete_substrings(word, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCompleteSubstrings(word: String, k: Int64): Int64 {

    }
}
```

