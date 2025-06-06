# 1888. 使二进制字符串字符交替的最少反转次数

## 题目描述

<p>给你一个二进制字符串 <code>s</code> 。你可以按任意顺序执行以下两种操作任意次：</p>

<ul>
	<li><strong>类型 1 ：删除</strong> 字符串 <code>s</code> 的第一个字符并将它 <strong>添加</strong> 到字符串结尾。</li>
	<li><strong>类型 2 ：选择 </strong>字符串 <code>s</code> 中任意一个字符并将该字符 <strong>反转 </strong>，也就是如果值为 <code>'0'</code> ，则反转得到 <code>'1'</code> ，反之亦然。</li>
</ul>

<p>请你返回使 <code>s</code> 变成 <strong>交替</strong> 字符串的前提下， <strong>类型 2 </strong>的 <strong>最少</strong> 操作次数 。</p>

<p>我们称一个字符串是 <strong>交替</strong> 的，需要满足任意相邻字符都不同。</p>

<ul>
	<li>比方说，字符串 <code>"010"</code> 和 <code>"1010"</code> 都是交替的，但是字符串 <code>"0100"</code> 不是。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "111000"
<b>输出：</b>2
<b>解释：</b>执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "10<strong>1</strong>01<strong>0</strong>" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "010"
<b>输出：</b>0
<strong>解释：</strong>字符串已经是交替的。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "1110"
<b>输出：</b>1
<b>解释：</b>对第二个字符执行第二种操作，得到 s = "1<strong>0</strong>10" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 要么是 <code>'0'</code> ，要么是 <code>'1'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 动态规划
- 滑动窗口

## 提示

1. Note what actually matters is how many 0s and 1s are in odd and even positions
2. For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for each parity

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
    int minFlips(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFlips(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFlips(self, s: str) -> int:
        
```

### C

```c
int minFlips(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFlips(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minFlips = function(s) {
    
};
```

### TypeScript

```typescript
function minFlips(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minFlips($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFlips(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlips(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFlips(String s) {
    
  }
}
```

### Go

```golang
func minFlips(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_flips(s)
    
end
```

### Scala

```scala
object Solution {
    def minFlips(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-flips s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_flips(S :: unicode:unicode_binary()) -> integer().
min_flips(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips(s :: String.t) :: integer
  def min_flips(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFlips(s: String): Int64 {

    }
}
```

