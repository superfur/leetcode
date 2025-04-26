# 1864. 构成交替字符串需要的最小交换次数

## 题目描述

<p>给你一个二进制字符串 <code>s</code> ，现需要将其转化为一个 <strong>交替字符串</strong> 。请你计算并返回转化所需的 <strong>最小</strong> 字符交换次数，如果无法完成转化，返回<em> </em><code>-1</code><em> </em>。</p>

<p><strong>交替字符串</strong> 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 <code>"010"</code> 和 <code>"1010"</code> 属于交替字符串，但 <code>"0100"</code> 不是。</p>

<p>任意两个字符都可以进行交换，<strong>不必相邻</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "111000"
<strong>输出：</strong>1
<strong>解释：</strong>交换位置 1 和 4："1<em><strong>1</strong></em>10<em><strong>0</strong></em>0" -> "1<em><strong>0</strong></em>10<em><strong>1</strong></em>0" ，字符串变为交替字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "010"
<strong>输出：</strong>0
<strong>解释：</strong>字符串已经是交替字符串了，不需要交换。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "1110"
<strong>输出：</strong>-1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 1000</code></li>
	<li><code>s[i]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. Think about all valid strings of length n.
2. Try to count the mismatched positions with each valid string of length n.

## 示例

```
"111000"
"010"
"1110"
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

