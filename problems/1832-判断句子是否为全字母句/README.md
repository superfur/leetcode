# 1832. 判断句子是否为全字母句

## 题目描述

<p><strong>全字母句</strong> 指包含英语字母表中每个字母至少一次的句子。</p>

<p>给你一个仅由小写英文字母组成的字符串 <code>sentence</code> ，请你判断 <code>sentence</code> 是否为 <strong>全字母句</strong> 。</p>

<p>如果是，返回<em> </em><code>true</code> ；否则，返回<em> </em><code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>sentence = "thequickbrownfoxjumpsoverthelazydog"
<strong>输出：</strong>true
<strong>解释：</strong><code>sentence</code> 包含英语字母表中每个字母至少一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>sentence = "leetcode"
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= sentence.length <= 1000</code></li>
	<li><code>sentence</code> 由小写英语字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Iterate over the string and mark each character as found (using a boolean array, bitmask, or any other similar way).
2. Check if the number of found characters equals the alphabet length.

## 示例

```
"thequickbrownfoxjumpsoverthelazydog"
"leetcode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkIfPangram(string sentence) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkIfPangram(String sentence) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
```

### C

```c
bool checkIfPangram(char* sentence) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckIfPangram(string sentence) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    
};
```

### TypeScript

```typescript
function checkIfPangram(sentence: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sentence
     * @return Boolean
     */
    function checkIfPangram($sentence) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkIfPangram(_ sentence: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkIfPangram(sentence: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkIfPangram(String sentence) {
    
  }
}
```

### Go

```golang
func checkIfPangram(sentence string) bool {
    
}
```

### Ruby

```ruby
# @param {String} sentence
# @return {Boolean}
def check_if_pangram(sentence)
    
end
```

### Scala

```scala
object Solution {
    def checkIfPangram(sentence: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-if-pangram sentence)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_if_pangram(Sentence :: unicode:unicode_binary()) -> boolean().
check_if_pangram(Sentence) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_if_pangram(sentence :: String.t) :: boolean
  def check_if_pangram(sentence) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkIfPangram(sentence: String): Bool {

    }
}
```

