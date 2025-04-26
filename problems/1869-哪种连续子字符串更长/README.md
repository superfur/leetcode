# 1869. 哪种连续子字符串更长

## 题目描述

<p>给你一个二进制字符串 <code>s</code> 。如果字符串中由 <code>1</code> 组成的 <strong>最长</strong> 连续子字符串 <strong>严格长于</strong> 由 <code>0</code> 组成的 <strong>最长</strong> 连续子字符串，返回 <code>true</code> ；否则，返回 <code>false</code><em> </em>。</p>

<ul>
	<li>例如，<code>s = "<strong>11</strong>01<strong>000</strong>10"</code> 中，由 <code>1</code> 组成的最长连续子字符串的长度是 <code>2</code> ，由 <code>0</code> 组成的最长连续子字符串的长度是 <code>3</code> 。</li>
</ul>

<p>注意，如果字符串中不存在 <code>0</code> ，此时认为由 <code>0</code> 组成的最长连续子字符串的长度是 <code>0</code> 。字符串中不存在 <code>1</code> 的情况也适用此规则。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1101"
<strong>输出：</strong>true
<strong>解释：</strong>
由 <code>1</code> 组成的最长连续子字符串的长度是 2："<strong>11</strong>01"
由 <code>0</code> 组成的最长连续子字符串的长度是 1："11<strong>0</strong>1"
由 1 组成的子字符串更长，故返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "111000"
<strong>输出：</strong>false
<strong>解释：</strong>
由 <code>1</code> 组成的最长连续子字符串的长度是 3："<strong>111</strong>000"
由<code> 0</code> 组成的最长连续子字符串的长度是 3："111<strong>000</strong>"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "110100010"
<strong>输出：</strong>false
<strong>解释：</strong>
由 <code>1</code> 组成的最长连续子字符串的长度是 2："<strong>11</strong>0100010"
由 <code>0</code> 组成的最长连续子字符串的长度是 3："1101<strong>000</strong>10"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s[i]</code> 不是 <code>'0'</code> 就是 <code>'1'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Check every possible segment of 0s and 1s.
2. Is there a way to iterate through the string to keep track of the current character and its count?

## 示例

```
"1101"
"111000"
"110100010"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkZeroOnes(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkZeroOnes(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
```

### C

```c
bool checkZeroOnes(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckZeroOnes(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkZeroOnes = function(s) {
    
};
```

### TypeScript

```typescript
function checkZeroOnes(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkZeroOnes($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkZeroOnes(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkZeroOnes(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkZeroOnes(String s) {
    
  }
}
```

### Go

```golang
func checkZeroOnes(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_zero_ones(s)
    
end
```

### Scala

```scala
object Solution {
    def checkZeroOnes(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_zero_ones(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-zero-ones s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_zero_ones(S :: unicode:unicode_binary()) -> boolean().
check_zero_ones(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_zero_ones(s :: String.t) :: boolean
  def check_zero_ones(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkZeroOnes(s: String): Bool {

    }
}
```

