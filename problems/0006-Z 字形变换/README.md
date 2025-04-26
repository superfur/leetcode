# 6. Z 字形变换

## 题目描述

<p>将一个给定字符串 <code>s</code> 根据给定的行数 <code>numRows</code> ，以从上往下、从左到右进行 Z 字形排列。</p>

<p>比如输入字符串为 <code>"PAYPALISHIRING"</code> 行数为 <code>3</code> 时，排列如下：</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R</pre>

<p>之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：<code>"PAHNAPLSIIGYIR"</code>。</p>

<p>请你实现这个将字符串进行指定行数变换的函数：</p>

<pre>
string convert(string s, int numRows);</pre>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "PAYPALISHIRING", numRows = 3
<strong>输出：</strong>"PAHNAPLSIIGYIR"
</pre>
<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>s = "PAYPALISHIRING", numRows = 4
<strong>输出：</strong>"PINALSIGYAHRPI"
<strong>解释：</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "A", numRows = 1
<strong>输出：</strong>"A"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 1000</code></li>
	<li><code>s</code> 由英文字母（小写和大写）、<code>','</code> 和 <code>'.'</code> 组成</li>
	<li><code>1 <= numRows <= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 示例

```
"PAYPALISHIRING"
3
"PAYPALISHIRING"
4
"A"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        
    }
};
```

### Java

```java
class Solution {
    public String convert(String s, int numRows) {
        
    }
}
```

### Python

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
```

### C

```c
char* convert(char* s, int numRows) {
    
}
```

### C#

```csharp
public class Solution {
    public string Convert(string s, int numRows) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    
};
```

### TypeScript

```typescript
function convert(s: string, numRows: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        
    }
}
```

### Swift

```swift
class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun convert(s: String, numRows: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String convert(String s, int numRows) {
    
  }
}
```

### Go

```golang
func convert(s string, numRows int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
    
end
```

### Scala

```scala
object Solution {
    def convert(s: String, numRows: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (convert s numRows)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec convert(S :: unicode:unicode_binary(), NumRows :: integer()) -> unicode:unicode_binary().
convert(S, NumRows) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec convert(s :: String.t, num_rows :: integer) :: String.t
  def convert(s, num_rows) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func convert(s: String, numRows: Int64): String {

    }
}
```

