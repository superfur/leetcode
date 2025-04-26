# 925. 长按键入

## 题目描述

<p>你的朋友正在使用键盘输入他的名字&nbsp;<code>name</code>。偶尔，在键入字符&nbsp;<code>c</code>&nbsp;时，按键可能会被<em>长按</em>，而字符可能被输入 1 次或多次。</p>

<p>你将会检查键盘输入的字符&nbsp;<code>typed</code>。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回&nbsp;<code>True</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>name = "alex", typed = "aaleex"
<strong>输出：</strong>true
<strong>解释：</strong>'alex' 中的 'a' 和 'e' 被长按。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>name = "saeed", typed = "ssaaedd"
<strong>输出：</strong>false
<strong>解释：</strong>'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= name.length, typed.length &lt;= 1000</code></li>
	<li><code>name</code> 和&nbsp;<code>typed</code>&nbsp;的字符都是小写字母</li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 示例

```
"alex"
"aaleex"
"saeed"
"ssaaedd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isLongPressedName(String name, String typed) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
```

### C

```c
bool isLongPressedName(char* name, char* typed) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsLongPressedName(string name, string typed) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
    
};
```

### TypeScript

```typescript
function isLongPressedName(name: string, typed: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $name
     * @param String $typed
     * @return Boolean
     */
    function isLongPressedName($name, $typed) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isLongPressedName(_ name: String, _ typed: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isLongPressedName(name: String, typed: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isLongPressedName(String name, String typed) {
    
  }
}
```

### Go

```golang
func isLongPressedName(name string, typed string) bool {
    
}
```

### Ruby

```ruby
# @param {String} name
# @param {String} typed
# @return {Boolean}
def is_long_pressed_name(name, typed)
    
end
```

### Scala

```scala
object Solution {
    def isLongPressedName(name: String, typed: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_long_pressed_name(name: String, typed: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-long-pressed-name name typed)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_long_pressed_name(Name :: unicode:unicode_binary(), Typed :: unicode:unicode_binary()) -> boolean().
is_long_pressed_name(Name, Typed) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_long_pressed_name(name :: String.t, typed :: String.t) :: boolean
  def is_long_pressed_name(name, typed) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isLongPressedName(name: String, typed: String): Bool {

    }
}
```

