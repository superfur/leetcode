# LCR 020. 回文子串

## 题目描述

<p>给定一个字符串 <code>s</code> ，请计算这个字符串中有多少个回文子字符串。</p>

<p>具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;abc&quot;
<strong>输出：</strong>3
<strong>解释：</strong>三个回文子串: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s =<strong> </strong>&quot;aaa&quot;
<strong>输出：</strong>6
<strong>解释：</strong>6个回文子串: &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;aa&quot;, &quot;aa&quot;, &quot;aaa&quot;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 70 题相同：<a href="https://leetcode-cn.com/problems/palindromic-substrings/">https://leetcode-cn.com/problems/palindromic-substrings/</a>&nbsp;</p>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 示例

```
"abc"
"aaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubstrings(string s) {

    }
};
```

### Java

```java
class Solution {
    public int countSubstrings(String s) {

    }
}
```

### Python

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def countSubstrings(self, s: str) -> int:
```

### C

```c


int countSubstrings(char * s){

}
```

### C#

```csharp
public class Solution {
    public int CountSubstrings(string s) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {

};
```

### TypeScript

```typescript
function countSubstrings(s: string): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countSubstrings($s) {

    }
}
```

### Swift

```swift
class Solution {
    func countSubstrings(_ s: String) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String): Int {

    }
}
```

### Go

```golang
func countSubstrings(s string) int {

}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_substrings(s)

end
```

### Scala

```scala
object Solution {
    def countSubstrings(s: String): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_substrings(s: String) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (count-substrings s)
  (-> string? exact-integer?)

  )
```

### Erlang

```erlang
-spec count_substrings(S :: unicode:unicode_binary()) -> integer().
count_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t) :: integer
  def count_substrings(s) do

  end
end
```

