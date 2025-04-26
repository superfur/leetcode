# 678. 有效的括号字符串

## 题目描述

<p>给你一个只包含三种字符的字符串，支持的字符类型分别是 <code>'('</code>、<code>')'</code> 和 <code>'*'</code>。请你检验这个字符串是否为有效字符串，如果是 <strong>有效</strong> 字符串返回 <code>true</code> 。</p>

<p><strong>有效</strong> 字符串符合如下规则：</p>

<ul>
	<li>任何左括号 <code>'('</code>&nbsp;必须有相应的右括号 <code>')'</code>。</li>
	<li>任何右括号 <code>')'</code>&nbsp;必须有相应的左括号 <code>'('</code>&nbsp;。</li>
	<li>左括号 <code>'('</code> 必须在对应的右括号之前 <code>')'</code>。</li>
	<li><code>'*'</code>&nbsp;可以被视为单个右括号 <code>')'</code>&nbsp;，或单个左括号 <code>'('</code>&nbsp;，或一个空字符串 <code>""</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "()"
<strong>输出：</strong>true
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "(*)"
<strong>输出：</strong>true
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "(*))"
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> 为 <code>'('</code>、<code>')'</code> 或 <code>'*'</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串
- 动态规划

## 提示

1. Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
2. DP[i][j] represents whether the substring s[i:j] is valid.
3. Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
4. How about using 2 stacks instead of 1? Think about it.

## 示例

```
"()"
"(*)"
"(*))"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkValidString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkValidString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkValidString(self, s: str) -> bool:
        
```

### C

```c
bool checkValidString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckValidString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    
};
```

### TypeScript

```typescript
function checkValidString(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkValidString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkValidString(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkValidString(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkValidString(String s) {
    
  }
}
```

### Go

```golang
func checkValidString(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_valid_string(s)
    
end
```

### Scala

```scala
object Solution {
    def checkValidString(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-valid-string s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_valid_string(S :: unicode:unicode_binary()) -> boolean().
check_valid_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_valid_string(s :: String.t) :: boolean
  def check_valid_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkValidString(s: String): Bool {

    }
}
```

