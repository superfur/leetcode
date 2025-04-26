# 1963. 使字符串平衡的最小交换次数

## 题目描述

<p>给你一个字符串 <code>s</code> ，<strong>下标从 0 开始</strong> ，且长度为偶数 <code>n</code> 。字符串 <strong>恰好</strong> 由 <code>n / 2</code> 个开括号 <code>'['</code> 和 <code>n / 2</code> 个闭括号 <code>']'</code> 组成。</p>

<p>只有能满足下述所有条件的字符串才能称为 <strong>平衡字符串</strong> ：</p>

<ul>
	<li>字符串是一个空字符串，或者</li>
	<li>字符串可以记作 <code>AB</code> ，其中 <code>A</code> 和 <code>B</code> 都是 <strong>平衡字符串</strong> ，或者</li>
	<li>字符串可以写成 <code>[C]</code> ，其中 <code>C</code> 是一个 <strong>平衡字符串</strong> 。</li>
</ul>

<p>你可以交换 <strong>任意</strong> 两个下标所对应的括号 <strong>任意</strong> 次数。</p>

<p>返回使<em> </em><code>s</code> 变成 <strong>平衡字符串</strong> 所需要的 <strong>最小</strong> 交换次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "][]["
<strong>输出：</strong>1
<strong>解释：</strong>交换下标 0 和下标 3 对应的括号，可以使字符串变成平衡字符串。
最终字符串变成 "[[]]" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "]]][[["
<strong>输出：</strong>2
<strong>解释：</strong>执行下述操作可以使字符串变成平衡字符串：
- 交换下标 0 和下标 4 对应的括号，s = "[]][][" 。
- 交换下标 1 和下标 5 对应的括号，s = "[[][]]" 。
最终字符串变成 "[[][]]" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "[]"
<strong>输出：</strong>0
<strong>解释：</strong>这个字符串已经是平衡字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>n</code> 为偶数</li>
	<li><code>s[i]</code> 为<code>'['</code> 或 <code>']'</code></li>
	<li>开括号 <code>'['</code> 的数目为 <code>n / 2</code> ，闭括号 <code>']'</code> 的数目也是 <code>n / 2</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 双指针
- 字符串

## 提示

1. Iterate over the string and keep track of the number of opening and closing brackets on each step.
2. If the number of closing brackets is ever larger, you need to make a swap.
3. Swap it with the opening bracket closest to the end of s.

## 示例

```
"][]["
"]]][[["
"[]"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSwaps(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSwaps(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSwaps(self, s: str) -> int:
        
```

### C

```c
int minSwaps(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSwaps(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {
    
};
```

### TypeScript

```typescript
function minSwaps(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minSwaps($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSwaps(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSwaps(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSwaps(String s) {
    
  }
}
```

### Go

```golang
func minSwaps(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_swaps(s)
    
end
```

### Scala

```scala
object Solution {
    def minSwaps(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-swaps s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_swaps(S :: unicode:unicode_binary()) -> integer().
min_swaps(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_swaps(s :: String.t) :: integer
  def min_swaps(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSwaps(s: String): Int64 {

    }
}
```

