# 3174. 清除数字

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>你的任务是重复以下操作删除 <strong>所有</strong>&nbsp;数字字符：</p>

<ul>
	<li>删除 <strong>第一个数字字符</strong>&nbsp;以及它左边 <strong>最近</strong>&nbsp;的 <strong>非数字</strong>&nbsp;字符。</li>
</ul>

<p>请你返回删除所有数字字符以后剩下的字符串。</p>

<p><strong>注意</strong>，该操作不能对左侧没有任何非数字字符的数字执行。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abc"</span></p>

<p><span class="example-io"><b>输出：</b>"abc"</span></p>

<p><strong>解释：</strong></p>

<p>字符串中没有数字。<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde --></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "cb34"</span></p>

<p><span class="example-io"><b>输出：</b>""</span></p>

<p><b>解释：</b></p>

<p>一开始，我们对&nbsp;<code>s[2]</code>&nbsp;执行操作，<code>s</code>&nbsp;变为&nbsp;<code>"c4"</code>&nbsp;。</p>

<p>然后对&nbsp;<code>s[1]</code>&nbsp;执行操作，<code>s</code>&nbsp;变为&nbsp;<code>""</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母和数字字符。</li>
	<li>输入保证所有数字都可以按以上操作被删除。</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 字符串
- 模拟

## 提示

1. Process string <code>s</code> from left to right, if <code>s[i]</code> is a digit, mark the nearest unmarked non-digit index to its left.
2. Delete all digits and all marked characters.

## 示例

```
"abc"
"cb34"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string clearDigits(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String clearDigits(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def clearDigits(self, s: str) -> str:
        
```

### C

```c
char* clearDigits(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string ClearDigits(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    
};
```

### TypeScript

```typescript
function clearDigits(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function clearDigits($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func clearDigits(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun clearDigits(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String clearDigits(String s) {
    
  }
}
```

### Go

```golang
func clearDigits(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def clear_digits(s)
    
end
```

### Scala

```scala
object Solution {
    def clearDigits(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn clear_digits(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (clear-digits s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec clear_digits(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
clear_digits(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec clear_digits(s :: String.t) :: String.t
  def clear_digits(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func clearDigits(s: String): String {

    }
}
```

