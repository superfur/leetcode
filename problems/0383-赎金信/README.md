# 383. 赎金信

## 题目描述

<p>给你两个字符串：<code>ransomNote</code> 和 <code>magazine</code> ，判断 <code>ransomNote</code> 能不能由 <code>magazine</code> 里面的字符构成。</p>

<p>如果可以，返回 <code>true</code> ；否则返回 <code>false</code> 。</p>

<p><code>magazine</code> 中的每个字符只能在 <code>ransomNote</code> 中使用一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>ransomNote = "a", magazine = "b"
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>ransomNote = "aa", magazine = "ab"
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>ransomNote = "aa", magazine = "aab"
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> 和 <code>magazine</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 示例

```
"a"
"b"
"aa"
"ab"
"aa"
"aab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
```

### C

```c
bool canConstruct(char* ransomNote, char* magazine) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    
};
```

### TypeScript

```typescript
function canConstruct(ransomNote: string, magazine: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $ransomNote
     * @param String $magazine
     * @return Boolean
     */
    function canConstruct($ransomNote, $magazine) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canConstruct(_ ransomNote: String, _ magazine: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canConstruct(String ransomNote, String magazine) {
    
  }
}
```

### Go

```golang
func canConstruct(ransomNote string, magazine string) bool {
    
}
```

### Ruby

```ruby
# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
    
end
```

### Scala

```scala
object Solution {
    def canConstruct(ransomNote: String, magazine: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-construct ransomNote magazine)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec can_construct(RansomNote :: unicode:unicode_binary(), Magazine :: unicode:unicode_binary()) -> boolean().
can_construct(RansomNote, Magazine) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_construct(ransom_note :: String.t, magazine :: String.t) :: boolean
  def can_construct(ransom_note, magazine) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canConstruct(ransomNote: String, magazine: String): Bool {

    }
}
```

