# 2957. 消除相邻近似相等字符

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>word</code>&nbsp;。</p>

<p>一次操作中，你可以选择&nbsp;<code>word</code>&nbsp;中任意一个下标 <code>i</code>&nbsp;，将&nbsp;<code>word[i]</code> 修改成任意一个小写英文字母。</p>

<p>请你返回消除 <code>word</code>&nbsp;中所有相邻 <strong>近似相等</strong>&nbsp;字符的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>两个字符&nbsp;<code>a</code> 和&nbsp;<code>b</code>&nbsp;如果满足&nbsp;<code>a == b</code>&nbsp;或者&nbsp;<code>a</code> 和&nbsp;<code>b</code>&nbsp;在字母表中是相邻的，那么我们称它们是 <strong>近似相等</strong>&nbsp;字符。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>word = "aaaaa"
<b>输出：</b>2
<b>解释：</b>我们将 word 变为 "a<em><strong>c</strong></em>a<em><strong>c</strong></em>a" ，该字符串没有相邻近似相等字符。
消除 word 中所有相邻近似相等字符最少需要 2 次操作。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>word = "abddez"
<b>输出：</b>2
<b>解释：</b>我们将 word 变为 "<em><strong>y</strong></em>bd<em><strong>o</strong></em>ez" ，该字符串没有相邻近似相等字符。
消除 word 中所有相邻近似相等字符最少需要 2 次操作。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>word = "zyxyxyz"
<b>输出：</b>3
<b>解释：</b>我们将 word 变为 "z<em><strong>a</strong></em>x<em><strong>a</strong></em>x<em><strong>a</strong></em>z" ，该字符串没有相邻近似相等字符。
消除 word 中所有相邻近似相等字符最少需要 3 次操作
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 动态规划

## 提示

1. For <code>i > 0</code>, if <code>word[i]</code> and <code>word[i - 1]</code> are adjacent, we will change <code>word[i]</code> to another character. Which character should we change it to?
2. We will change <code>word[i]</code> to some character that is not adjacent to <code>word[i - 1]</code> nor <code>word[i + 1]</code> (if it exists). Such a character always exists. However, since the problem does not ask for the final state of the string, It is enough to prove that the character exists and we do not need to find it.

## 示例

```
"aaaaa"
"abddez"
"zyxyxyz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int removeAlmostEqualCharacters(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int removeAlmostEqualCharacters(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
```

### C

```c
int removeAlmostEqualCharacters(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int RemoveAlmostEqualCharacters(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var removeAlmostEqualCharacters = function(word) {
    
};
```

### TypeScript

```typescript
function removeAlmostEqualCharacters(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function removeAlmostEqualCharacters($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeAlmostEqualCharacters(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeAlmostEqualCharacters(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int removeAlmostEqualCharacters(String word) {
    
  }
}
```

### Go

```golang
func removeAlmostEqualCharacters(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def remove_almost_equal_characters(word)
    
end
```

### Scala

```scala
object Solution {
    def removeAlmostEqualCharacters(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_almost_equal_characters(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (remove-almost-equal-characters word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec remove_almost_equal_characters(Word :: unicode:unicode_binary()) -> integer().
remove_almost_equal_characters(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_almost_equal_characters(word :: String.t) :: integer
  def remove_almost_equal_characters(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeAlmostEqualCharacters(word: String): Int64 {

    }
}
```

