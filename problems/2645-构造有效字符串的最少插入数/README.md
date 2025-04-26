# 2645. 构造有效字符串的最少插入数

## 题目描述

<p>给你一个字符串 <code>word</code> ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 <code>word</code> <strong>有效</strong> 需要插入的最少字母数。</p>

<p>如果字符串可以由 "abc" 串联多次得到，则认为该字符串 <strong>有效</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>word = "b"
<strong>输出：</strong>2
<strong>解释：</strong>在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "<strong>a</strong>b<strong>c</strong>" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>word = "aaa"
<strong>输出：</strong>6
<strong>解释：</strong>在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "a<strong>bc</strong>a<strong>bc</strong>a<strong>bc</strong>" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>word = "abc"
<strong>输出：</strong>0
<strong>解释：</strong>word 已经是有效字符串，不需要进行修改。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 50</code></li>
	<li><code>word</code> 仅由字母 "a"、"b" 和 "c" 组成。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串
- 动态规划

## 提示

1. Maintain a pointer on word and another pointer on string “abc”.
2. If the two characters that are being pointed to differ, Increment the answer and the pointer to the string “abc” by one.

## 示例

```
"b"
"aaa"
"abc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int addMinimum(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int addMinimum(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def addMinimum(self, word: str) -> int:
        
```

### C

```c
int addMinimum(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int AddMinimum(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var addMinimum = function(word) {
    
};
```

### TypeScript

```typescript
function addMinimum(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function addMinimum($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func addMinimum(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addMinimum(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int addMinimum(String word) {
    
  }
}
```

### Go

```golang
func addMinimum(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def add_minimum(word)
    
end
```

### Scala

```scala
object Solution {
    def addMinimum(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_minimum(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (add-minimum word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec add_minimum(Word :: unicode:unicode_binary()) -> integer().
add_minimum(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_minimum(word :: String.t) :: integer
  def add_minimum(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func addMinimum(word: String): Int64 {

    }
}
```

