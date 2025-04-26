# 1147. 段式回文

## 题目描述

<p>你会得到一个字符串&nbsp;<code>text</code>&nbsp;。你应该把它分成 <code>k</code>&nbsp;个子字符串&nbsp;<code>(subtext1, subtext2，…， subtextk)</code>&nbsp;，要求满足:</p>

<ul>
	<li><code>subtext<sub>i</sub></code><sub>&nbsp;</sub>是 <strong>非空&nbsp;</strong>字符串</li>
	<li>所有子字符串的连接等于 <code>text</code> ( 即<code>subtext<sub>1</sub>&nbsp;+ subtext<sub>2</sub>&nbsp;+ ... + subtext<sub>k</sub>&nbsp;== text</code>&nbsp;)</li>
	<li>对于所有 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">i</span></span></font></font>&nbsp;的有效值( 即&nbsp;<code>1 &lt;= i&nbsp;&lt;= k</code> ) ，<code>subtext<sub>i</sub>&nbsp;== subtext<sub>k - i + 1</sub></code> 均成立</li>
</ul>

<p>返回<code>k</code>可能最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>text = "ghiabcdefhelloadamhelloabcdefghi"
<strong>输出：</strong>7
<strong>解释：</strong>我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>text = "merchant"
<strong>输出：</strong>1
<strong>解释：</strong>我们可以把字符串拆分成 "(merchant)"。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>text = "antaprezatepzapreanta"
<strong>输出：</strong>11
<strong>解释：</strong>我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 1000</code></li>
	<li><code>text</code>&nbsp;仅由小写英文字符组成</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 双指针
- 字符串
- 动态规划
- 哈希函数
- 滚动哈希

## 提示

1. Using a rolling hash, we can quickly check whether two strings are equal.
2. Use that as the basis of a dp.

## 示例

```
"ghiabcdefhelloadamhelloabcdefghi"
"merchant"
"antaprezatepzapreanta"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestDecomposition(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestDecomposition(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestDecomposition(self, text: str) -> int:
        
```

### C

```c
int longestDecomposition(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestDecomposition(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var longestDecomposition = function(text) {
    
};
```

### TypeScript

```typescript
function longestDecomposition(text: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function longestDecomposition($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestDecomposition(_ text: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestDecomposition(text: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestDecomposition(String text) {
    
  }
}
```

### Go

```golang
func longestDecomposition(text string) int {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {Integer}
def longest_decomposition(text)
    
end
```

### Scala

```scala
object Solution {
    def longestDecomposition(text: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_decomposition(text: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-decomposition text)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_decomposition(Text :: unicode:unicode_binary()) -> integer().
longest_decomposition(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_decomposition(text :: String.t) :: integer
  def longest_decomposition(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestDecomposition(text: String): Int64 {

    }
}
```

