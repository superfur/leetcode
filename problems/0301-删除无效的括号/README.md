# 301. 删除无效的括号

## 题目描述

<p>给你一个由若干括号和字母组成的字符串 <code>s</code> ，删除最小数量的无效括号，使得输入的字符串有效。</p>

<p>返回所有可能的结果。答案可以按 <strong>任意顺序</strong> 返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "()())()"
<strong>输出：</strong>["(())()","()()()"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "(a)())()"
<strong>输出：</strong>["(a())()","(a)()()"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = ")("
<strong>输出：</strong>[""]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 25</code></li>
	<li><code>s</code> 由小写英文字母以及括号 <code>'('</code> 和 <code>')'</code> 组成</li>
	<li><code>s</code> 中至多含 <code>20</code> 个括号</li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 字符串
- 回溯

## 提示

1. Since we do not know which brackets can be removed, we try all the options! We can use recursion.
2. In the recursion, for each bracket, we can either use it or remove it.
3. Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.
4. We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.

## 示例

```
"()())()"
"(a)())()"
")("
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> removeInvalidParentheses(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeInvalidParentheses(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> RemoveInvalidParentheses(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    
};
```

### TypeScript

```typescript
function removeInvalidParentheses(s: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function removeInvalidParentheses($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeInvalidParentheses(_ s: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeInvalidParentheses(s: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> removeInvalidParentheses(String s) {
    
  }
}
```

### Go

```golang
func removeInvalidParentheses(s string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    
end
```

### Scala

```scala
object Solution {
    def removeInvalidParentheses(s: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (remove-invalid-parentheses s)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec remove_invalid_parentheses(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
remove_invalid_parentheses(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_invalid_parentheses(s :: String.t) :: [String.t]
  def remove_invalid_parentheses(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeInvalidParentheses(s: String): ArrayList<String> {

    }
}
```

