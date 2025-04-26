# LCR 097. 不同的子序列

## 题目描述

<p>给定一个字符串 <code>s</code> 和一个字符串 <code>t</code> ，计算在 <code>s</code> 的子序列中 <code>t</code> 出现的个数。</p>

<p>字符串的一个 <strong>子序列</strong> 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，<code>&quot;ACE&quot;</code> 是 <code>&quot;ABCDE&quot;</code> 的一个子序列，而 <code>&quot;AEC&quot;</code> 不是）</p>

<p>题目数据保证答案符合 32 位带符号整数范围。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;rabbbit&quot;, t = &quot;rabbit&quot;
<strong>输出：</strong>3
<strong>解释：</strong>
如下图所示, 有 3 种可以从 s 中得到 &quot;rabbit&quot; 的方案。
<strong><u>rabb</u></strong>b<strong><u>it</u></strong>
<strong><u>ra</u></strong>b<strong><u>bbit</u></strong>
<strong><u>rab</u></strong>b<strong><u>bit</u></strong></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;babgbag&quot;, t = &quot;bag&quot;
<strong>输出：</strong>5
<strong>解释：</strong>
如下图所示, 有 5 种可以从 s 中得到 &quot;bag&quot; 的方案。 
<strong><u>ba</u></strong>b<u><strong>g</strong></u>bag
<strong><u>ba</u></strong>bgba<strong><u>g</u></strong>
<u><strong>b</strong></u>abgb<strong><u>ag</u></strong>
ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u>
babg<strong><u>bag</u></strong>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 115 题相同： <a href="https://leetcode-cn.com/problems/distinct-subsequences/">https://leetcode-cn.com/problems/distinct-subsequences/</a></p>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 示例

```
"rabbbit"
"rabbit"
"babgbag"
"bag"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numDistinct(string s, string t) {

    }
};
```

### Java

```java
class Solution {
    public int numDistinct(String s, String t) {

    }
}
```

### Python

```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
```

### C

```c


int numDistinct(char * s, char * t){

}
```

### C#

```csharp
public class Solution {
    public int NumDistinct(string s, string t) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {

};
```

### TypeScript

```typescript
function numDistinct(s: string, t: string): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function numDistinct($s, $t) {

    }
}
```

### Swift

```swift
class Solution {
    func numDistinct(_ s: String, _ t: String) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numDistinct(s: String, t: String): Int {

    }
}
```

### Go

```golang
func numDistinct(s string, t string) int {

}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def num_distinct(s, t)

end
```

### Scala

```scala
object Solution {
    def numDistinct(s: String, t: String): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (num-distinct s t)
  (-> string? string? exact-integer?)

  )
```

### Erlang

```erlang
-spec num_distinct(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
num_distinct(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_distinct(s :: String.t, t :: String.t) :: integer
  def num_distinct(s, t) do

  end
end
```

