# 3019. 按键变更的次数

## 题目描述

<p>给你一个下标从<strong> 0</strong> 开始的字符串 <code>s</code> ，该字符串由用户输入。按键变更的定义是：使用与上次使用的按键不同的键。例如 <code>s = "ab"</code> 表示按键变更一次，而 <code>s = "bBBb"</code> 不存在按键变更。</p>

<p>返回用户输入过程中按键变更的次数。</p>

<p><strong>注意：</strong><code>shift</code> 或 <code>caps lock</code> 等修饰键不计入按键变更，也就是说，如果用户先输入字母 <code>'a'</code> 然后输入字母 <code>'A'</code> ，不算作按键变更。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aAbBcC"
<strong>输出：</strong>2
<strong>解释：</strong> 
从 s[0] = 'a' 到 s[1] = 'A'，不存在按键变更，因为不计入 caps lock 或 shift 。
从 s[1] = 'A' 到 s[2] = 'b'，按键变更。
从 s[2] = 'b' 到 s[3] = 'B'，不存在按键变更，因为不计入 caps lock 或 shift 。
从 s[3] = 'B' 到 s[4] = 'c'，按键变更。
从 s[4] = 'c' 到 s[5] = 'C'，不存在按键变更，因为不计入 caps lock 或 shift 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "AaAaAaaA"
<strong>输出：</strong>0
<strong>解释：</strong> 不存在按键变更，因为这个过程中只按下字母 'a' 和 'A' ，不需要进行按键变更。<!-- notionvc: 8849fe75-f31e-41dc-a2e0-b7d33d8427d2 -->
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由英文大写字母和小写字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Change all the characters to lowercase and then return the number of indices where the character does not match with the last index character.

## 示例

```
"aAbBcC"
"AaAaAaaA"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countKeyChanges(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countKeyChanges(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countKeyChanges(self, s: str) -> int:
        
```

### C

```c
int countKeyChanges(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountKeyChanges(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countKeyChanges = function(s) {
    
};
```

### TypeScript

```typescript
function countKeyChanges(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countKeyChanges($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countKeyChanges(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countKeyChanges(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countKeyChanges(String s) {
    
  }
}
```

### Go

```golang
func countKeyChanges(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_key_changes(s)
    
end
```

### Scala

```scala
object Solution {
    def countKeyChanges(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_key_changes(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-key-changes s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_key_changes(S :: unicode:unicode_binary()) -> integer().
count_key_changes(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_key_changes(s :: String.t) :: integer
  def count_key_changes(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countKeyChanges(s: String): Int64 {

    }
}
```

