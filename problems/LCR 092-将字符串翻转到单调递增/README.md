# LCR 092. 将字符串翻转到单调递增

## 题目描述

<p>如果一个由&nbsp;<code>&#39;0&#39;</code> 和 <code>&#39;1&#39;</code>&nbsp;组成的字符串，是以一些 <code>&#39;0&#39;</code>（可能没有 <code>&#39;0&#39;</code>）后面跟着一些 <code>&#39;1&#39;</code>（也可能没有 <code>&#39;1&#39;</code>）的形式组成的，那么该字符串是&nbsp;<strong>单调递增&nbsp;</strong>的。</p>

<p>我们给出一个由字符 <code>&#39;0&#39;</code> 和 <code>&#39;1&#39;</code>&nbsp;组成的字符串 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="caret-color: rgb(199, 37, 78); font-size: 12.600000381469727px; background-color: rgb(249, 242, 244);">s</span></font>，我们可以将任何&nbsp;<code>&#39;0&#39;</code> 翻转为&nbsp;<code>&#39;1&#39;</code>&nbsp;或者将&nbsp;<code>&#39;1&#39;</code>&nbsp;翻转为&nbsp;<code>&#39;0&#39;</code>。</p>

<p>返回使 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="caret-color: rgb(199, 37, 78); font-size: 12.600000381469727px; background-color: rgb(249, 242, 244);">s</span></font>&nbsp;<strong>单调递增&nbsp;</strong>的最小翻转次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s =<strong> </strong>&quot;00110&quot;
<strong>输出：</strong>1
<strong>解释：</strong>我们翻转最后一位得到 00111.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s =<strong> </strong>&quot;010110&quot;
<strong>输出：</strong>2
<strong>解释：</strong>我们翻转得到 011111，或者是 000111。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s =<strong> </strong>&quot;00011000&quot;
<strong>输出：</strong>2
<strong>解释：</strong>我们翻转得到 00000000。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20000</code></li>
	<li><font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="caret-color: rgb(199, 37, 78); font-size: 12.600000381469727px; background-color: rgb(249, 242, 244);">s</span></font> 中只包含字符&nbsp;<code>&#39;0&#39;</code>&nbsp;和&nbsp;<code>&#39;1&#39;</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 926&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/">https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/</a></p>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 示例

```
"00110"
"010110"
"00011000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFlipsMonoIncr(string s) {

    }
};
```

### Java

```java
class Solution {
    public int minFlipsMonoIncr(String s) {

    }
}
```

### Python

```python
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
```

### C

```c


int minFlipsMonoIncr(char * s){

}
```

### C#

```csharp
public class Solution {
    public int MinFlipsMonoIncr(string s) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {

};
```

### TypeScript

```typescript
function minFlipsMonoIncr(s: string): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minFlipsMonoIncr($s) {

    }
}
```

### Swift

```swift
class Solution {
    func minFlipsMonoIncr(_ s: String) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlipsMonoIncr(s: String): Int {

    }
}
```

### Go

```golang
func minFlipsMonoIncr(s string) int {

}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_flips_mono_incr(s)

end
```

### Scala

```scala
object Solution {
    def minFlipsMonoIncr(s: String): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (min-flips-mono-incr s)
  (-> string? exact-integer?)

  )
```

### Erlang

```erlang
-spec min_flips_mono_incr(S :: unicode:unicode_binary()) -> integer().
min_flips_mono_incr(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips_mono_incr(s :: String.t) :: integer
  def min_flips_mono_incr(s) do

  end
end
```

