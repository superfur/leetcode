# 1047. 删除字符串中的所有相邻重复项

## 题目描述

<p>给出由小写字母组成的字符串&nbsp;<code>s</code>，<strong>重复项删除操作</strong>会选择两个相邻且相同的字母，并删除它们。</p>

<p>在 <code>s</code> 上反复执行重复项删除操作，直到无法继续删除。</p>

<p>在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>"abbaca"
<strong>输出：</strong>"ca"
<strong>解释：</strong>
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ol>


## 难度

Easy

## 标签

- 栈
- 字符串

## 提示

1. Use a stack to process everything greedily.

## 示例

```
"abbaca"
"azxxzy"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeDuplicates(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
```

### C

```c
char* removeDuplicates(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveDuplicates(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
    
};
```

### TypeScript

```typescript
function removeDuplicates(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function removeDuplicates($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeDuplicates(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeDuplicates(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeDuplicates(String s) {
    
  }
}
```

### Go

```golang
func removeDuplicates(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def remove_duplicates(s)
    
end
```

### Scala

```scala
object Solution {
    def removeDuplicates(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-duplicates s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec remove_duplicates(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_duplicates(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_duplicates(s :: String.t) :: String.t
  def remove_duplicates(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeDuplicates(s: String): String {

    }
}
```

