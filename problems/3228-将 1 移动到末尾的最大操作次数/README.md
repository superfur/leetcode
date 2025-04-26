# 3228. 将 1 移动到末尾的最大操作次数

## 题目描述

<p>给你一个 <span data-keyword="binary-string">二进制字符串</span> <code>s</code>。</p>

<p>你可以对这个字符串执行 <strong>任意次</strong> 下述操作：</p>

<ul>
	<li>选择字符串中的任一下标 <code>i</code>（ <code>i + 1 &lt; s.length</code> ），该下标满足 <code>s[i] == '1'</code> 且 <code>s[i + 1] == '0'</code>。</li>
	<li>将字符 <code>s[i]</code> 向 <strong>右移 </strong>直到它到达字符串的末端或另一个 <code>'1'</code>。例如，对于 <code>s = "010010"</code>，如果我们选择 <code>i = 1</code>，结果字符串将会是 <code>s = "0<strong><u>001</u></strong>10"</code>。</li>
</ul>

<p>返回你能执行的<strong> 最大 </strong>操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "1001101"</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>可以执行以下操作：</p>

<ul>
	<li>选择下标 <code>i = 0</code>。结果字符串为 <code>s = "<u><strong>001</strong></u>1101"</code>。</li>
	<li>选择下标 <code>i = 4</code>。结果字符串为 <code>s = "0011<u><strong>01</strong></u>1"</code>。</li>
	<li>选择下标 <code>i = 3</code>。结果字符串为 <code>s = "001<strong><u>01</u></strong>11"</code>。</li>
	<li>选择下标 <code>i = 2</code>。结果字符串为 <code>s = "00<strong><u>01</u></strong>111"</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "00111"</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code>。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 计数

## 提示

1. It is optimal to perform the operation on the lowest index possible each time.
2. Traverse the string from left to right and perform the operation every time it is possible.

## 示例

```
"1001101"
"00111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxOperations(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxOperations(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxOperations(self, s: str) -> int:
        
```

### C

```c
int maxOperations(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxOperations(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxOperations = function(s) {
    
};
```

### TypeScript

```typescript
function maxOperations(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxOperations($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxOperations(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxOperations(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxOperations(String s) {
    
  }
}
```

### Go

```golang
func maxOperations(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_operations(s)
    
end
```

### Scala

```scala
object Solution {
    def maxOperations(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_operations(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-operations s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_operations(S :: unicode:unicode_binary()) -> integer().
max_operations(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_operations(s :: String.t) :: integer
  def max_operations(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxOperations(s: String): Int64 {

    }
}
```

