# 1830. 使字符串有序的最少操作次数

## 题目描述

<p>给你一个字符串 <code>s</code> （<strong>下标从 0 开始</strong>）。你需要对 <code>s</code> 执行以下操作直到它变为一个有序字符串：</p>

<ol>
	<li>找到 <strong>最大下标</strong> <code>i</code> ，使得 <code>1 &lt;= i &lt; s.length</code> 且 <code>s[i] &lt; s[i - 1]</code> 。</li>
	<li>找到 <strong>最大下标</strong> <code>j</code> ，使得 <code>i &lt;= j &lt; s.length</code> 且对于所有在闭区间 <code>[i, j]</code> 之间的 <code>k</code> 都有 <code>s[k] &lt; s[i - 1]</code> 。</li>
	<li>交换下标为 <code>i - 1</code>​​​​ 和 <code>j</code>​​​​ 处的两个字符。</li>
	<li>将下标 <code>i</code> 开始的字符串后缀反转。</li>
</ol>

<p>请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "cba"
<b>输出：</b>5
<b>解释：</b>模拟过程如下所示：
操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。
操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。
操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。
操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。
操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "aabaa"
<b>输出：</b>2
<b>解释：</b>模拟过程如下所示：
操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。
操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "cdbea"
<b>输出：</b>63</pre>

<p><strong>示例 4：</strong></p>

<pre><b>输入：</b>s = "leetcodeleetcodeleetcode"
<b>输出：</b>982157772
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code>​ 只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 组合数学

## 提示

1. Note that the operations given describe getting the previous permutation of s
2. To solve this problem you need to solve every suffix separately

## 示例

```
"cba"
"aabaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int makeStringSorted(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int makeStringSorted(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeStringSorted(self, s: str) -> int:
        
```

### C

```c
int makeStringSorted(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MakeStringSorted(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var makeStringSorted = function(s) {
    
};
```

### TypeScript

```typescript
function makeStringSorted(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function makeStringSorted($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeStringSorted(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeStringSorted(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeStringSorted(String s) {
    
  }
}
```

### Go

```golang
func makeStringSorted(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def make_string_sorted(s)
    
end
```

### Scala

```scala
object Solution {
    def makeStringSorted(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_string_sorted(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (make-string-sorted s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec make_string_sorted(S :: unicode:unicode_binary()) -> integer().
make_string_sorted(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_string_sorted(s :: String.t) :: integer
  def make_string_sorted(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeStringSorted(s: String): Int64 {

    }
}
```

