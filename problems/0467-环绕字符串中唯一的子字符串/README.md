# 467. 环绕字符串中唯一的子字符串

## 题目描述

<p>定义字符串&nbsp;<code>base</code>&nbsp;为一个&nbsp;<code>"abcdefghijklmnopqrstuvwxyz"</code>&nbsp;无限环绕的字符串，所以&nbsp;<code>base</code>&nbsp;看起来是这样的：</p>

<ul>
	<li><code>"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."</code>.</li>
</ul>

<p>给你一个字符串&nbsp;<code>s</code> ，请你统计并返回&nbsp;<code>s</code>&nbsp;中有多少&nbsp;<strong>不同</strong><strong>非空子串</strong>&nbsp;也在&nbsp;<code>base</code>&nbsp;中出现。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>s = "a"
<strong>输出：</strong>1
<strong>解释：</strong>字符串 s 的子字符串 "a" 在 base 中出现。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "cac"
<strong>输出：</strong>2
<strong>解释：</strong>字符串 s 有两个子字符串 ("a", "c") 在 base 中出现。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "zab"
<strong>输出：</strong>6
<strong>解释：</strong>字符串 s 有六个子字符串 ("z", "a", "b", "za", "ab", and "zab") 在 base 中出现。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size: 12.6px; background-color: rgb(249, 242, 244);">s</span></font> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 提示

1. One possible solution might be to consider allocating an array size of 26 for each character in the alphabet. (Credits to @r2ysxu)

## 示例

```
"a"
"cac"
"zab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findSubstringInWraproundString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int findSubstringInWraproundString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
```

### C

```c
int findSubstringInWraproundString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindSubstringInWraproundString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var findSubstringInWraproundString = function(s) {
    
};
```

### TypeScript

```typescript
function findSubstringInWraproundString(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function findSubstringInWraproundString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSubstringInWraproundString(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSubstringInWraproundString(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findSubstringInWraproundString(String s) {
    
  }
}
```

### Go

```golang
func findSubstringInWraproundString(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def find_substring_in_wrapround_string(s)
    
end
```

### Scala

```scala
object Solution {
    def findSubstringInWraproundString(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_substring_in_wrapround_string(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-substring-in-wrapround-string s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_substring_in_wrapround_string(S :: unicode:unicode_binary()) -> integer().
find_substring_in_wrapround_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_substring_in_wrapround_string(s :: String.t) :: integer
  def find_substring_in_wrapround_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSubstringInWraproundString(s: String): Int64 {

    }
}
```

