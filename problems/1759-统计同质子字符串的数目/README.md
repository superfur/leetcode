# 1759. 统计同质子字符串的数目

## 题目描述

<p>给你一个字符串 <code>s</code> ，返回<em> </em><code>s</code><em> </em>中 <strong>同质子字符串</strong> 的数目。由于答案可能很大，只需返回对 <code>10<sup>9</sup> + 7</code> <strong>取余 </strong>后的结果。</p>

<p><strong>同质字符串</strong> 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同质字符串。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abbcccaa"
<strong>输出：</strong>13
<strong>解释：</strong>同质子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "xy"
<strong>输出：</strong>2
<strong>解释：</strong>同质子字符串是 "x" 和 "y" 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "zzzzz"
<strong>输出：</strong>15
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写字符串组成。</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串

## 提示

1. A string of only 'a's of length k contains k + 1 choose 2 homogenous substrings.
2. Split the string into substrings where each substring contains only one letter, and apply the formula on each substring's length.

## 示例

```
"abbcccaa"
"xy"
"zzzzz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countHomogenous(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countHomogenous(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countHomogenous(self, s: str) -> int:
        
```

### C

```c
int countHomogenous(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountHomogenous(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function(s) {
    
};
```

### TypeScript

```typescript
function countHomogenous(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countHomogenous($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countHomogenous(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countHomogenous(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countHomogenous(String s) {
    
  }
}
```

### Go

```golang
func countHomogenous(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_homogenous(s)
    
end
```

### Scala

```scala
object Solution {
    def countHomogenous(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-homogenous s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_homogenous(S :: unicode:unicode_binary()) -> integer().
count_homogenous(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_homogenous(s :: String.t) :: integer
  def count_homogenous(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countHomogenous(s: String): Int64 {

    }
}
```

