# 3499. 操作后最大活跃区段数 I

## 题目描述

<p>给你一个长度为 <code>n</code> 的二进制字符串 <code>s</code>，其中：</p>

<ul>
	<li><code>'1'</code> 表示一个 <strong>活跃</strong> 区段。</li>
	<li><code>'0'</code> 表示一个 <strong>非活跃</strong> 区段。</li>
</ul>

<p>你可以执行 <strong>最多一次操作</strong>&nbsp;来最大化 <code>s</code> 中的活跃区段数量。在一次操作中，你可以：</p>

<ul>
	<li>将一个被 <code>'0'</code> 包围的连续 <code>'1'</code> 区块转换为全 <code>'0'</code>。</li>
	<li>然后，将一个被 <code>'1'</code> 包围的连续 <code>'0'</code> 区块转换为全 <code>'1'</code>。</li>
</ul>

<p>返回在执行最优操作后，<code>s</code> 中的 <strong>最大</strong> 活跃区段数。</p>

<p><strong>注意：</strong>处理时需要在 <code>s</code> 的两侧加上 <code>'1'</code> ，即 <code>t = '1' + s + '1'</code>。这些加上的 <code>'1'</code> 不会影响最终的计数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "01"</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>因为没有被 <code>'0'</code> 包围的 <code>'1'</code> 区块，因此无法进行有效操作。最大活跃区段数为 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "0100"</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>字符串 <code>"0100"</code> → 两端加上 <code>'1'</code>&nbsp;后得到&nbsp;<code>"101001"</code>&nbsp;。</li>
	<li>选择 <code>"0100"</code>，<code>"10<u><strong>1</strong></u>001"</code> → <code>"1<u><strong>0000</strong></u>1"</code> → <code>"1<u><strong>1111</strong></u>1"</code>&nbsp;。</li>
	<li>最终的字符串去掉两端的 <code>'1'</code>&nbsp;后为 <code>"1111"</code>&nbsp;。最大活跃区段数为 4。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "1000100"</span></p>

<p><strong>输出：</strong> <span class="example-io">7</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>字符串 <code>"1000100"</code> → 两端加上 <code>'1'</code>&nbsp;后得到 <code>"110001001"</code>&nbsp;。</li>
	<li>选择 <code>"000100"</code>，<code>"11000<u><strong>1</strong></u>001"</code> → <code>"11<u><strong>000000</strong></u>1"</code> → <code>"11<u><strong>111111</strong></u>1"</code>。</li>
	<li>最终的字符串去掉两端的 <code>'1'</code>&nbsp;后为 <code>"1111111"</code>。最大活跃区段数为 7。</li>
</ul>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "01010"</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>字符串 <code>"01010"</code> → 两端加上 <code>'1'</code>&nbsp;后得到 <code>"1010101"</code>。</li>
	<li>选择 <code>"010"</code>，<code>"10<u><strong>1</strong></u>0101"</code> → <code>"1<u><strong>000</strong></u>101"</code> → <code>"1<u><strong>111</strong></u>101"</code>。</li>
	<li>最终的字符串去掉两端的 <code>'1'</code>&nbsp;后为 <code>"11110"</code>。最大活跃区段数为 4。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 仅包含 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 枚举

## 提示

1. Split the string into several zero-one segments.
2. For each one-segment, if it has two neighbors (i.e., it is surrounded by two zero-segments), the total sum of their lengths is one of the candidates for <code>delta</code>.
3. Find the maximum <code>delta</code> and add it to the total number of ones in the string.

## 示例

```
"01"
"0100"
"1000100"
"01010"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
```

### C

```c
int maxActiveSectionsAfterTrade(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxActiveSectionsAfterTrade(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxActiveSectionsAfterTrade = function(s) {
    
};
```

### TypeScript

```typescript
function maxActiveSectionsAfterTrade(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxActiveSectionsAfterTrade($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxActiveSectionsAfterTrade(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxActiveSectionsAfterTrade(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxActiveSectionsAfterTrade(String s) {
    
  }
}
```

### Go

```golang
func maxActiveSectionsAfterTrade(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_active_sections_after_trade(s)
    
end
```

### Scala

```scala
object Solution {
    def maxActiveSectionsAfterTrade(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_active_sections_after_trade(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-active-sections-after-trade s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_active_sections_after_trade(S :: unicode:unicode_binary()) -> integer().
max_active_sections_after_trade(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_active_sections_after_trade(s :: String.t) :: integer
  def max_active_sections_after_trade(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxActiveSectionsAfterTrade(s: String): Int64 {

    }
}
```

