# 1758. 生成交替二进制字符串的最少操作数

## 题目描述

<p>给你一个仅由字符 <code>'0'</code> 和 <code>'1'</code> 组成的字符串 <code>s</code> 。一步操作中，你可以将任一 <code>'0'</code> 变成 <code>'1'</code> ，或者将 <code>'1'</code> 变成 <code>'0'</code> 。</p>

<p><strong>交替字符串</strong> 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 <code>"010"</code> 是交替字符串，而字符串 <code>"0100"</code> 不是。</p>

<p>返回使 <code>s</code> 变成 <strong>交替字符串</strong> 所需的 <strong>最少</strong> 操作数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "0100"
<strong>输出：</strong>1
<strong>解释：</strong>如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "10"
<strong>输出：</strong>0
<strong>解释：</strong>s 已经是交替字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = "1111"
<strong>输出：</strong>2
<strong>解释：</strong>需要 2 步操作得到 "0101" 或 "1010" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s[i]</code> 是 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Think about how the final string will look like.
2. It will either start with a '0' and be like '010101010..' or with a '1' and be like '10101010..'
3. Try both ways, and check for each way, the number of changes needed to reach it from the given string. The answer is the minimum of both ways.

## 示例

```
"0100"
"10"
"1111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, s: str) -> int:
        
```

### C

```c
int minOperations(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    
};
```

### TypeScript

```typescript
function minOperations(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minOperations($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(String s) {
    
  }
}
```

### Go

```golang
func minOperations(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_operations(s)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(S :: unicode:unicode_binary()) -> integer().
min_operations(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(s :: String.t) :: integer
  def min_operations(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(s: String): Int64 {

    }
}
```

