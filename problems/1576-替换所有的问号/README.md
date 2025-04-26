# 1576. 替换所有的问号

## 题目描述

<p>给你一个仅包含小写英文字母和 <code>'?'</code> 字符的字符串 <code>s</code>，请你将所有的 <code>'?'</code> 转换为若干小写字母，使最终的字符串不包含任何 <strong>连续重复</strong> 的字符。</p>

<p>注意：你 <strong>不能</strong> 修改非 <code>'?'</code> 字符。</p>

<p>题目测试用例保证 <strong>除</strong> <code>'?'</code> 字符 <strong>之外</strong>，不存在连续重复的字符。</p>

<p>在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "?zs"
<strong>输出：</strong>"azs"
<strong>解释：</strong>该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 'z' 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ubv?w"
<strong>输出：</strong>"ubvaw"
<strong>解释：</strong>该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>
	<p><code>1 &lt;= s.length&nbsp;&lt;= 100</code></p>
	</li>
	<li>
	<p><code>s</code> 仅包含小写英文字母和 <code>'?'</code> 字符</p>
	</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Processing string from left to right, whenever you get a ‘?’, check left character and right character, and select a character not equal to either of them
2. Do take care to compare with replaced occurrence of ‘?’ when checking the left character.

## 示例

```
"?zs"
"ubv?w"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string modifyString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String modifyString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def modifyString(self, s: str) -> str:
        
```

### C

```c
char* modifyString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string ModifyString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var modifyString = function(s) {
    
};
```

### TypeScript

```typescript
function modifyString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function modifyString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func modifyString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun modifyString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String modifyString(String s) {
    
  }
}
```

### Go

```golang
func modifyString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def modify_string(s)
    
end
```

### Scala

```scala
object Solution {
    def modifyString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn modify_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (modify-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec modify_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
modify_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec modify_string(s :: String.t) :: String.t
  def modify_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func modifyString(s: String): String {

    }
}
```

