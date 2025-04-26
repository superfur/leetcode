# 1433. 检查一个字符串是否可以打破另一个字符串

## 题目描述

<p>给你两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;，它们长度相等，请你检查是否存在一个&nbsp;<code>s1</code>&nbsp; 的排列可以打破 <code>s2</code>&nbsp;的一个排列，或者是否存在一个&nbsp;<code>s2</code>&nbsp;的排列可以打破 <code>s1</code> 的一个排列。</p>

<p>字符串&nbsp;<code>x</code>&nbsp;可以打破字符串&nbsp;<code>y</code>&nbsp;（两者长度都为&nbsp;<code>n</code>&nbsp;）需满足对于所有&nbsp;<code>i</code>（在&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;之间）都有&nbsp;<code>x[i] &gt;= y[i]</code>（字典序意义下的顺序）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;abc&quot;, s2 = &quot;xya&quot;
<strong>输出：</strong>true
<strong>解释：</strong>&quot;ayx&quot; 是 s2=&quot;xya&quot; 的一个排列，&quot;abc&quot; 是字符串 s1=&quot;abc&quot; 的一个排列，且 &quot;ayx&quot; 可以打破 &quot;abc&quot; 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;abe&quot;, s2 = &quot;acd&quot;
<strong>输出：</strong>false 
<strong>解释：</strong>s1=&quot;abe&quot; 的所有排列包括：&quot;abe&quot;，&quot;aeb&quot;，&quot;bae&quot;，&quot;bea&quot;，&quot;eab&quot; 和 &quot;eba&quot; ，s2=&quot;acd&quot; 的所有排列包括：&quot;acd&quot;，&quot;adc&quot;，&quot;cad&quot;，&quot;cda&quot;，&quot;dac&quot; 和 &quot;dca&quot;。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;leetcodee&quot;, s2 = &quot;interview&quot;
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s1.length == n</code></li>
	<li><code>s2.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li>所有字符串都只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 排序

## 提示

1. Sort both strings and then check if one of them can break the other.

## 示例

```
"abc"
"xya"
"abe"
"acd"
"leetcodee"
"interview"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkIfCanBreak(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool checkIfCanBreak(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckIfCanBreak(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkIfCanBreak = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function checkIfCanBreak(s1: string, s2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkIfCanBreak($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkIfCanBreak(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkIfCanBreak(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkIfCanBreak(String s1, String s2) {
    
  }
}
```

### Go

```golang
func checkIfCanBreak(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_if_can_break(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def checkIfCanBreak(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_if_can_break(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-if-can-break s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec check_if_can_break(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_if_can_break(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_if_can_break(s1 :: String.t, s2 :: String.t) :: boolean
  def check_if_can_break(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkIfCanBreak(s1: String, s2: String): Bool {

    }
}
```

