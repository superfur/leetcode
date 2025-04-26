# 1678. 设计 Goal 解析器

## 题目描述

<p>请你设计一个可以解释字符串 <code>command</code> 的 <strong>Goal 解析器</strong> 。<code>command</code> 由 <code>"G"</code>、<code>"()"</code> 和/或 <code>"(al)"</code> 按某种顺序组成。Goal 解析器会将 <code>"G"</code> 解释为字符串 <code>"G"</code>、<code>"()"</code> 解释为字符串 <code>"o"</code> ，<code>"(al)"</code> 解释为字符串 <code>"al"</code> 。然后，按原顺序将经解释得到的字符串连接成一个字符串。</p>

<p>给你字符串 <code>command</code> ，返回<em> </em><strong>Goal<em><strong> </strong></em>解析器 </strong>对<em> </em><code>command</code> 的解释结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>command = "G()(al)"
<strong>输出：</strong>"Goal"
<strong>解释：</strong>Goal 解析器解释命令的步骤如下所示：
G -&gt; G
() -&gt; o
(al) -&gt; al
最后连接得到的结果是 "Goal"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>command = "G()()()()(al)"
<strong>输出：</strong>"Gooooal"
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>command = "(al)G(al)()()G"
<strong>输出：</strong>"alGalooG"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= command.length &lt;= 100</code></li>
	<li><code>command</code> 由 <code>"G"</code>、<code>"()"</code> 和/或 <code>"(al)"</code> 按某种顺序组成</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. You need to check at most 2 characters to determine which character comes next.

## 示例

```
"G()(al)"
"G()()()()(al)"
"(al)G(al)()()G"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string interpret(string command) {
        
    }
};
```

### Java

```java
class Solution {
    public String interpret(String command) {
        
    }
}
```

### Python

```python
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def interpret(self, command: str) -> str:
        
```

### C

```c
char* interpret(char* command) {
    
}
```

### C#

```csharp
public class Solution {
    public string Interpret(string command) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
    
};
```

### TypeScript

```typescript
function interpret(command: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $command
     * @return String
     */
    function interpret($command) {
        
    }
}
```

### Swift

```swift
class Solution {
    func interpret(_ command: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun interpret(command: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String interpret(String command) {
    
  }
}
```

### Go

```golang
func interpret(command string) string {
    
}
```

### Ruby

```ruby
# @param {String} command
# @return {String}
def interpret(command)
    
end
```

### Scala

```scala
object Solution {
    def interpret(command: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn interpret(command: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (interpret command)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec interpret(Command :: unicode:unicode_binary()) -> unicode:unicode_binary().
interpret(Command) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec interpret(command :: String.t) :: String.t
  def interpret(command) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func interpret(command: String): String {

    }
}
```

