# 2423. 删除字符使频率相同

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>word</code>&nbsp;，字符串只包含小写英文字母。你需要选择 <strong>一个</strong>&nbsp;下标并 <strong>删除</strong>&nbsp;下标处的字符，使得 <code>word</code>&nbsp;中剩余每个字母出现 <strong>频率</strong>&nbsp;相同。</p>

<p>如果删除一个字母后，<code>word</code>&nbsp;中剩余所有字母的出现频率都相同，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>字母&nbsp;<code>x</code>&nbsp;的 <strong>频率</strong><strong>&nbsp;</strong>是这个字母在字符串中出现的次数。</li>
	<li>你 <strong>必须</strong>&nbsp;恰好删除一个字母，不能一个字母都不删除。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>word = "abcc"
<b>输出：</b>true
<b>解释：</b>选择下标 3 并删除该字母：word 变成 "abc" 且每个字母出现频率都为 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>word = "aazz"
<b>输出：</b>false
<b>解释：</b>我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Brute force all letters that could be removed.
2. Use a frequency array of size 26.

## 示例

```
"abcc"
"aazz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool equalFrequency(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean equalFrequency(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def equalFrequency(self, word: str) -> bool:
        
```

### C

```c
bool equalFrequency(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public bool EqualFrequency(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {boolean}
 */
var equalFrequency = function(word) {
    
};
```

### TypeScript

```typescript
function equalFrequency(word: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function equalFrequency($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func equalFrequency(_ word: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun equalFrequency(word: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool equalFrequency(String word) {
    
  }
}
```

### Go

```golang
func equalFrequency(word string) bool {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Boolean}
def equal_frequency(word)
    
end
```

### Scala

```scala
object Solution {
    def equalFrequency(word: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn equal_frequency(word: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (equal-frequency word)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec equal_frequency(Word :: unicode:unicode_binary()) -> boolean().
equal_frequency(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec equal_frequency(word :: String.t) :: boolean
  def equal_frequency(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func equalFrequency(word: String): Bool {

    }
}
```

