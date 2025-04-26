# 2390. 从字符串中移除星号

## 题目描述

<p>给你一个包含若干星号 <code>*</code> 的字符串 <code>s</code> 。</p>

<p>在一步操作中，你可以：</p>

<ul>
	<li>选中 <code>s</code> 中的一个星号。</li>
	<li>移除星号 <strong>左侧</strong> 最近的那个 <strong>非星号</strong> 字符，并移除该星号自身。</li>
</ul>

<p>返回移除 <strong>所有</strong> 星号之后的字符串<strong>。</strong></p>

<p><strong>注意：</strong></p>

<ul>
	<li>生成的输入保证总是可以执行题面中描述的操作。</li>
	<li>可以证明结果字符串是唯一的。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "leet**cod*e"
<strong>输出：</strong>"lecoe"
<strong>解释：</strong>从左到右执行移除操作：
- 距离第 1 个星号最近的字符是 "lee<em><strong>t</strong></em>**cod*e" 中的 't' ，s 变为 "lee*cod*e" 。
- 距离第 2 个星号最近的字符是 "le<em><strong>e</strong></em>*cod*e" 中的 'e' ，s 变为 "lecod*e" 。
- 距离第 3 个星号最近的字符是 "leco<em><strong>d</strong></em>*e" 中的 'd' ，s 变为 "lecoe" 。
不存在其他星号，返回 "lecoe" 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "erase*****"
<strong>输出：</strong>""
<strong>解释：</strong>整个字符串都会被移除，所以返回空字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母和星号 <code>*</code> 组成</li>
	<li><code>s</code> 可以执行上述操作</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串
- 模拟

## 提示

1. What data structure could we use to efficiently perform these removals?
2. Use a stack to store the characters. Pop one character off the stack at each star. Otherwise, we push the character onto the stack.

## 示例

```
"leet**cod*e"
"erase*****"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeStars(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeStars(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeStars(self, s: str) -> str:
        
```

### C

```c
char* removeStars(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveStars(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    
};
```

### TypeScript

```typescript
function removeStars(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function removeStars($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeStars(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeStars(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeStars(String s) {
    
  }
}
```

### Go

```golang
func removeStars(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def remove_stars(s)
    
end
```

### Scala

```scala
object Solution {
    def removeStars(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_stars(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-stars s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec remove_stars(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_stars(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_stars(s :: String.t) :: String.t
  def remove_stars(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeStars(s: String): String {

    }
}
```

