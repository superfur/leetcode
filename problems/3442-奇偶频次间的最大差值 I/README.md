# 3442. 奇偶频次间的最大差值 I

## 题目描述

<p>给你一个由小写英文字母组成的字符串&nbsp;<code>s</code> 。请你找出字符串中两个字符的出现频次之间的 <strong>最大</strong> 差值，这两个字符需要满足：</p>

<ul>
	<li>一个字符在字符串中出现 <strong>偶数次</strong> 。</li>
	<li>另一个字符在字符串中出现 <strong>奇数次</strong>&nbsp;。</li>
</ul>

<p>返回 <strong>最大</strong> 差值，计算方法是出现 <strong>奇数次</strong> 字符的次数 <strong>减去</strong> 出现 <strong>偶数次</strong> 字符的次数。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "aaaaabbc"</span></p>

<p><b>输出：</b>3</p>

<p><b>解释：</b></p>

<ul>
	<li>字符&nbsp;<code>'a'</code>&nbsp;出现 <strong>奇数次</strong>&nbsp;，次数为&nbsp;<code><font face="monospace">5</font></code><font face="monospace"> ；字符</font>&nbsp;<code>'b'</code>&nbsp;出现 <strong>偶数次</strong> ，次数为&nbsp;<code><font face="monospace">2</font></code>&nbsp;。</li>
	<li>最大差值为&nbsp;<code>5 - 2 = 3</code>&nbsp;。</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abcabcab"</span></p>

<p><b>输出：</b>1</p>

<p><b>解释：</b></p>

<ul>
	<li>字符&nbsp;<code>'a'</code>&nbsp;出现 <strong>奇数次</strong>&nbsp;，次数为&nbsp;<code><font face="monospace">3</font></code><font face="monospace"> ；字符</font>&nbsp;<code>'c'</code>&nbsp;出现 <strong>偶数次</strong>&nbsp;，次数为&nbsp;<font face="monospace">2 。</font></li>
	<li>最大差值为&nbsp;<code>3 - 2 = 1</code> 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;仅由小写英文字母组成。</li>
	<li><code>s</code>&nbsp;至少由一个出现奇数次的字符和一个出现偶数次的字符组成。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Use a frequency map to identify the maximum odd and minimum even frequencies. Then, calculate their difference.

## 示例

```
"aaaaabbc"
"abcabcab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDifference(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDifference(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDifference(self, s: str) -> int:
        
```

### C

```c
int maxDifference(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDifference(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function(s) {
    
};
```

### TypeScript

```typescript
function maxDifference(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxDifference($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDifference(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDifference(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDifference(String s) {
    
  }
}
```

### Go

```golang
func maxDifference(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_difference(s)
    
end
```

### Scala

```scala
object Solution {
    def maxDifference(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_difference(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-difference s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_difference(S :: unicode:unicode_binary()) -> integer().
max_difference(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_difference(s :: String.t) :: integer
  def max_difference(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDifference(s: String): Int64 {

    }
}
```

