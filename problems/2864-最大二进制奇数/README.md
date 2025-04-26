# 2864. 最大二进制奇数

## 题目描述

<p>给你一个 <strong>二进制</strong> 字符串 <code>s</code> ，其中至少包含一个 <code>'1'</code> 。</p>

<p>你必须按某种方式 <strong>重新排列</strong> 字符串中的位，使得到的二进制数字是可以由该组合生成的 <strong>最大二进制奇数</strong> 。</p>

<p>以字符串形式，表示并返回可以由给定组合生成的最大二进制奇数。</p>

<p><strong>注意 </strong>返回的结果字符串 <strong>可以</strong> 含前导零。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "010"
<strong>输出：</strong>"001"
<strong>解释：</strong>因为字符串 s 中仅有一个 '1' ，其必须出现在最后一位上。所以答案是 "001" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0101"
<strong>输出：</strong>"1001"
<strong>解释：</strong>其中一个 '1' 必须出现在最后一位上。而由剩下的数字可以生产的最大数字是 "100" 。所以答案是 "1001" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由 <code>'0'</code> 和 <code>'1'</code> 组成</li>
	<li><code>s</code> 中至少包含一个 <code>'1'</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学
- 字符串

## 提示

1. The binary representation of an odd number contains <code>'1'</code> in the least significant place.

## 示例

```
"010"
"0101"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String maximumOddBinaryNumber(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
```

### C

```c
char* maximumOddBinaryNumber(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    
};
```

### TypeScript

```typescript
function maximumOddBinaryNumber(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function maximumOddBinaryNumber($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumOddBinaryNumber(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumOddBinaryNumber(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String maximumOddBinaryNumber(String s) {
    
  }
}
```

### Go

```golang
func maximumOddBinaryNumber(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def maximum_odd_binary_number(s)
    
end
```

### Scala

```scala
object Solution {
    def maximumOddBinaryNumber(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-odd-binary-number s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec maximum_odd_binary_number(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
maximum_odd_binary_number(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_odd_binary_number(s :: String.t) :: String.t
  def maximum_odd_binary_number(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumOddBinaryNumber(s: String): String {

    }
}
```

