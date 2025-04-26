# 2982. 找出出现至少三次的最长特殊子字符串 II

## 题目描述

<p>给你一个仅由小写英文字母组成的字符串 <code>s</code> 。</p>

<p>如果一个字符串仅由单一字符组成，那么它被称为 <strong>特殊 </strong>字符串。例如，字符串 <code>"abc"</code> 不是特殊字符串，而字符串 <code>"ddd"</code>、<code>"zz"</code> 和 <code>"f"</code> 是特殊字符串。</p>

<p>返回在 <code>s</code> 中出现 <strong>至少三次 </strong>的<strong> 最长特殊子字符串 </strong>的长度，如果不存在出现至少三次的特殊子字符串，则返回 <code>-1</code> 。</p>

<p><strong>子字符串 </strong>是字符串中的一个连续<strong> 非空 </strong>字符序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aaaa"
<strong>输出：</strong>2
<strong>解释：</strong>出现三次的最长特殊子字符串是 "aa" ：子字符串 "<em><strong>aa</strong></em>aa"、"a<em><strong>aa</strong></em>a" 和 "aa<em><strong>aa</strong></em>"。
可以证明最大长度是 2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcdef"
<strong>输出：</strong>-1
<strong>解释：</strong>不存在出现至少三次的特殊子字符串。因此返回 -1 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abcaba"
<strong>输出：</strong>1
<strong>解释：</strong>出现三次的最长特殊子字符串是 "a" ：子字符串 "<em><strong>a</strong></em>bcaba"、"abc<em><strong>a</strong></em>ba" 和 "abcab<em><strong>a</strong></em>"。
可以证明最大长度是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 二分查找
- 计数
- 滑动窗口

## 提示

1. Let <code>len[i]</code> be the length of the longest special string ending with <code>s[i]</code>.
2. If <code>i > 0</code> and <code>s[i] == s[i - 1]</code>, <code>len[i] = len[i - 1] + 1</code>. Otherwise <code>len[i] == 1</code>.
3. Group all the <code>len[i]</code> by <code>s[i]</code>. We have at most <code>26</code> groups.
4. The maximum value of the third largest <code>len[i]</code> in each group is the answer.
5. We only need to maintain the top three values for each group. You can use sorting, heap, or brute-force comparison to find the third largest value in each group.

## 示例

```
"aaaa"
"abcdef"
"abcaba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumLength(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumLength(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumLength(self, s: str) -> int:
        
```

### C

```c
int maximumLength(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumLength(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maximumLength = function(s) {
    
};
```

### TypeScript

```typescript
function maximumLength(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maximumLength($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumLength(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumLength(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumLength(String s) {
    
  }
}
```

### Go

```golang
func maximumLength(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def maximum_length(s)
    
end
```

### Scala

```scala
object Solution {
    def maximumLength(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-length s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_length(S :: unicode:unicode_binary()) -> integer().
maximum_length(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_length(s :: String.t) :: integer
  def maximum_length(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumLength(s: String): Int64 {

    }
}
```

