# 1446. 连续字符

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，字符串的<strong>「能量」</strong>定义为：只包含一种字符的最长非空子字符串的长度。</p>

<p>请你返回字符串 <code>s</code> 的 <strong>能量</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "leetcode"
<strong>输出：</strong>2
<strong>解释：</strong>子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abbcccddddeeeeedcba"
<strong>输出：</strong>5
<strong>解释：</strong>子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Keep an array power where power[i] is the maximum power of the i-th character.
2. The answer is max(power[i]).

## 示例

```
"leetcode"
"abbcccddddeeeeedcba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPower(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPower(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPower(self, s: str) -> int:
        
```

### C

```c
int maxPower(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPower(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
    
};
```

### TypeScript

```typescript
function maxPower(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxPower($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPower(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPower(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPower(String s) {
    
  }
}
```

### Go

```golang
func maxPower(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_power(s)
    
end
```

### Scala

```scala
object Solution {
    def maxPower(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_power(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-power s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_power(S :: unicode:unicode_binary()) -> integer().
max_power(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_power(s :: String.t) :: integer
  def max_power(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPower(s: String): Int64 {

    }
}
```

