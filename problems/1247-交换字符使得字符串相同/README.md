# 1247. 交换字符使得字符串相同

## 题目描述

<p>有两个长度相同的字符串&nbsp;<code>s1</code> 和&nbsp;<code>s2</code>，且它们其中&nbsp;<strong>只含有</strong>&nbsp;字符&nbsp;<code>"x"</code> 和&nbsp;<code>"y"</code>，你需要通过「交换字符」的方式使这两个字符串相同。</p>

<p>每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。</p>

<p>交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换&nbsp;<code>s1[i]</code> 和&nbsp;<code>s2[j]</code>，但不能交换&nbsp;<code>s1[i]</code> 和&nbsp;<code>s1[j]</code>。</p>

<p>最后，请你返回使 <code>s1</code> 和 <code>s2</code> 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "xx", s2 = "yy"
<strong>输出：</strong>1
<strong>解释：
</strong>交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "xy", s2 = "yx"
<strong>输出：</strong>2
<strong>解释：
</strong>交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s1 = "xx", s2 = "xy"
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 1000</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li><code>s1, s2</code>&nbsp;只包含&nbsp;<code>'x'</code>&nbsp;或&nbsp;<code>'y'</code>。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 字符串

## 提示

1. First, ignore all the already matched positions, they don't affect the answer at all. For the unmatched positions, there are three basic cases (already given in the examples):
2. ("xx", "yy") => 1 swap, ("xy", "yx") => 2 swaps
3. So the strategy is, apply case 1 as much as possible, then apply case 2 if the last two unmatched are in this case, or fall into impossible if only one pair of unmatched left. This can be done via a simple math.

## 示例

```
"xx"
"yy"
"xy"
"yx"
"xx"
"xy"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSwap(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSwap(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
```

### C

```c
int minimumSwap(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSwap(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumSwap = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function minimumSwap(s1: string, s2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function minimumSwap($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSwap(_ s1: String, _ s2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSwap(s1: String, s2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSwap(String s1, String s2) {
    
  }
}
```

### Go

```golang
func minimumSwap(s1 string, s2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_swap(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def minimumSwap(s1: String, s2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_swap(s1: String, s2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-swap s1 s2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_swap(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
minimum_swap(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_swap(s1 :: String.t, s2 :: String.t) :: integer
  def minimum_swap(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSwap(s1: String, s2: String): Int64 {

    }
}
```

