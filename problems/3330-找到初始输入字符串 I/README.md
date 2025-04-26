# 3330. 找到初始输入字符串 I

## 题目描述

<p>Alice 正在她的电脑上输入一个字符串。但是她打字技术比较笨拙，她&nbsp;<strong>可能</strong>&nbsp;在一个按键上按太久，导致一个字符被输入&nbsp;<strong>多次</strong>&nbsp;。</p>

<p>尽管 Alice 尽可能集中注意力，她仍然可能会犯错 <strong>至多</strong>&nbsp;一次。</p>

<p>给你一个字符串&nbsp;<code>word</code> ，它表示 <strong>最终</strong>&nbsp;显示在 Alice 显示屏上的结果。</p>

<p>请你返回 Alice 一开始可能想要输入字符串的总方案数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word = "abbcccc"</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong></p>

<p>可能的字符串包括：<code>"abbcccc"</code>&nbsp;，<code>"abbccc"</code>&nbsp;，<code>"abbcc"</code>&nbsp;，<code>"abbc"</code>&nbsp;和&nbsp;<code>"abcccc"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word = "abcd"</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>唯一可能的字符串是&nbsp;<code>"abcd"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word = "aaaa"</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Any group of consecutive characters might have been the mistake.

## 示例

```
"abbcccc"
"abcd"
"aaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int possibleStringCount(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int possibleStringCount(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def possibleStringCount(self, word: str) -> int:
        
```

### C

```c
int possibleStringCount(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int PossibleStringCount(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var possibleStringCount = function(word) {
    
};
```

### TypeScript

```typescript
function possibleStringCount(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function possibleStringCount($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func possibleStringCount(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun possibleStringCount(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int possibleStringCount(String word) {
    
  }
}
```

### Go

```golang
func possibleStringCount(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def possible_string_count(word)
    
end
```

### Scala

```scala
object Solution {
    def possibleStringCount(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn possible_string_count(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (possible-string-count word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec possible_string_count(Word :: unicode:unicode_binary()) -> integer().
possible_string_count(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec possible_string_count(word :: String.t) :: integer
  def possible_string_count(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func possibleStringCount(word: String): Int64 {

    }
}
```

